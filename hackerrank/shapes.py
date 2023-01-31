from math import pi


class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


if __name__ == '__main__':
    rec = Rectangle(12, 10)
    print(rec.area())

    cir = Circle(12)
    print(cir.area())
