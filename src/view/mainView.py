import os
import time
from model.restaurant import Restaurant
from model.menuItem import MenuItem
from view.restaurantView import RestaurantView
from controller.viewManager import ViewManager
from controller.orderManager import OrderManager


class MainView:

    def __init__(self, viewManager=ViewManager(), orderManager=OrderManager()):
        # dummy data for showing funcitonality
        self.restaurants = [Restaurant(1, "Pizza Place", [MenuItem(1, "Cheese", "Cheese Pizza with tomato sauce", 1000, 11.99), MenuItem(
            2, "Peperoni", "Peperoni Pizza with tomato sauce", 1500, 13.99)], 20)]
        self.viewManager = viewManager
        self.orderManager = orderManager
        self.name = "Main View"

    # main view method for inital main view
    def viewApp(self):
        while True:
            # display welcome text
            os.system('clear')
            print("Welcome to the Restaurant Selector!")
            print("Please choose a restaurant from the list below:")

            for i, restaurant in enumerate(self.restaurants, start=1):
                print(f"{i}. {restaurant.name}")

            try:
                choice = int(
                    input("Enter the number of your chosen restaurant (or 0 to exit): "))
                # exit the ordering program
                if choice == 0:
                    print("Exiting...")
                    time.sleep(2)
                    exit()
                # choose an available restaurant and navigate to it
                elif 1 <= choice <= len(self.restaurants):
                    print(
                        f"You have chosen: {self.restaurants[choice - 1].name}")
                    time.sleep(1)
                    self.viewManager.changeView(
                        RestaurantView(self.viewManager, self.orderManager, self.restaurants[choice - 1], self))

                else:
                    print("Invalid input. Please choose a valid option.")
                    time.sleep(1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)
