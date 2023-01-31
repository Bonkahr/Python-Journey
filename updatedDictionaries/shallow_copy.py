import copy

animals = {
    'lion': ['scary', 'big', 'cat'],
    'elephant': ['big', 'grey', 'wrinkled'],
    'teddy': ['cuddly', 'stuffed'],
}


if __name__ == '__main__':

    # perform a shallow copy
    # things = animals.copy()  # creates a new copy of the dict

    # perform a deep copy
    things = copy.deepcopy(animals)

    print(animals['teddy'])
    print(things['teddy'])

    print()

    things['teddy'].append('toy')
    print(things['teddy'])
    print(animals['teddy'])
