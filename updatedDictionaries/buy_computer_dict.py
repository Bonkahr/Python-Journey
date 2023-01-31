available_parts = {'1': 'computer',
                   '2': 'monitor',
                   '3': 'mouse',
                   '4': 'keyboard',
                   '5': 'mouse mat',
                   '6': 'HDMI cable',
                   '7': 'dvd drive',
                   }

current_choice = None
computer_parts = {}


while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if current_choice not in computer_parts:
            print(f'Adding {chosen_part}')
            computer_parts[current_choice] = chosen_part

        else:
            print(f'You already chose -> {chosen_part}')
            print(f'Chosen items:')
            for key, part in computer_parts.items():
                print(f'{key} -> {part}')

    elif current_choice == '8':
        for key, part in computer_parts.items():
            print(f'{key} -> {part}')
        remove = input("What do you want to remove? >")
        removed = computer_parts.pop(remove, 'Not on list')
    else:
        print("Available items: ")
        for key, item in available_parts.items():
            print(f'{key} -> {item}')
        print('0 -> To finish\n8 -> to remove item')

    current_choice = input('Make your choice: > ')



