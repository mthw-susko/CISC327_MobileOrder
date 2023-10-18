class Customer:
    '''Datastore entity that contains customer details'''

    def __init__(self, id, name, username, password, email, address, creditCardInfo):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.creditCardInfo = creditCardInfo

    def getName(self):
        return self.name

    def setName(self, name):
        if isinstance(name, str):
            self.name = name
            return True
        else:
            return False

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        if isinstance(username, str):
            self.username = username
            return True
        else:
            return False

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        if isinstance(password, str):
            self.password = password
            return True
        else:
            return False

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        if isinstance(email, str):
            self.email = email
            return True
        else:
            return False

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        if isinstance(address, str):
            self.address = address
            return True
        else:
            return False

    def getCreditCardInfo(self):
        return self.creditCardInfo

    def setCreditCardInfo(self, ccInfo):
        if isinstance(ccInfo, str):
            self.creditCardInfo = ccInfo
            return True
        else:
            return False
