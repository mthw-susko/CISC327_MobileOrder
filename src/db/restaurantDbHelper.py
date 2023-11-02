import sqlite3
import os
import ast
from model.restaurant import Restaurant
from db.menuItemDbHelper import MenuItemDbHelper


class RestaurantDbHelper:
    '''Translates frontend code to interact with the database'''

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open(self):
        # Get the absolute path to the parent directory where the DB is
        scriptDir = os.path.dirname(__file__)
        parentDir = os.path.abspath(os.path.join(scriptDir, '..'))

        # Replace 'your_database.db' with the actual path
        dbFile = os.path.join(parentDir, 'dataBase.db')
        conn = sqlite3.connect(dbFile)
        self.cursor = conn.cursor()
        self.conn = conn

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def getRestaurants(self):
        self.open()
        self.cursor.execute("SELECT * FROM Restaurant")
        result = self.cursor.fetchall()
        self.close()
        if result:
            menuItemDb = MenuItemDbHelper()
            restaurants = []

            for restaurant in result:
                menuItemNames = ast.literal_eval(restaurant[2])
                menuItems = menuItemDb.getMenuItems(menuItemNames)
                restaurants.append(Restaurant(
                    restaurant[0], restaurant[1], menuItems, restaurant[3]))

            return restaurants
        else:
            return None
