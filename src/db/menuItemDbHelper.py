
import sqlite3
import os
from model.menuItem import MenuItem


class MenuItemDbHelper:
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

    def getMenuItems(self, items):
        self.open()
        rawMenuItems = []
        for item in items:
            self.cursor.execute(
                "SELECT * FROM MenuItem WHERE name = ?", (item,))
            rawMenuItems.append(self.cursor.fetchone())
        self.close()

        if rawMenuItems:
            print(rawMenuItems)
            menuItems = [MenuItem(item[0], item[1], item[2], int(
                item[3]), int(item[4])) for item in rawMenuItems]
            return menuItems
        else:
            return None
