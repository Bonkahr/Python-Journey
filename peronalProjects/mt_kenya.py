print("Enter 3 numbers: ")
number_1, number_2, number_3 = input("Number_1: "), input("Number_2: "), \
                            input("Number_3: ")
if number_3 == number_1 == number_2:
    print("Numbers are equal. ")
else:
    largest_number = max(number_1, number_2, number_3)
    print(f"Largest number is : {largest_number}")
