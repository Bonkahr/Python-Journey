import array

list_1 = list(range(10))
a = array.array('i', list_1)  # -> i indicating the type of data
list_str = [str(i) for i in list_1]
print(list_str)
b = array.array('u', list_str)
print(a)
print(b)
