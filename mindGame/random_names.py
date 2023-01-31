from random_words import RandomNicknames

names = RandomNicknames()
boys = names.random_nicks(gender='m', letter='s', count=30)
girls = names.random_nicks(gender='f', letter='s', count=30)

with open('random_names.txt', 'w') as random_names:
    random_names.write('Boys Names Starting with \'S\':\n')
    for n, boy in enumerate(boys, start=1):
        random_names.write(f"{n:>2}. {boy}\n")
    random_names.write('\n')
    random_names.write('Girls name starting with \'s\':\n')
    for n, girl in enumerate(girls,start=1):
        random_names.write(f"{n:>2}. {girl}\n")

