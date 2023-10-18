class Order:
    '''Datastore entity that contains customer order'''

    def __init__(self, id, customerId, Items, orderStatus, totalPrice):
        self.id = id
        self.customerId = customerId
        self.Items = Items
        self.orderStatus = orderStatus
        self.totalPrice = totalPrice

    def getCustomerId(self):
        return self.customerId

    def setCustomerId(self, id):
        if isinstance(id, int):
            self.customerId = id
            return True
        else:
            return False

    def getOrderItems(self):
        return self.Items

    def setOrderItems(self, items):
        if isinstance(items, list):
            self.Items = items
            return True
        else:
            return False

    def getOrderStatus(self):
        return self.orderStatus

    def setOrderStatus(self, status):
        if isinstance(status, str):
            self.orderStatus = status
            return True
        else:
            return False

    def getTotalPrice(self):
        return self.totalPrice

    def setTotalPrice(self, price):
        if isinstance(price, int):
            self.totalPrice = price
            return True
        else:
            return False
