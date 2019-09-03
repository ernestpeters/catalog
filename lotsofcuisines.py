from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Cuisine, Dish, User

engine = create_engine('sqlite:///cuisines.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Dummy user account that will attach to all the dishes created in this file
user1 = User(name="Python Script User", email="dummy")
session.add(user1)
session.commit()

# Italian
cuisine1 = Cuisine(name="Italian")
session.add(cuisine1)
session.commit()

dish1 = Dish(user_id=1, name="Baccala alla Vicentina",
             description="""Stockfish (dried cod) covered with flour, placed on
             top of anchovies, onions, and parsley, simmered in milk for 4
             hours, and topped with parmesan.""", cuisine=cuisine1)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Bistecca alla Fiorentina",
             description="""Thick T-bone brushed with oil by rosemary sprigs,
             grilled rare.""", cuisine=cuisine1)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Pollo alla Cacciatora",
             description="""Chicken coated with flour and browned, then
             simmered in a sauce made of white wine, tomatoes, rosemary,
             olives, and capers.""", cuisine=cuisine1)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Ossobuco",
             description="""Veal shanks braised with vegetables, white wine,
             and broth.  Traditionally it's flavored with lemon, garlic,
             parsley, and cinnamon.  But an alternative is tomatoes, carrots,
             celery and onions.""", cuisine=cuisine1)
session.add(dish4)
session.commit()

# Chinese
cuisine2 = Cuisine(name="Chinese")
session.add(cuisine2)
session.commit()

dish1 = Dish(user_id=1, name="Peking Duck",
             description="""Duck coated and filled with syrup made of sugar and
             soy sauce, oven-roasted, then sliced at the table by the cook.
             Skin is served with a garlic sauce dip, and meat is served with
             pancakes.""", cuisine=cuisine2)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Jellyfish Salad",
             description="""Boiled and chilled jellyfish becomes crunchy.  Then
             it's marinated with vinegar, sugar, soy sauce, and sesame oil.""",
             cuisine=cuisine2)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Beef Chow Fun",
             description="""Stir-fried marinated beef, wide rice noodles, and
             bean sprouts.  Additional flavors are wine, soy sauce, garlic,
             onion, and ginger.""", cuisine=cuisine2)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Xiaolongbao",
             description="""Steamed dumplings filled with soup.  Fillings can
             include pork, crab meat, roe, shrimp, or vegetables.  They are
             dipped in black vinegar after cooking.""", cuisine=cuisine2)
session.add(dish4)
session.commit()


# Japanese
cuisine3 = Cuisine(name="Japanese")
session.add(cuisine3)
session.commit()

dish1 = Dish(user_id=1, name="Unadon",
             description="""Eel filets (known as unagi) glazed with sweetened
             soy sauce, grilled, and placed on steamed white rice.  Japanese
             pepper is sprinkled on top.""", cuisine=cuisine3)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Soba",
             description="""Thin buckwheat noodles can be served hot as a soup,
             or chilled with dipping sauce.""", cuisine=cuisine3)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Udon",
             description="""Thick wheat noodles usually served in soup flavored
             with dashi (stock), soy sauce, and mirin (rice wine).  Common
             toppings are scallions, tempura, and deep-fried tofu.""",
             cuisine=cuisine3)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Yakitori",
             description="""Skewered chicken, grilled.  Commonly seasoned with
             salt, or a sauce made of rice wine, soy sauce, and sugar.""",
             cuisine=cuisine3)
session.add(dish4)
session.commit()


# Thai
cuisine4 = Cuisine(name="Thai")
session.add(cuisine4)
session.commit()

dish1 = Dish(user_id=1, name="Tom Yam Goong",
             description="""Soup base made of roasted chilies, shallots, and
             garlic, cooked with shrimp.  Some additions include lemongrass,
             mushrooms, cilantro, and tomatoes.""", cuisine=cuisine4)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Pad Thai",
             description="""Stir-fried rice noodles, eggs, and tofu, flavored
             with tamarind pulp, shrimp, fish sauce, garlic, chili pepper, and
             sugar.  Peanuts are often added.""", cuisine=cuisine4)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Som Tam",
             description="""Green papaya salad with lime, chili pepper, fish
             sauce, and sugar.  It is very spicy.""", cuisine=cuisine4)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Massamann Curry",
             description="""Mild curry flavored with chili peppers, cilantro,
             lemongrass, and shallots.  It's commonly made with chicken.""",
             cuisine=cuisine4)
