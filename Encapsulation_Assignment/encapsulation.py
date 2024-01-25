

class Protected:
    def __init__(self):
        self.__privateVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()
obj.getPrivate()#gets the variable set in the class
obj.setPrivate(47)#assigns a new private variable
obj.getPrivate()#gets the new private variable assigned


