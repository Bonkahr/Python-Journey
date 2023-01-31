class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        """
        Appends deposit information to the ledger
        :param amount: float or int
        :param description: a description of the deposit amount
        :return: a dict that's appended to the ledger
        """
        return self.ledger.append({'amount': amount,
                                   'description': description})

    def withdraw(self, amount, description='') -> bool:
        """
        Appends withdrawn amount and description to the ledger
        :param amount: float or int
        :param description: a description of the deposit amount
        :return: a boolean on successful/ unsuccessful transaction
        """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        """
        Returns the balance of the ledger(sum of withdrawals and deposits)
        :return: float
        """
        return sum([cash['amount'] for cash in self.ledger])

    def transfer(self, amount, account):
        """
        Transfer the amount passed to the object of Category class(account).
        :param amount: a float
        :param account: an object of Category class
        :return: boolean on successful transaction and an error if the object
        is not already instantiated
        """
        if self.check_funds(amount):
            try:
                self.withdraw(amount, f'Transfer to {account.name}')
                account.deposit(amount, f'Transfer from {self.name}')
                return True
            except AttributeError:
                return 'Transfer Error: Account does not exist'
        return False

    def check_funds(self, amount):
        """
        Checks if the available funds in the account(ledger) is enough to do
        the transaction of the amount passed
        :param amount: float or int
        :return: a boolean upon successful/ unsuccessful transaction
        """
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):
        l_name = (30 - len(self.name)) // 2
        s = f"{'*' * l_name}{self.name}{'*' * l_name}\n"
        if len(self.name) % 2 != 0:
            s = f"{'*' * l_name}{self.name}{'*' * (l_name + 1)}\n"
        for items in self.ledger:
            if len(items['description']) > 23:
                s += f"{items['description'][0:23]}" \
                     f" {format(items['amount'], '.2f').rjust(31 - len(items['description']))}\n"

            else:
                s += f"{items['description']}" \
                     f"{format(items['amount'], '.2f').rjust(30 - len(items['description']))}\n"
        return s + f"Total: {self.get_balance()}"


def create_spend_chart(categories: list) -> str:
    """
    Difficult: lots of string formatting to draw a barchart like figure,
    the class takes in all the amount in the ledger, extracts withdrawals in
    'ans' list, then tries to format the list to a barchart.
    :param categories: objects of Category class,
    :return: the barchart string
    """
    ans = []  # list consisting of withdrawals only
    for category in categories:
        totals = 0
        for items in category.ledger:
            if items['amount'] < 0:
                totals += items['amount']
        if totals < 0:
            totals *= -1
        ans.append([category.name, int(round((totals / 10), -1))])

    to_return = 'Percentage spent by category\n'

    # trying to create the barchart
    for i in range(100, -10, -10):
        to_return += f"{i:>{3}}|"
        for index, item in enumerate(ans):
            if index <= 1:
                if item[1] >= i:
                    to_return += f"  o"
                else:
                    to_return += '   '
            else:
                if item[1] >= i:
                    to_return += f"  {'' * index}o"
                else:
                    to_return += f" {' ' * index}"
        to_return += '\n'
    to_return += '-' * (6 + (len(ans) + 1) * 2) + '\n'

    # trying to add the names of the objects at the bottom of the chart
    x = 0
    for item in ans:
        if len(item[0]) > x:
            x = len(item[0])

    for i in range(x):
        for index, item in enumerate(ans):
            if index == 0:
                try:
                    to_return += f"      {item[0][i]}"
                except IndexError:
                    to_return += f"       "
            else:
                try:
                    to_return += f"  {item[0][i]}"
                except IndexError:
                    to_return += f"{'   ' * index}"

        to_return += '\n'
    return to_return
    # help a brother here


if __name__ == '__main__':
    clothing = Category('Clothing')
    grocery = Category('Grocery')
    furniture = Category('Furniture')
    new = Category('Foods')
    mad = Category('Madness')
    clothing.deposit(1000, 'Initial deposit')
    clothing.deposit(456, 'Additional Amount')
    clothing.transfer(56.89, grocery)
    clothing.withdraw(500, 'Buy shoes')
    furniture.deposit(1240, 'Purchased sofa')
    furniture.withdraw(800, 'Eating')
    furniture.transfer(790, clothing)
    grocery.deposit(346, 'News deposit')
    grocery.transfer(32.76, furniture)
    new.deposit(345, 'These foods are good but i do not like them')
    mad.deposit(5000, 'Buy madness')
    mad.withdraw(2000, 'sell madness')
    mad.transfer(1000, furniture)
    print(grocery.transfer(23, 'donkey'))
    print(clothing)
    print(grocery)
    print(create_spend_chart([clothing, grocery, furniture, mad]))
    print(furniture)
    print(new)
    print(mad)
    # print(create_spend_chart([clothing, grocery, furniture, mad]))
