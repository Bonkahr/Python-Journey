class Kettle(object):
    p = 10

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


if __name__ == '__main__':
    kenwood = Kettle('Kenwood', 44.4)
    print(kenwood.make)
    kenwood.price = 30
    print(kenwood.price)
    print(f'make = {kenwood.make} | price = {kenwood.price}')

    print(kenwood.p)
    kenwood.p = 5
    print(kenwood.p)
