import os
import time
from view.orderView import OrderView


class RestaurantView:
    def __init__(self, viewManager, orderManager, restaurant, lastView):
        self.restaurant = restaurant
        self.orderManager = orderManager
        self.viewManager = viewManager
        self.lastView = lastView
        self.name = "Restaurant View"

    def viewApp(self):
        print(f"Welcome to {self.restaurant.name}!")

        # restaurant has no avaialable menu items
        if not self.restaurant.menuItems:
            print("There are no available menu items for this restaurant...")
            while True:
                try:
                    choice = int(input("Enter any number to exit: "))
                    # if an integer is entered, then exit back to the main view
                    if isinstance(choice, int):
                        self.viewManager.changeView(self.lastView)
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # restaurant has menu items
        else:
            # get user input
            while True:
                # disaply avaialable menu items
                os.system('clear')
                for i, item in enumerate(self.restaurant.menuItems, start=1):
                    print(
                        f"{i}. ${item.price} calories: {item.calories} {item.name}: {item.description} ")
                try:
                    choice = int(input(
                        "Please add a menu item to cart by entering its number, check cart by entering 0 (or press -1 or exit): "))
                    # exits back to main view
                    if choice == -1:
                        print("Exiting...")
                        time.sleep(2)
                        self.viewManager.changeView(self.lastView)
                        break
                    # adds chosen menu item to the cart
                    elif 1 <= choice <= len(self.restaurant.menuItems):
                        print(
                            f"You have added: {self.restaurant.menuItems[choice - 1].name}")
                        self.orderManager.addToCart(
                            self.restaurant.menuItems[choice - 1])
                        time.sleep(1)
                    # goes to view the current order view
                    elif choice == 0:
                        print("Going to Order View...")
                        time.sleep(2)
                        self.viewManager.changeView(
                            OrderView(self.viewManager, self.orderManager, self))
                        break
                    # catch case if invalid input is given
                    else:
                        print("Invalid input. Please choose a valid option.")
                        time.sleep(1)
                # catch case if invalid input is given
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(1)
