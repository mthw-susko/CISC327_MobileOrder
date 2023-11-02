import sqlite3
import os
import random


class OrderDbHelper:
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

    def addOrder(self, customerId, items, orderStatus, totalPrice):
        self.open()
        self.cursor.execute(
            """INSERT INTO "Order" (customerId, items, orderStatus, totalPrice) VALUES(?, ?, ?, ?)""", (customerId, str([item.name for item in items]), orderStatus, totalPrice))
        self.close()
