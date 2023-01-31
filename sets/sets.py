farm_animals = {"sheep", "cow", "hen"}

for animal in farm_animals:
    print(animal)
    print("*" * 10)

print("=" * 40)


wild_animals = {"Lion", "tiger", "panther", "elephant", "hyena"}

for animal in wild_animals:
    print(animal)
    print("~" * 10)

print("=" * 40)

farm_animals.add("dog")
wild_animals.add("antelope")

print(farm_animals)
print(wild_animals)

# creating empty set
empty_set = set()
empty_set.add("kenya")
print(empty_set)
