# x = 1
# y = 1
# z = 1
#
# x_val = range(x + 1)
# y_val = range(y + 1)
# z_val = range(z + 1)


my_set = {1, 3, 5, 6, 6, 2}
print(sorted(set(my_set))[-2])


# set algorythm


def my_set(items):
    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
    return new_items


print(my_set([1, 1, 1, 1, 3, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 3, 2]))

import random


def generate(amount):
    numbers = []
    for i in range(amount):
        numbers.append(random.randint(0, 9))
    return numbers


print(generate(1000))
