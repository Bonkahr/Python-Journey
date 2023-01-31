vehicles = {'dream': 'Honda 250T', 'roadstar': 'BMW R1100',
            'er5': 'Kawasaki ER5', 'fiesta': 'Ford Fiesta Ghia 1.4',
            'toyota': 'Vitz new model', 'toy': 'glider'}

# adding items to the dictionary, use keys, the item appears at the end of
# the list

# iterating over dictionaries

for key in vehicles:
    print(f'{key}, {vehicles[key]}')

# better way of iterating through the dictionary
print('*' * 40)

for key, value in vehicles.items():
    print(key, value, sep=',')

print('*' * 40)

# updating a dict
vehicles['toy'] = 'gatege'

# removing an item, if the key doesn't exist the program crashes
del vehicles['dream']

print('*' * 40)

# removing an item and return, the print function prints
# 'poppers' to console, you can also provide None as the 2nd arg, if the key
# is present the pop method return whats in the key
you_popped = vehicles.pop('roadstar', 'Poppers')
print(you_popped)

print('*' * 40)

print(vehicles)
