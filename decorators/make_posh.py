from functools import wraps


def make_posh(func):
    """
    Decorator Function
    :param func: function
    :return: str
    """

    @wraps(func)
    def wrapper():
        """
        Wrapper function
        :return: str
        """
        print('+--------+')
        print('|        |')
        print(func())
        print('|        |')
        print('+--------+')

    return wrapper


@make_posh
def posh():
    return 'Am  Poshed'


if __name__ == '__main__':
    print(posh())
