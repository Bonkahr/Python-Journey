available_parts = ['computer',
                   'monitor',
                   'mouse',
                   'keyboard',
                   'mouse mat',
                   'HDMI cable',
                   'dvd drive'
                   ]

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

computer_parts = []

current_choice = "-"

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # remove the item
            print('removing {}'.format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print('Adding {}'.format(current_choice))
            computer_parts.append(chosen_part)
        print('Your list now contains: {}'.format(computer_parts))
    else:
        print('Choose from the options below')
        for number, part in enumerate(available_parts):
            print('{0}. {1}'.format(number + 1, part))
    current_choice = input('Enter your option: ')

print(computer_parts)
