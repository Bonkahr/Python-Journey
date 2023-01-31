items = set(range(21))

print(items)

# clear all items
# items.clear()

# removing single items
items.discard(10)
items.remove(11)

print(items)

# program crashes when you try to remove an item not in the set, not the case \
# with discard function
# items.remove(90)  # program crashes with KeyError
items.discard(95)
print(items)

# The pop method
# removes and returns the removed item, in no order

n = items.pop()
print(f'Popped: {n}')
