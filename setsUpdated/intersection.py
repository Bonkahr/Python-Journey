from primes_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
squares = set(squares_generator(100))
print(primes)
print(squares)

print('=' * 90)
# intersection returns whats in two sets
print(evens.intersection(odds))
print('=' * 90)
print(odds.intersection(squares))
print(evens.intersection(squares))


# intersecting more that two sets

farm_animals = {'sheep', 'goat', 'dog', 'cow', 'cat', 'horse'}
wild_animals = {'lion', 'goat', 'elephant', 'giraffe', 'panther', 'horse'}
potential_rides = {'donkey', 'horse', 'camel'}

# using the & operator -> only horse appears in all sets

intersect = farm_animals & wild_animals & potential_rides
print(intersect)

print('=' * 90)
# using the intersect method

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)


text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_set = set([word for word in text.split()])

preps_used = prepositions.intersection(text_set)
print(text_set)
print(preps_used)
