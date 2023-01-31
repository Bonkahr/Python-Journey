# my_file = open("sample.txt", 'r')
# for lines in my_file:
#     if "ware" in lines.capitalize():
#         print(lines, end="")
# my_file.close()

# the following code doesnt require the close function
#
# with open("sample.txt", "r") as my_file:
#     for lines in my_file:
#         print(lines, end="")
#
# making the file a list

# with open("sample.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()   # returns false after reading all files

with open("sample.txt", "r") as file:
    lines = file.readlines()    # make the file a list
print(lines)

for line in lines[::-1]:
    print(line, end="")
