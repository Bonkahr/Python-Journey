class Circle:
    PI = 22 / 7

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return self.PI * (self.radius ** 2)

    def get_perimeter(self):
        return self.PI * 2 * self.radius


if __name__ == '__main__':
    circle = Circle(10)
    print(circle.get_area())
    print(circle.get_perimeter())
