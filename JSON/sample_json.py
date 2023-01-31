import json

# json doesn't support tuples, it will always be serialized to list(python),
# 'or json array

languages = [
    ['ABC', 1987],
    ['Algo 68', 1968],
    ['APL', 1973],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# with open('test.json', 'w', encoding='utf-8') as testfile:
#     json.dump(languages, testfile)

# reading the data from the json file created above (commented lines)
with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])
