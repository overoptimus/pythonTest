class C:
    def __init__(self):
        self.x = 'x-man'

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def delX(self):
        del self.x

    a = property(getX, setX, delX)
