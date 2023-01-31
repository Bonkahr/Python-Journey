# when all items of one set are also in another set, the contained set is
# called subset of the containing set.

# A proper subset must contain fewer elements than its superset,
# and a proper superset must contain all and elements of subsets

animals = {'Turtle', 'Horse', 'Robin', 'Python', 'Swallow', 'Hedgehog',
           'Wren', 'Aardvark', 'Cat'}

birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'Animals is superset of birds: {animals.issuperset(birds)}')

print(f'birds is a subset of animals: {animals.issubset(birds)}')

# using operators to check

print(birds < animals)  # <= proper subset, < subset
print(animals > birds)  # > superset, >= proper superset
