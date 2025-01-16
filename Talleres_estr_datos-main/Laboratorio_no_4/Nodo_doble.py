class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def setData(self, obj_e):
        self.data = obj_e

    def setNext(self, n):
        self.next = n

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setPrev(self, p):
        self.prev = p

    def getPrev(self):
        return self.prev

    def __str__(self):
        return str(self.data)
    
