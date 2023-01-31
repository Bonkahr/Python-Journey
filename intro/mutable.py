shopping_list = ["lemon",
                 "mangoes",
                 "oranges",
                 "sweet potatoes",
                 ]

another_shopping = shopping_list

print(id(shopping_list))
print(shopping_list)
print(id(another_shopping))
print(another_shopping)

shopping_list += ["pawpaw"]

print(id(shopping_list))
print(shopping_list)
print(id(another_shopping))
print(another_shopping)


if "pawpaw" in shopping_list:
    print()
