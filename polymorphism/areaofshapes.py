class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print("Area:", shape.area())

s1 = Rectangle(5, 3)
s2 = Circle(4)
s3 = Triangle(4, 6)

print_area(s1)
print_area(s2)
print_area(s3)