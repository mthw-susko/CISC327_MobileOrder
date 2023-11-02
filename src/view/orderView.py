import os
import time
from controller.paymentManager import PaymentManager
from db.orderDbHelper import OrderDbHelper


class OrderView:
    def __init__(self, viewManager, orderManager, lastView, user):
        self.viewManager = viewManager
        self.orderManager = orderManager
        self.lastView = lastView
        self.loggedIn = user
        self.name = "Order View"

    # Main view method for orders
    def viewApp(self):
        # get user input
        while True:
            os.system('clear')

            # displays all the items in the cart
            if not self.orderManager.cart:
                print("Your cart is empty.")
                choice = input("Press Enter to exit...")

                # if an integer is entered then exit back to the restaruant view
                if len(choice) == 0:
                    print("Exiting...")
                    time.sleep(1)
                    self.viewManager.changeView(self.lastView)
                    break
            else:
                # display items in current order
                print("Your current order...")
                for i, item in enumerate(self.orderManager.cart, start=1):
                    print(
                        f"{i}. ${item.price} calories: {item.calories} {item.name}: {item.description} ")

                # print total price
                print(
                    f"The total price is: ${self.orderManager.calculateTotalOrderPrice()}\n")

                try:
                    # get user input for choice
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
                        time.sleep(1)

                    # check out and submit order
                    elif choice == 0:
                        print("Checking Out...")
                        time.sleep(1)
                        finished = self.orderManager.submitOrder()
                        # order had been successfully submitted
                        if finished:
                            print("Order Submitted!")
                            time.sleep(1)

                            # validate payment info
                            paymentProcessed = PaymentManager().processPayment(
                                self.loggedIn["creditCardInfo"])

                            # payment processed correctly and cart emptied
                            if paymentProcessed:
                                print("Payment Processed!")
                                time.sleep(1)

                                orderDb = OrderDbHelper()

                                # if no delay, then order is delivered
                                if self.lastView.restaurant.kitchenDelay == 0:
                                    print("Order Delivered!")
                                    orderDb.addOrder(
                                        self.loggedIn["id"], self.orderManager.cart, "Delivered", self.orderManager.calculateTotalOrderPrice())
                                    time.sleep(1)

                                else:
                                    print("Delivery on its way!")
                                    time.sleep(1)
                                    orderDb.addOrder(
                                        self.loggedIn["id"], self.orderManager.cart, "Delivering", self.orderManager.calculateTotalOrderPrice())
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
                        time.sleep(1)
                # catch case if invalid input is given
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(1)
