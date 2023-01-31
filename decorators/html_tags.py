from functools import wraps


def tagged(func):
    """
    Make HTML tags
    :param func: function
    :return: str
    """

    @wraps(func)
    def wrapper():
        """
        Wrapper function
        :return: str
        """
        return f'<p><{func()[1]}>{func()[0]}</{func()[1]}></p>'

    return wrapper


@tagged
def to_tag():
    return 'hello', 'stronger'


if __name__ == '__main__':
    print(to_tag())
