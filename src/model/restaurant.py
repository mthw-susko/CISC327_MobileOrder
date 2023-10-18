class Restaurant:
    '''Datastore entity that contains restaurant details'''

    def __init__(self, id, name, menuItems, kitchenDelay):
        self.id = id
        self.name = name
        self.menuItems = menuItems
        self.kitchenDelay = kitchenDelay

    def getRestaurantName(self):
        return self.name

    def setRestaurantName(self, name):
        if isinstance(name, str):
            self.name = name
            return True
        else:
            return False

    def getMenuItems(self):
        return self.menuItems

    def setMenuItems(self, items):
        if isinstance(items, list):
            self.menuItems = items
            return True
        else:
            return False

    def increaseDelay(self):
        self.kitchenDelay += 1
        return self.kitchenDelay

    def decreaseDelay(self):
        self.kitchenDelay -= 1
        return self.kitchenDelay
