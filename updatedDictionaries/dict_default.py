from contents import pantry

# the setdefault method adds the key to the dictionary if it doesnt exist
chicken_quantity = pantry.setdefault('chicken', 0)
chicks = pantry.setdefault('chick', 0)  # chick is added to the dict

for key, quantity in sorted(pantry.items()):
    print(f'{key} -> {quantity}')

# the get method, check the existence of the key in the dict and returns if
# it exists, otherwise the default value given is returned, any data
# structure can be used as default

print('=' * 60)

kitchen = pantry.get('chicken', 'Available')
kitchen1 = pantry.get('chicks', 'Not Available')  # not added to the dict

print(f'{kitchen} -> {kitchen1}')

print('=' * 60)
for key, quantity in sorted(pantry.items()):
    print(f'{key} -> {quantity}')
