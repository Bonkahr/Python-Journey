generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '3', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7',
]

values = "".join(generated_list)
print("after join",  values)

values_list = values.split()
print("after split", values_list)

generated_integers = []


for items in range(len(values_list)):
    generated_integers.append(int(values_list[items]))

print(generated_integers)
