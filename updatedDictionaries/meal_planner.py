from contents import pantry, recipes

# comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


def add_shopping_items(data: dict, item: str, amounts: int) -> None:
    # if item in data:
    #     data[item] += amounts
    # else:
    #     data[item] = amounts

    # better way to represent the code above
    # the code sets a default value of 0, if the data doesn't exist, otherwise
    # it adds the amount
    data[item] = data.setdefault(item, 0) + amounts


items_to_buy = {}

while True:
    # Display a menu of the recipes we know how to cook
    print('Please choose Recipe')
    print('-' * 80)
    for key, value in display_dict.items():
        print(f'{key} -> {value}')
    print('0 -> exit')

    choice = input('What do you want to cook: ')

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f'You have selected {selected_item}')
        print('Checking ingredients......')
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity in ingredients.items():
            # if no item in the dict, '0' is returned as default, and program
            # doesnt crash
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f'{food_item} is available')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                add_shopping_items(items_to_buy, food_item, quantity_to_buy)

print("Need to buy: ")
for items, amount in items_to_buy.items():
    print(f'{items} -> {amount}')
