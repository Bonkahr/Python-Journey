# creating a times table
# {1:.2} formats to right aligned
with open("times_table.txt", 'w') as table:
    for number in range(2, 13):
        for numbers in range(1, 13):
            print("{1:>2} times {0} is {2}".format(numbers, number, number *
                                                   numbers), file=table)
        print("*" * 40, file=table)


with open("times_table.txt", 'r') as my_table:
    for lines in my_table:
        print(lines, end="")
