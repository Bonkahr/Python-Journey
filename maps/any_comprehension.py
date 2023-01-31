from data import people, basic_plants_list, plants_list, plants_dict

if bool(people) and all([person[1] for person in people]):
    print('Sending email')
else:
    print('Edit list of recipient')


if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print('This pack contains grass')
else:
    print('No grasses in the pack')

print('x' * 60)


# check in the dictionary

if any([plant.plant_type == 'Gras' for plant in plants_dict.values()]):
    print('Its here')
else:
    print('None')

# Using keys

if any(plants_dict[key].plant_type == 'Grass' for key in plants_dict):
    print('Its here')
else:
    print('None')

