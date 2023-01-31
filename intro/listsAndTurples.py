shopping_list = ["milk", "pasta", "spam", "bread", "rice"]

item_to_find = "spam"

for item in shopping_list:
    if item == item_to_find:
        print(shopping_list.index(item))
        break

for i in range(0, 100, 7):
    if i > 0 and i % 11 == 0:
        print(i)
        break

print("*************************************")
for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
