# Import statements
from flask import (
    Flask,
    flash,
    render_template,
    url_for,
    redirect,
    request,
    jsonify,
    make_response)
from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Cuisine, Dish, User

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

import random
import string
import httplib2
import json
import requests

# End imports

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

app = Flask(__name__)


# Connect to the database
engine = create_engine('sqlite:///cuisines.db',
                       connect_args={'check_same_thread': False},
                       echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Google token creation
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Compare tokens to authorize user
@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps(
            'Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If token process led to an error, abort
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
    # Verify the user token is a match
    google_id = credentials.id_token['sub']
    if result['user_id'] != google_id:
        response = make_response(json.dumps(
            "Token's user ID doesn't match given user ID"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify the client token matches
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps(
            "Token's client ID doesn't match app's"), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check if user is logged in already
    stored_credentials = login_session.get('credentials')
    stored_google_id = login_session.get('google_id')
    if stored_credentials is not None and google_id == stored_google_id:
        response = make_response(json.dumps(
            'Current user is already connected'), 200)
        response.headers['Content-Type'] = 'application/json'

    # Store access token
    login_session['credentials'] = credentials
    login_session['google_id'] = google_id

    # Get user information
    userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# Log out
@app.route('/gdisconnect')
def gdisconnect():
    # Check if user is logged in
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current user not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset user session
        del login_session['credentials']
        del login_session['google_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# Homepage that shows all the cuisines
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    cuisines = session.query(Cuisine).all()
    return render_template('catalog.html', cuisines=cuisines)


# Shows all the dishes under a cuisine
@app.route('/catalog/<int:cuisine_id>/')
@app.route('/catalog/<int:cuisine_id>/dishes/')
def showDishes(cuisine_id):
    cuisine = session.query(Cuisine).filter_by(id=cuisine_id).one()
    dishes = session.query(Dish).filter_by(cuisine_id=cuisine_id).all()
    # If not logged in, all pages can be viewed, but edit/del buttons are gone
    if 'username' not in login_session:
        return render_template('publicDishes.html', dishes=dishes,
                               cuisine=cuisine)
    return render_template('dishes.html', dishes=dishes, cuisine=cuisine,
                           user_id=login_session['user_id'])


# Create a new dish
@app.route('/catalog/<int:cuisine_id>/new/', methods=['GET', 'POST'])
def newDish(cuisine_id):
    if 'username' not in login_session:
        return redirect('/login/')
    if request.method == 'POST':
        newDish = Dish(
            name=request.form['name'],
            description=request.form['description'],
            cuisine_id=cuisine_id,
            user_id=login_session['user_id']
            )
        session.add(newDish)
        session.commit()
        return redirect(url_for('showDishes', cuisine_id=cuisine_id))
    else:
        return render_template('newDish.html', cuisine_id=cuisine_id)


# Edit a dish
@app.route('/catalog/<int:cuisine_id>/dish/<int:dish_id>/edit/',
           methods=['GET', 'POST'])
def editDish(cuisine_id, dish_id):
    if 'username' not in login_session:
        return redirect('/login/')
    editedDish = session.query(Dish).filter_by(id=dish_id).one()
    if login_session['user_id'] != editedDish.user_id:
        return """<script>function myFunction() {alert('You must be the creator
               of a dish to edit it.);}</script><body onload='myFunction()'>"""
    if request.method == 'POST':
        if request.form['name']:
            editedDish.name = request.form['name']
        if request.form['description']:
            editedDish.description = request.form['description']
        session.add(editedDish)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template(
            'editDish.html',
            cuisine_id=cuisine_id,
            dish_id=dish_id,
            dish=editedDish
            )


# Delete a dish
@app.route('/catalog/dish/<int:dish_id>/delete/', methods=['GET', 'POST'])
def deleteDish(dish_id):
    if 'username' not in login_session:
        return redirect('/login/')
    dishToDelete = session.query(Dish).filter_by(id=dish_id).one()
    if login_session['user_id'] != dishToDelete.user_id:
        return """<script>function myFunction() {alert('You must be the creator
               of a dish to delete it.);}</script><body
               onload='myFunction()'>"""
    if request.method == 'POST':
        session.delete(dishToDelete)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('deleteDish.html', dish=dishToDelete)


# JSON endpoint for a dish
@app.route('/catalog/<int:cuisine_id>/dish/<int:dish_id>/JSON/')
def dishJSON(cuisine_id, dish_id):
    One_Dish = session.query(Dish).filter_by(id=dish_id).one()
    return jsonify(One_Dish=One_Dish.serialize)


# Create a user in the database for tracking ownership of dishes
def createUser(login_session):
    newUser = User(
                   name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture']
                   )
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Return user id associated with an item
def getUserInfo(user_id_):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# Return email associated with user id
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
