def year_diff(date_1: str, date_2: str) -> int:
    return abs(int(date_1.split('/')[0]) - int(date_2.split('/')[0]))


print(year_diff('1997/10/10', '2022/10/10'))


def add_remainder(num, div): return [k + k % div for k in num]


print(add_remainder([2, 7, 5, 9, 100, 34, 32, 0], 3))


def sum_of_digits(a, b):
    return sum(int(n) for p in range(a, b + 1) for n in str(p))


print(sum_of_digits(1, 788))

