from data import basic_plants_list, plants_list

print(plants_list[0])

# for plant in plants_list:
#     print(plant[0])

# same code with .notation

for plant in plants_list:
    print(plant.name)

print()

example = plants_list[0]
print(example)

example = example._replace(lifecycle='Annual')

print(example)
