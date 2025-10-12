import math

class Shape:
    def area(self):
        # Base method meant to be overridden by subclasses
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return math.pi * (self.radius ** 2)
