from random import random

class Leaf:
    UID = None
    name = None
    mother = None
    father = None

    def __init__(self, leafName):
        self.name = leafName
        self.UID = round(random() * 100)

    def printMyself(self):
        print(self.name)
        print('UID: ' + str(self.UID))

