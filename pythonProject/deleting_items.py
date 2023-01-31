data = [600, 101, 2, 10, 435, 98, 540, 198, 54, 187, 120, 43, 230]

min_valid = 100
max_valid = 200

# for index in range(len(data)-1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         #print(index, data)
#         del data[index]
# print(data)

# reverse iterating through a list
top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)


