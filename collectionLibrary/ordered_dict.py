from collections import OrderedDict
import string
import random


# The Oedered gives keeps the dict ans the keys and values were entered. Similar to Python >= 3.8

# normal python dict
my_dict: dict = {}

for x in range(10):
    my_dict[string.ascii_letters[random.randint(
        0, 25)]] = random.randint(0, 99)

my_dict_ord = OrderedDict()

for x in range(10):
    my_dict_ord[string.ascii_letters[random.randint(
        0, 25)]] = random.randint(0, 99)

# pythin 3.8 -> dicts are ordered as they were entered.
print(f'unordered dict: {my_dict}')
print(f'orderd dict {my_dict_ord}')

for key, value in my_dict_ord.items():
    print(f'{key}: {value}')
