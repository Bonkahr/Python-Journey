fruit = {"orange": 'a sweet, orange, citrus fruit',
         "apple": 'good for making cider',
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lime"])
print(fruit["apple"])

fruit["pear"] = "an odd shaped fruit"  # appending items
print(fruit)

del fruit["lime"]
print(fruit)
# fruit.clear()  # clear items

# ordered dict
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))

for f in sorted(fruit):
    print(f + " -> " + fruit[f])

for val in fruit.values():
    print(val)
