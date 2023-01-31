import sys


def get_int():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print('That is not an integer')

        # exceptions raised by os ctrl+D
        except EOFError:
            sys.exit(1)

        # executed no matter the condition
        finally:
            print("Thank you")


try:
    print(get_int() / get_int())

except ZeroDivisionError:
    print("Cant divide by zero")
    sys.exit(2)

    # only performs when the try block is executed, no exceptions
else:
    print('successful')
