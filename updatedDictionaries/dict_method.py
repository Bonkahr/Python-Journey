d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items, 0)
# dict is a class, calling the method `fromkeys` and created a new dict
# from the list pantry_items

# the key method, return the keys in a dict

keys = d.keys()
print(keys)

# or

for items in d.keys():   # more readable than `for items in d:`
    print(items)


# the update method

d2 = {
    7: 'lucky seven',
    10: 'ten',
    3: 'this is the new three',
}


d.update(d2)  # updates the value keys in `d` with `d2`, update preserve order

for key, value in d.items():
    print(f'{key} -> {value}')


print('=' * 60)

# ' giving our pantry items dict keys

d.update(enumerate(pantry_items))

for key, value in d.items():
    print(f'{key} -> {value}')



