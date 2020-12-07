# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod               # ye method bolti hai ki jo function isme defined hai vo compulsarily har class me
    # implement hona chahiye because ye abstact  base class method hai
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# ABC ek module hai
# apan abstract base class ke object nahi bana sakte like ye try karlo
# tryobj=Shape()