def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:....{}, {}".format(p1, p2))
    print("var-positional (*args):.......{}".format(args))
    print("keyword:......................{}".format(k))
    print("var-keyword:..................{}".format(kwargs))


func(1, 2, 3, 4, 5, 7, 8, k=9, key1=6, key2=10)


def sum_numbers(*args: float) -> float:
    """
    Gets a couple of numbers from the stdIN,
    unpack then to a tuple and iterate to get
    the sum.

    :param args: tuple of integers or float
    :return: float or integer sum
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
