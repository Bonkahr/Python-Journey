entries = [1, 2, 3, 4, 5]

print(f'all: {all(entries)}')
print(f'ant: {any(entries)}')

entries = [1, 2, 3, 0, 4, 5]
print(f'all: {all(entries)}')  # prints false, 0 returns false
print(f'ant: {any(entries)}')  # checks whether there's any true value

empty_entries = []
print(f'all: {all(empty_entries)}')  # prints true, empty returns true
print(f'ant: {any(empty_entries)}')  # checks whether there's any true value
