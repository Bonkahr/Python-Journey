for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j} | ', end='')

print()

for number1, number2, multiple in [(i, j, i * j) for i in range(1, 11) for j
                                   in range(1, 11)]:
    print(f'{number1} x {number2} = {multiple} | ', end="")

# generator expression of the above nested list, use () instead of [].
print()
for number1, number2, multiple in ((i, j, i * j) for i in range(1, 11) for j in
                                   range(1, 11)):
    print(f'{number1} x {number2} = {multiple} | ', end="")
