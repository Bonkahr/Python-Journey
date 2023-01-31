import csv

# with open('sample4.csv', 'r') as csv_sample:
#     reader = csv.reader(csv_sample)
#     for row in reader:
#         print(row)

data_list = []
with open('sample_csv.csv', 'r') as csv_sample:
    reader = csv.reader(csv_sample)

    for row in reader:
        data_list.append(row)

data_keys = [data_list[0][0].split(';')][0]
# print(data_keys)
data_items = data_list[1:][0]
print(data_items)

# data_dict = {}
#
# for n, key in enumerate(data_keys, start=0):
#     data_dict[key] = ' '
#     for data in data_items[n][0].split(';'):
#         print(len(data))
#         # print(data)
#         data_dict[key] += data[n]
#
# print(data_dict)
