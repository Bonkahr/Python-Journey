def factorial(number: int) -> int:
    """
    Get a number from the stdIN and calculate its factorial
    :param number: stdIN input
    :return: factorial
    """
    if number == 0:
        return 1
    else:
        number_factorial = 1
        for integer in range(1, number):
            number_factorial *= integer+1

        return number_factorial


for n in range(0, 35):
    print(n, factorial(n))

