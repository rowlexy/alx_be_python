import math
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self, length, width):
        return f"The area of the Rectangle is: {length * width}"
class Circle(Shape):
    def area(self, radius):
        return f"The area of the Circle is: {math.pi*(radius * radius)}"
    
