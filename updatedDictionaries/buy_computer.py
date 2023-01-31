available_parts = {'1': 'computer',
                   '2': 'monitor',
                   '3': 'mouse',
                   '4': 'keyboard',
                   '5': 'mouse mat',
                   '6': 'HDMI cable',
                   '7': 'dvd drive',
                   }

current_choice = None
chosen_items = []

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part not in chosen_items:
            print(f'Adding {chosen_part}')
            chosen_items.append(available_parts[current_choice])
        else:
            print(f'You already chose {chosen_part}')
            print(f'This are your chosen items: {chosen_items}')
    else:
        print("Available items: ")
        for key, item in available_parts.items():
            print(f'{key} -> {item}')
        print('0 -> To finish')

    current_choice = input('Make your choice: > ')



