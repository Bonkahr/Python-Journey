# creating empty sets
# numbers = {*''} or numbers{*{}} but the below format is preferred and
# readable, {} creates an empty dict

numbers = set()

print(type(numbers))

while len(numbers) < 5:
    try:
        numbers.add(int(input('Enter 5 different number, pressing enter: ')))
        print(f'You now have {len(numbers)} numbers entered')
    except ValueError:
        print('That was not a number')


# printing in the order they were typed
print(f'You typed {list(dict.fromkeys(numbers))}')

# printing in sorted order
print(f'Your numbers were: {sorted(numbers)}')

