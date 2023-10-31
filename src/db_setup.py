import sqlite3

connection = sqlite3.connect('dataBase.db')

# insert data into table
restaurant_data = [
    (1, "MacDonalds", "[BigMac, MacChicken, CheeseBurger]", 0),
    (2, "KFC", "[ChickenTenders, SpicyChicken, NonSpicyChicken]", 1)
]

# test insertion setup
connection.executemany('INSERT INTO Restaurant(id, name, menuItems, kitchenDelay) VALUES(?,?,?,?)', restaurant_data)

# write data to the file
connection.commit()

# close the database connection
connection.close()