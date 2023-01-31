class User(object):

    def __init__(self, name: str, balance: int, checking_account=True):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError(f"You can't withdraw "
                             f"{amount}, your balance is {self.balance}")
        self.balance -= amount
        return f'Withdraw of amount {amount} successful '\
               f'from account {self.name} balance is {self.balance}.'

    def transfer(self, user, amount):
        if user.checking_account:
            user.withdraw(amount)
            self.add_cash(amount)
            return f'{amount} transfer from your account to ' \
                   f'{self.name} successful, your balance is ' \
                   f'{int(user.balance)}.'

        raise ValueError(f"{user.name} doesn't allow checking balance")

    def add_cash(self, amount):
        self.balance += amount
        return f'{amount} added to your account, your balance is now ' \
               f'{int(self.balance)}.'


if __name__ == '__main__':
    Jeff = User('Jeff', 70000, True)
    Joe = User('Joe', 347867, True)
    
    print(Jeff.withdraw(22345.67))
    print(Joe.transfer(Jeff, 509))
    print(Joe.balance)
    print(Jeff.transfer(Joe, 6000))
    print(Jeff.balance)
    print(f'Joe -> {Joe.balance}')
    print(Jeff.add_cash(20))
    print(Joe.transfer(Jeff, 50.0))
    print(Joe.withdraw(60000))
    print(Jeff.balance)
    print(Joe.balance)
