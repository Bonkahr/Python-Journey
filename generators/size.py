import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


big_range = my_range(5)

print(f'big_range is {sys.getsizeof(big_range)} bytes')

big_list = []
for items in big_range:
    big_list.append(items)

print(f'big_list is {sys.getsizeof(big_list)} bytes')

print(big_list)
print(big_range)
