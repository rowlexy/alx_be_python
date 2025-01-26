import math
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        return f"The area of the Rectangle is: {length * width}"
class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        return f"The area of the Circle is: {math.pi*(self.radius ** 2)}"
    
