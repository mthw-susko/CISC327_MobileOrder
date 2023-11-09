import os
import time
import re
# Model imports
from model.restaurant import Restaurant
from model.menuItem import MenuItem
# Helper imports
from db.customerDbHelper import CustomerDbHelper
from db.restaurantDbHelper import RestaurantDbHelper
from view.restaurantView import RestaurantView
# Manager imports
from controller.viewManager import ViewManager
from controller.orderManager import OrderManager
# Helper imports
from helper.format import Format


class MainView:

    def __init__(self, viewManager=ViewManager(), orderManager=OrderManager()):
        customerDb = CustomerDbHelper()
        restaurantDb = RestaurantDbHelper()

        self.restaurants = restaurantDb.getRestaurants()

        # get customer data from database
        self.users = customerDb.getCustomers()
        self.loggedIn = {}
        self.viewManager = viewManager
        self.orderManager = orderManager
        self.name = "Main View"

    # main view method for inital main view

    def viewApp(self):
        while True:
            # display welcome text
            os.system('clear')
            message = "Welcome {}!".format(self.loggedIn["name"])
            Format.welcomeMessage(message)
            Format.subheaderFormat("Please choose a restaurant from the list below:")

            # display restaurants
            for i, restaurant in enumerate(self.restaurants, start=1):
                print(f"{i}. {restaurant.name}")

            try:
                # get choice input
                choice = int(
                    input("Enter the number of your chosen restaurant (or 0 to exit): "))

                # exit the ordering program
                if choice == 0:
                    print("Exiting...")
                    time.sleep(2)
                    self.loginView()

                # choose an available restaurant and navigate to it
                elif 1 <= choice <= len(self.restaurants):

                    # display which restaurant you have chosen
                    print(
                        f"You have chosen: {self.restaurants[choice - 1].name}")
                    time.sleep(1)

                    # change view
                    self.viewManager.changeView(
                        RestaurantView(self.viewManager, self.orderManager, self.restaurants[choice - 1], self, self.loggedIn))

                else:
                    print("Invalid input. Please choose a valid option.")
                    time.sleep(1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)

    def registerView(self):
        self.loggedIn = {}
        while True:
            # print a welcome message
            os.system('clear')
            Format.welcomeMessage("Welcome to the registration for the Restaurant Selector")
            Format.subheaderFormat("Please follow the instructions to create an account")

            # input new user details
            userDetails = input(
                "Enter the user details as follows, 'username:email:password' (or 0 to exit) : ")

            # exits back to login view
            if userDetails == "0":
                print("Exiting...")
                time.sleep(1)
                self.loginView()

            #making sure email input is valid
            detailsPattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not detailsPattern.match(userDetails.split(":")[0]):
                print("Invalid Email. Please try again...")
                time.sleep(1)
                self.registerView()

            # input payment info
            userPayment = input(
                "Enter the payment detials as follows 'paymentType:cardNumber:MM/YY:CVV' : ")

            # making sure input is valid
            pattern = re.compile(r'^(credit|debit):([1-9]\d{15}):(0[1-9]|1[0-2])\/(2[4-9]|3[0-9]):\d{3,4}$')
            userList = userDetails.split(":")
            if pattern.match(userPayment):

                # get user address
                userAddress = input(
                    "Enter address associated with this account: ")

                # real name of user
                name = input(
                    "Enter your real name associated with this account: ")

                # validating account inputs
                if self.validateLogin(userList[0], userList[1], userList[2]):
                    # time delay for output
                    time.sleep(1)
                    # add new customer to database
                    customerDb = CustomerDbHelper()
                    customerDb.addCustomer(name,
                                           userList[0], userList[2], userList[1], userAddress, userPayment.split(":"))

                    # update list of users
                    self.users = customerDb.getCustomers()

                    # add new logged in user
                    self.loggedIn = {
                        "username": userList[0], "creditCardInfo": userPayment.split(":"), "id": customerDb.getCustomerId(userList[0]), "name": name}

                    # go to main view of app
                    self.viewApp()

            else:
                print("Invalid Input. Please try again...")
                time.sleep(1)

    def loginView(self):
        self.loggedIn = {}
        while True:
            os.system('clear')
            Format.welcomeMessage("Welcome to the Restaurant Selector!")
            Format.subheaderFormat("Please enter your username followed by your password to sign in (press Enter to register or 0 to exit)")

            try:
                # get username input
                username = input(
                    "Enter username (press Enter to create an account or 0 to exit): ")

                # exit program
                if username == "0":
                    print("Exiting...")
                    time.sleep(1)
                    exit()

                # go to register view
                if len(username) == 0:
                    self.registerView()

                password = input("Enter password: ")

                # validate username and password are with a valid account
                if self.tryLogin(username, password):
                    time.sleep(1)
                    customerDb = CustomerDbHelper()
                    creditCardInfo = customerDb.getCreditCardInfo(username)
                    userId = customerDb.getCustomerId(username)
                    name = customerDb.getCustomerName(username)
                    self.loggedIn = {
                        "username": username, "creditCardInfo": creditCardInfo, "id": userId, "name": name}

                    self.viewApp()

                # time delay for error message
                time.sleep(1)

            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)

    # validate login info
    def tryLogin(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Successful login")
            return True

        elif username not in self.users:
            print("Username does not exist")
            return False
        else:
            print("Incorrect Password")
            return False

    def validateLogin(self, username, email, password):
        if len(username) != 0:
            if len(email) != 0:
                if len(password) != 0:
                    # verify the username isn't already taken
                    if username not in self.users:
                        emailPattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                        uppercase_regex = r'[A-Z]'
                        lowercase_regex = r'[a-z]'
                        number_regex = r'[0-9]'

                        # verify the email is good
                        if re.match(emailPattern, email):
                            # verify passowrd is good
                            if re.search(uppercase_regex, password):
                                if re.search(lowercase_regex, password):
                                    if re.search(number_regex, password):
                                        print("User Registered Successfully")
                                        return True
                                    else:
                                        print(
                                            "Password must contain at least one number")
                                else:
                                    print(
                                        "Password must contain at least one lowercase letter")
                            else:
                                print(
                                    "Password must contain at least one uppercase letter")
                        else:
                            print("Invalid email entered")
                    else:
                        print("Username has been taken")
                else:
                    print("Missing password")
            else:
                print("Missing email")
        else:
            print("Missing username")

        return False
