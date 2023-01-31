def factorial(n):
    """
    recursive
    :param n: number
    :return: factorial
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(800))
except (RecursionError, ZeroDivisionError):
    print("Number too large, try with less number.")
    print('Bye')
