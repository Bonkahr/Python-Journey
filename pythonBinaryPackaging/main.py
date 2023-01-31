import math


class Calculator:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self):
        return self.y + self.x

    def power(self):
        return math.pow(self.x, self.y)


if __name__ == '__main__':
    print("""
    ************************************************************************
    * This is a terminal calculator, you will enter two numbers and choose *
    * the arithmetic you want to perform.                                  *
    ************************************************************************
    """)

    choice = input("What do you want to perform:\n\t1. Addition\n\t2. "
                   "Power\n=> ")
    while True:
        try:
            int(choice)
            if int(choice) != 1 and int(choice) != 2:
                print(f"{choice} - is not in our list.")
                cont = input("Do you want to try again? y/N => ")
                if cont.casefold() == 'y':
                    choice = input("Enter your choice, 1 or 2: ")
            break
        except ValueError:
            choice = input("Enter a valid choice, 1 or 2: ")

    if choice.isalpha():
        print("Sorry you can't be helped.")

    elif int(choice) == 1:
        print("Enter the number to do addition: ")
        number_1 = input("Enter the first number: ")
        number_2 = input("Enter the second number: ")

        while True:
            try:
                number_1 = int(number_1)
                number_2 = int(number_2)
                break
            except ValueError:
                print("Enter valid numbers!")
                number_1 = input("First number: ")
                number_2 = input("Second number: ")

        print(f"{number_1} + {number_2} = "
              f"{Calculator(number_1, number_2).add()}")
    elif int(choice) == 2:
        print("Enter the numbers to do find its power: ")
        number_1 = input("Enter the first number: ")
        number_2 = input("Enter the second number: ")

        while True:
            try:
                number_1 = int(number_1)
                number_2 = int(number_2)
                break
            except ValueError:
                print("Enter valid numbers!")
                number_1 = input("First number: ")
                number_2 = input("Second number: ")

        print(
            f"{number_1} to power {number_2} ="
            f" {Calculator(number_1, number_2).power()}")
    else:
        print(f"{choice}? -> You never follow instructions.")
