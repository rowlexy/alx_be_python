import math
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return f"The area of the Rectangle is: {self.length * self.width}"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return f"The area of the Circle is: {math.pi*(self.radius ** 2)}"
    
