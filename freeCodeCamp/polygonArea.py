class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        pic = ''
        for i in range(self.height):
            pic += '*' * self.width + '\n'
        return 'Too big for picture.' \
            if self.height >= 50 or self.width >= 50 else pic

    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, width):
        super().__init__(width, width)

    def set_height(self, height):
        super().__init__(height, height)

    def set_side(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_area())
    print(rect.get_picture())
    print(rect.get_perimeter())
    print(rect)
    rect.set_height(6)
    print(rect.get_picture())

    sq = Square(4)
    print(sq.get_area())
    sq.set_side(4)
    print(sq)
    print(sq.get_picture())
    print(sq.get_diagonal())
    print(sq)
    sq.set_side(60)
    sq.set_height(56)
    print(sq.get_picture())
    print(sq.get_area())
    print(sq)

    print("*" * 80)
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
