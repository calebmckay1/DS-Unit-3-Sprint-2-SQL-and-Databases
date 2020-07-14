#! /usr/bin/env python

"""
    How many total Characters are there?
    How many of each specific subclass?
    How many total Items?
    How many of the Items are weapons? How many are not?
    How many Items does each character have? (Return first 20 rows)
    How many Weapons does each character have? (Return first 20 rows)
    On average, how many Items does each Character have?
    On average, how many Weapons does each character have?
"""

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there? table: charactercreator_character
count_characters = 'SELECT COUNT(*) FROM charactercreator_character;'
print(curs.execute(count_characters).fetchall())


# How many of each specific subclass?
count_mages = 'SELECT COUNT(*) FROM charactercreator_mage;'
print(curs.execute(count_mages).fetchall())

    
# How many total Items?
count_items = 'SELECT COUNT(*) FROM armory_item;'
print(curs.execute(count_items).fetchall())    


# How many of the Items are weapons? How many are not?
count_weapons = 'SELECT COUNT(*) FROM armory_item WHERE item like("%WEAPON%");'
print(curs.execute(count_weapons).fetchall())


# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have
