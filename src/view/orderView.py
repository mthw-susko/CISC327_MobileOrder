import os
import time
from controller.paymentManager import PaymentManager


class OrderView:
    def __init__(self, viewManager, orderManager, lastView):
        self.viewManager = viewManager
        self.orderManager = orderManager
        self.lastView = lastView
        self.name = "Order View"

    def viewApp(self):
        # get user input
        while True:
            os.system('clear')
            # displays all the items in the cart
            if not self.orderManager.cart:
                print("Your cart is empty.")
                try:
                    choice = int(input("Enter any number to exit: "))
                    # if an integer is entered then exit back to the restaruant view
                    if isinstance(choice, int):
                        print("Exiting...")
                        time.sleep(2)
                        self.viewManager.changeView(self.lastView)
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(2)
            else:
                print("Your current order...")
                for i, item in enumerate(self.orderManager.cart, start=1):
                    print(
                        f"{i}. ${item.price} calories: {item.calories} {item.name}: {item.description} ")

                print(
                    f"The total price is: ${self.orderManager.calculateTotalOrderPrice()}\n")
                try:
                    choice = int(input(
                        "Enter the number of the item to remove it. Or Enter 0 to submit your order(or -1 to exit): "))
                    # exit back to restaurant view
                    if choice == -1:
                        print("Exiting...")
                        time.sleep(2)
                        self.viewManager.changeView(self.lastView)
                        break
                    # remove chosen item from cart
                    elif 1 <= choice <= len(self.orderManager.cart):
                        print(
                            f"You have removed: {self.orderManager.cart[choice - 1].name}")
                        self.orderManager.removeFromCart(
                            self.orderManager.cart[choice - 1])
                        time.sleep(2)
                    # check out and submit order
                    elif choice == 0:
                        print("Checking Out...")
                        time.sleep(2)
                        finished = self.orderManager.submitOrder()
                        # order had been successfully submitted
                        if finished:
                            print("Order Submitted!")
                            # TODO: add real payment processing info
                            time.sleep(2)
                            paymentProcessed = PaymentManager().processPayment(True)
                            # payment processed correctly and cart emptied
                            if paymentProcessed:
                                time.sleep(2)
                                print("Payment Processed!")
                                self.orderManager.cart = []
                            # error processing payment
                            else:
                                print("Error Processing Payment...")
                        # order not successfully submitted
                        else:
                            print("Error Submitting Order...")
                    # catch case if invalid input is given
                    else:
                        print("Invalid input. Please choose a valid option.")
                        time.sleep(2)
                # catch case if invalid input is given
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(2)
