import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")



class Rectangle(Shape):
    def __init__(self, length, width):
        self.legnth = length
        self.width = width
        
    def area(self):
        return f"The area of a Rectangle is: {self.legnth * self.width}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f"The area of a Circle is: {math.pi * (self.radius)**2}"



shape = Shape()
rectangle = Rectangle(5, 4)
cicle = Circle(10)
print(rectangle.area())
print(cicle.area())