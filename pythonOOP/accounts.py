import datetime
import pytz


class Accounts:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.transactions_list = [(Accounts._current_time().astimezone(),
                                   self.__balance)]
        print(f'Account created for {self._name}.')

    def deposit(self, amount):
        # if len(self.transactions_list) == 0 and self.balance > 0:
        #     self.transactions_list.append((Accounts._current_time(),
        #                                    self.balance))
        if amount > 0:
            self.__balance += amount

            # Calling static method use the class name
            self.transactions_list.append((Accounts._current_time(), amount))
        else:
            print('Transaction can not be completed')

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f'Withdrawal of ksh{amount} successful, balance is '
                  f'ksh{self.__balance}')
            self.transactions_list.append((Accounts._current_time(), -amount))

        else:
            print(f'You can not withdraw amount ksh{amount}, your balance is '
                  f'ksh{self.__balance}')

    def show_balance(self):
        print(f'Balance is ksh{self.__balance}')

    def show_transactions(self):
        for date, amount in self.transactions_list:
            if amount > 0:
                tran_type = 'Deposited'
            else:
                tran_type = 'Withdrawn'
                amount *= -1
            print(f'ksh{amount} {tran_type} on  {date.astimezone()} ')


if __name__ == '__main__':
    john = Accounts('John', 0)
    john.deposit(2500)
    john.deposit(1200)
    john.withdraw(1500)
    john.show_transactions()

    print('*' * 80)

    steph = Accounts('Steph', 500)
    steph.deposit(1000)
    steph.deposit(1000)
    steph.withdraw(800)
    steph.show_transactions()
    steph.show_balance()
