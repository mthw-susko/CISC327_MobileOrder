class OrderManager:
    def __init__(self):
        # Attributes
        self.cart = []
        self.is_order_submitted = False

    def submitOrder(self):
        if self.cart and not self.is_order_submitted:
            # Process the order, e.g., send it to the backend
            self.is_order_submitted = True
            return True
        else:
            return False

    def cancelOrder(self):
        if self.is_order_submitted:
            # Cancel the order, e.g., revert the order submission
            self.is_order_submitted = False
            self.cart = []
            return True
        else:
            return False

    def calculateTotalOrderPrice(self):
        # Logic to calculate total order price
        total_price = sum(item.price for item in self.cart)
        return float(total_price)

    def addToCart(self, item):
        # Add to array of items
        self.cart.append(item)

    def removeFromCart(self, item):
        # Delete from array of items
        if item in self.cart:
            self.cart.remove(item)
