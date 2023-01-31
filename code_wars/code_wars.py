import string


def divisors(n):
    counter = 0
    if n > 0:
        counter = 1
        for digit in range(1, int(n / 2 + 1)):
            if n % digit == 0:
                counter += 1
    return counter


def divisors2(n):
    return sum(n % x == 0 for x in range(1, n + 1))


# print(divisors(5000003))

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# print(leap_year(1100))

def replace_with_numbers(string_):
    string_ = string_.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit_string = ""
    loop = 0
    while loop < len(string_):
        for alphabet in string_:
            loop += 1
            if alphabet in alphabets:
                digit_string += str(alphabets.index(alphabet) + 1)
            digit_string += " "
    return digit_string.strip()


print(replace_with_numbers("The sunset sets at twelve o'clock"))


def replace_with_letters(number_string):
    alphas = string.ascii_lowercase + ''
    word = ''
    print(f"space ->'{number_string.split(' ')[3]}'")

    for n in number_string.split():
        if n:
            word += alphas[int(n) - 1]
        if n == '':
            word += " "
    return word


print(replace_with_letters('20 8 5  19 21 14 19 5 20  19 5 20 19  1 20  20 23 '
                           '5 12 22 5  15  3 12 15 3 11'))
