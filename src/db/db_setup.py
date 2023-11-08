# DB has been setup. Run this file ONLY if db needs to be reset with initial data
# Note that Order is a keyword in sqlite3 thus the "Order"
import sqlite3

# Define data
customer_data = [
    (1, "Jabez", "Jabezng1", "Hello100", "jabezng1@gmail.com",
     "Queens University", "['CreditCard', 12345678910, '12/24', 123]"),
    (2, "Matthew", "Matthewsusko2", "Hello101", "matthewsusko2@gmail.com",
     "Queens University 1", "['CreditCard', 2468101214, '12/26', 246]"),
    (3, "Aiden", "Aidenhennigar3", "Hello102", "aidenhennigar3@gmail.com",
     "Queens University 2", "['DebitCard', 01987654321, '12/27', 369]")
]

restaurant_data = [
    (1, "MacDonalds", "['BigMac', 'MacChicken']", 0),
    (2, "KFC", "['ChickenTenders', 'SpicyChicken']", 1)
]

order_data = [
    (1, 1, "['BigMac', 'MacChicken']", "Pending", 20.80),
    (2, 3, "['ChickenTenders']", "Delivering", 10.20)
]

menu_item_data = [
    (1, "BigMac", "A big burger", 400, 10.40),
    (2, "MacChicken", "A chicken buger", 350, 10.40),
    (3, "ChickenTenders", "A tender chicken", 250, 10.20),
    (4, "SpicyChicken", "A spicy chicken", 300, 10.40)
]

# Connect to the database
connection = sqlite3.connect('src/dataBase.db')
cursor = connection.cursor()

# Define SQL statements to insert data to tables
customer_sql = 'INSERT INTO Customer(id, name, username, password, email, address, creditCardInfo) VALUES(?,?,?,?,?,?,?)'
restaurant_sql = 'INSERT INTO Restaurant(id, name, menuItems, kitchenDelay) VALUES(?,?,?,?)'
order_sql = 'INSERT INTO "Order" (id, customerId, items, orderStatus, totalPrice) VALUES(?,?,?,?,?)'
menu_item_sql = 'INSERT INTO MenuItem(id, name, description, calories, price) VALUES(?,?,?,?,?)'

# Define SQL statements to delete data from tables
delete_customer_sql = 'DELETE FROM Customer'
delete_restaurant_sql = 'DELETE FROM Restaurant'
delete_order_sql = 'DELETE FROM "Order"'
delete_menu_item_sql = 'DELETE FROM MenuItem'

# Execute SQL statements to delete data
cursor.execute(delete_customer_sql)
cursor.execute(delete_restaurant_sql)
cursor.execute(delete_order_sql)
cursor.execute(delete_menu_item_sql)

# Insert data into tables
cursor.executemany(customer_sql, customer_data)
cursor.executemany(restaurant_sql, restaurant_data)
cursor.executemany(order_sql, order_data)
cursor.executemany(menu_item_sql, menu_item_data)

# Commit changes and close the connection
connection.commit()
connection.close()
