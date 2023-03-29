from collections import Counter

# The counter can be called in with a sequence of items(list), with
# a dictionary containing keys and counts or with keyword arguments
# mapping string names to counts.
# Mostly usiful in lists.

# lists -> dict
my_list = ['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']
print(Counter(my_list))  # {'B': 5, 'A': 3, 'C': 2}
