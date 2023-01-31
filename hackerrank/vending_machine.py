class VendingMachine:

    def __init__(self, no_items: int, price: float) -> None:
        self.no_items = no_items
        self.price = price

    def buy(self, items: int, money: float) -> float:
        if items > self.no_items:
            raise ValueError('Not enough items in the machine')
        required_money = items * self.price
        if money < required_money:
            raise ValueError('Not enough coins')
        self.no_items -= items
        return money - required_money

    def __str__(self) -> str:
        return f'Available items: {self.no_items}\nCost: {self.price}'


if __name__ == '__main__':
    vendor = VendingMachine(10, 2)
    print(vendor.buy(1, 5))
    # print(vendor.buy(10, 100))
    print(vendor.buy(7, 100))
    # print(vendor.buy(2, 3))
    print(vendor)
