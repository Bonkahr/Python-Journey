import timeit

for_loop = """\
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j} | ', end='')
"""
print()

nested_for_loop = """\
for number1, number2, multiple in [(i, j, i * j) for i in range(1, 11) for j
                                   in range(1, 11)]:
    print(f'{number1} x {number2} = {multiple} | ', end="")
"""

# generator expression of the above nested list, use () instead of [].
print()

generator_loop = """\
for number1, number2, multiple in ((i, j, i * j) for i in range(1, 11) for j in
                                   range(1, 11)):
    print(f'{number1} x {number2} = {multiple} | ', end="")
"""


result_1 = timeit.timeit(for_loop, number=10000)

result_2 = timeit.timeit(nested_for_loop, number=10000)

result_3 = timeit.timeit(generator_loop, number=10000)
print()
print(f'Generator loop: {result_3}')
print(f'For loop: {result_1}')
print(f'Nested for loop: {result_2}')