session.add(dish4)
session.commit()


# French
cuisine5 = Cuisine(name="French")
session.add(cuisine5)
session.commit()

dish1 = Dish(user_id=1, name="Chicken Marengo",
             description="""Chicken sauteed with nutmeg, then simmered with
             wine and broth, then topped with parsley and lemon juice.""",
             cuisine=cuisine5)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Hachis Parmentier",
             description="""Mashed potato combined with ground or diced meat,
             combined with white wine, vinegar and onions.  It's traditionally
             served in the potato skins.""", cuisine=cuisine5)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Jambon-beurre",
             description="""A baguette sliced open, buttered, and filled with
             ham.""", cuisine=cuisine5)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Poulet Chasseur",
             description="""Sauteed chicken, simmered in a sauce of tomatoes,
             mushrooms, onions, white wine, brandy, and tarragon.""",
             cuisine=cuisine5)
session.add(dish4)
session.commit()


# Spanish
cuisine6 = Cuisine(name="Spanish")
session.add(cuisine6)
session.commit()

dish1 = Dish(user_id=1, name="Croquette",
             description="""Breaded, fried roll filled with white sauce and
             ham, chicken, or cod.  Sometimes they get weird and include apple
             or blood sausage instead.""", cuisine=cuisine6)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Tortilla Espanola",
             description="""Diced, sauteed potatoes mixed with eggs, then
             fried. Optional additions are onion, garlic, parsley, and
             oregano.""", cuisine=cuisine6)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Salmorejo",
             description="""Skinned tomatoes, bread, oil, and garlic are pureed
             and served cold.  It's usually served with diced ham and
             hard-boiled eggs.""", cuisine=cuisine6)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Pisto",
             description="""Tomatoes, onions, eggplant, and bell peppers, all
             diced, served hot, either with bread on side or an egg on top.""",
             cuisine=cuisine6)
session.add(dish4)
session.commit()


# Mexican
cuisine7 = Cuisine(name="Mexican")
session.add(cuisine7)
session.commit()

dish1 = Dish(user_id=1, name="Chilaquiles",
             description="""Quartered, fried corn tortillas covered with red
             salsa and pulled chicken and simmered.  It's topped with crema,
             white cheese, raw onions, and avocado.""", cuisine=cuisine7)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Pozole",
             description="""Soup made of hominy and pork.  It can be topped
             with many ingredients, such as shredded cabbage, avocado, and
             chile peppers.  It's served at celebrations.""", cuisine=cuisine7)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Tacos al Pastor",
             description="""Tacos filled with shawarma spit-grilled pork.  The
             meat is sliced very thin.  It can be served with pineapple.  This
             dish was created in the 20th century during a wave of Lebanese
             immigration.""", cuisine=cuisine7)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Chiles en Nogada",
             description="""Poblano peppers filled with shredded meat, fruits,
             and spices, then topped with a walnut-based cream sauce and
             pomegranate seeds.  It's served at room temperature.""",
             cuisine=cuisine7)
session.add(dish4)
session.commit()


# Indian
cuisine8 = Cuisine(name="Indian")
session.add(cuisine8)
session.commit()

dish1 = Dish(user_id=1, name="Makhan Murg",
             description="""Chicken is marinated in lemon juice, yogurt, and a
             blend of spices.  Then it's cooked in a clay oven, served in a
             curry sauce made of tomato, onion, and butter.""",
             cuisine=cuisine8)
session.add(dish1)
session.commit()

dish2 = Dish(user_id=1, name="Tandoori Chicken",
             description="""Chicken marinated in yogurt and a spice blend, then
             covered with a red spice such as turmeric or red chili powder.
             It's skewered and cooked at very high temperatures.""",
             cuisine=cuisine8)
session.add(dish2)
session.commit()

dish3 = Dish(user_id=1, name="Chole Bhture",
             description="Spicy white chickpeas and deep-fried bread.",
             cuisine=cuisine8)
session.add(dish3)
session.commit()

dish4 = Dish(user_id=1, name="Palak Paneer",
             description="""Pureed spinach and Indian cheese, seasoned with
             garlic, ginger, and a blend of Indian spices.""",
             cuisine=cuisine8)
session.add(dish4)
session.commit()


print "added cuisines"
