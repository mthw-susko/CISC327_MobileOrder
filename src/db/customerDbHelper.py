import sqlite3
import os
import ast


class CustomerDbHelper:
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

    def getCustomers(self):
        self.open()
        self.cursor.execute("SELECT * FROM Customer")
        result = self.cursor.fetchall()
        self.close()
        if result:
            customerDict = {}
            for customer in result:
                customerDict[customer[2]] = customer[3]
            return customerDict
        else:
            return None

    def addCustomer(self, name, username, password, email, address, creditCardInfo):
        # make sure card number and security codes are Integers
        creditCardInfo[1] = int(creditCardInfo[1])
        creditCardInfo[3] = int(creditCardInfo[3])
        self.open()
        self.cursor.execute(
            "INSERT INTO Customer (name, username, password, email, address, creditCardInfo) VALUES (?, ?, ?, ?, ?, ?)", (name, username, password, email, address, str(creditCardInfo),))
        self.close()

    def getCustomerId(self, username):
        self.open()
        self.cursor.execute(
            "SELECT id FROM Customer WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        self.close()
        if result:
            return result[0]
        else:
            return None

    def getCustomerName(self, username):
        self.open()
        self.cursor.execute(
            "SELECT name FROM Customer WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        self.close()
        if result:
            return result[0]
        else:
            return None

    def getCreditCardInfo(self, username):
        self.open()
        self.cursor.execute(
            "SELECT creditCardInfo FROM Customer WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        self.close()
        if result:
            return ast.literal_eval(result[0])
        else:
            return None
