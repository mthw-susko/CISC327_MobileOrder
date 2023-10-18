class MenuItem:
    '''Datastore entity that contains info for a food item on a menu'''

    def __init__(self, id, name, description, calories, price):
        self.id = id
        self.name = name
        self.description = description
        self.calories = calories
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        if isinstance(name, str):
            self.name = name
            return True
        else:
            return False

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        if isinstance(price, int):
            self.price = price
            return True
        else:
            return False

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        if isinstance(description, str):
            self.description = description
            return True
        else:
            return False

    def getCalories(self):
        return self.calories

    def setCalories(self, calories):
        if isinstance(calories, int):
            self.calories = calories
            return True
        else:
            return False
