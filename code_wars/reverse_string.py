import math


def is_square(number: int) -> bool:
    if number < 0:
        return False
    return math.sqrt(number).is_integer()


# print(is_square(-1))


def printer_error(string: str) -> str:
    bad_colours = 0
    for n in string:
        if n in "nopqrstuvwxyz":
            bad_colours += 1
    return "{}/{}".format(bad_colours, len(string))


# print(printer_error('aaabbbbyhaijjjm'))


def valid_ISBN10(isbn: str) -> bool:
    totals = 0
    if len(isbn) == 10:
        for n in range(0, len(isbn)):
            if isbn[n] == 'X':
                if n != 9:
                    break
                else:
                    totals += 10 * (n + 1)
            elif isbn[n].isalpha():
                return False
            else:
                totals += (n + 1) * int(isbn[int(n)])
        return totals != 0 and totals % 11 == 0
    return False


def valid_ISBN101(isbn: str) -> bool:
    totals = 0
    if len(isbn) == 10:
        for n in range(0, len(isbn)):
            if n < 9 and isbn[n].isalpha():
                return False
            else:
                if isbn[n] == 'X':
                    totals += 10 * (n + 1)
                    break
                elif isbn[n].isalpha():
                    return False
                else:
                    totals += int(isbn[int(n)]) * (n + 1)
        return totals % 11 == 0
    return False


# print(valid_ISBN10('1112223339'))


def fibonacci(n: int) -> list:
    fibonacci_numbers = []
    a = 0
    b = 1
    c = a + b

    # for number in range(que - 2):
    while True:
        a, b = b, c
        c = a + b
        if c < n:
            fibonacci_numbers.append(c)
        else:
            break
    return fibonacci_numbers


# print(fibonacci(1000))


def split_me():
    return "james was here but he is no longer here".split()


# print(split_me())


def numbers(string: str):
    add = 0
    string1 = string.split(',')
    print(string1)
    for number in string1:
        number = int(number)
        if number > 1:
            add += number
    return add


# print(numbers("2, 3,415,647"))


def name(string: str):
    return string.casefold().count('5')


# print(name('121324354556676889'))


def name_shuffler(str_):
    str_list = str_.split()
    return f'{str_list[1]} {str_list[0]}'


print(name_shuffler("judy wanjiru kimani"))
