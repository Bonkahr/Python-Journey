import statistics


def nb_dig(sq: int, n: int) -> int:
    return "".join(str(x * x) for x in range(sq + 1)).count(str(n))


print(nb_dig(10, 1))


def palindrome_product(left: int, right: int) -> str:
    pal_list = sorted(set(x * y for x in range(left, right + 1) for y in range(
        left, right + 1) if str(x * y) == str(x * y)[::-1]))
    return f"Range: {format((pal_list[-1] - pal_list[0]), '.2f')}," \
           f" Mean: {format(statistics.mean(pal_list), '.2f')}," \
           f" Median: {format(statistics.median(pal_list), '.2f')} " \
        if len(pal_list) >= 2 else 'Inadequate palindromic products '


print(palindrome_product(40, 55))


lst = ['a', 'b', 'c'] * -3
print(lst)
