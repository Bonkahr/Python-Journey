import timeit
import functools


def calc_values(x, y: int) -> int:
    return x + y


number = '123456789'
numbers = [2, 3, 5, 8, 13]
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)


def reducing(x, y):
    return int(x) + int(y)


reduced_val = functools.reduce(reducing, number)
print(reduced_val)

