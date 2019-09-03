# Item Catalog Project
=====================
## About
A website run by Python that holds information about dishes from various global cuisines.
## Prerequisites
Python
Web browser
Google account
Werkzeug 0.8.3: `sudo pip install werkzeug==0.8.3`
Flask 0.9: `sudo pip install flask==0.9`
Flask-Login 0.1.3 `sudo pip install Flask-Login==0.1.3`
### Directions
Unzip catalog.zip.
Open a terminal where you unzipped.
Run application.py: `python application.py`.
Website is hosted at `http://localhost:5000`.
JSON endpoint for a given dish is `http://localhost:5000/catalog/<cuisine id>/dish/<dish id>/JSON/`.
All users can read the website.
Log in with your Google account to create, update, or delete.
### If you want a fresh database
Stop the webserver started by application.py.
Delete cuisines.db.
Run database_setup.py to create the database: `python database_setup.py`.
Run lotsofcuisines.py to add the cuisines, along with some example dishes, to the database: `python lotsofcuisines.py`.
