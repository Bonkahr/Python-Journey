# A decorator is a callable that takes another function as an argument,
# extending the behaviour of that function without explicitly modifying that
# function

def my_decorator(func):
    """
    Decorator function
    :param func:
    :return: int
    """

    def wrapper():
        """

        :return:
        """
        return 'F-I-B-O-N-A-C-C-I'

    return wrapper


@my_decorator
def p_fib():
    """
    Return Fibonacci
    :return: int
    """
    return 'Fibonacci'


if __name__ == '__main__':
    # print(p_fib())
    # pfib = my_decorator(p_fib)
    # print(pfib())
    print(p_fib())
