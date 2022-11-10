#CarInventoryNode.py

from pyexpat import model
from Car import *
class CarInventoryNode():
    def __init__(self, car):
        self.cars = [car]
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.left = None
        self.right = None
        self.parent = None
        
    def getMake(self):
        return self.make
        
    def getModel(self):
        return self.model
        
    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
            
    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)
    
    def replaceNodeData(self, make, model, cars, lc, rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        if self.make < rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model > rhs.model:
                return True
            if self.model < rhs.model:
                return False     
            if self.model == rhs.model:
                return False
    
    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        if self.make > rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model < rhs.model:
                return True
            if self.model > rhs.model:
                return False     
            if self.model == rhs.model:
                return False

    def __eq__(self, rhs):
            if self is None or rhs is None:
                return False
            else:
                if (self.make == rhs.make) and (self.model == rhs.model):
                    return True

            
    def __str__(self):
        result = ""
        for car in self.cars:
            result += str(car) + "\n"
        return result

    def spliceOut(self):
        if self.isLeaf():
            if not self.parent:
                return
            elif self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None             
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
