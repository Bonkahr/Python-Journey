def is_number(n: str):
    user_value = n.split(" ")
    value = user_value[0]
    while True:
        if value.isdigit():
            return int(value)
        else:
            value = input("Entre a valid number")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def factorial(a):
    fact = 1
    for n in range(1, a + 1):
        fact *= n
    return fact


def users_input():
    n = is_number(input("Entre number: "))
    return n


if __name__ == '__main__':
    print("Choose your option of calculation")
    menu = ("""
    1. addition
    2. subtraction
    3. multiply
    4. factorial
    5. quit
    any other number to reprint menu
    """)
    print(menu)

    user_input = input("Entre your choice: ")
    choice = is_number(user_input)
    if choice == 1:
        print('You chose addition')
        print(addition(users_input(), users_input()))

    elif choice == 2:
        print('You chose subtraction')
        print(subtraction(users_input(), users_input()))

    elif choice == 3:
        print('You chose multiplication.')
        print(multiply(users_input(), users_input()))

    elif choice == 4:
        print('You choose factorial')
        print(factorial(users_input()))
    elif choice == 5:
        print("Bye")
    else:
        print("not valid")
