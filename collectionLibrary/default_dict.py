from collections import defaultdict

# default dict is a subclass of dict python class. used to provide
# default values for the key that does'nt exist and never raises a keyError.

# the objects can be initialized using the defaultdict method passing in the data type as an arg

dict_ = defaultdict(int)

l = [1, 2, 3, 4, 4, 3, 4, 3, 4, 2, 3]

# inserting values to the dict, default value start is 0 and l being the keys.

for i in l:
    dict_[i] += 1

print(dict_)

for key, value in dict_.items():
    print(f'{key}: {value}')
