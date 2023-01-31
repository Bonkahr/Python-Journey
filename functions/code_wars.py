from math import gcd


def remove_vowel(string_: str) -> str:
    """
    Get a string form stdIN and remove all the vowels

    :param string_: string in sentence form or word
    :return: string without the vowels
    """
    new_string = ""
    for char in string_:
        if char.casefold() == "a" or char.casefold() == 'e' or \
                char.casefold() == 'i' or char.casefold() == 'o' or \
                char.casefold() == 'u':
            continue
        else:
            new_string += char

    return new_string


# print(remove_vowel("Animals like Melee Like hell"))


def square_sum(n: int) -> int:
    """
    Get an array of integers and compute the sum of their squares.

    :param n: array int
    :return: square sum
    """
    square_sums = 0
    for numbers in n:
        square_sums += numbers * numbers
    return square_sums


# print(square_sum([]))

#
# def alphabet_to_number(string: str) -> str:
#     """
#     Get a string and return the position of each character in the alphabet.
#
#     :param string: string of characters
#     :return: string of digits
#     """
#
#     alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     string_number = ""
#
#     for n in range(1, len(string)):
#         if string[n].casefold() in alphabets:
#             string_number += string[n]
#     return string_number
#
#
# print(alphabet_to_number("animal"))

def to_camel_case(text: str) -> str:
    new_string = ""  # returned string
    after_sep = ""  # character after the non-alphabet

    for j in range(0, len(text)):
        chars = text[j]  # character at index j
        true = chars.isalpha()  # return true if the character is an alphabet

        if after_sep.casefold() == chars:
            new_string += after_sep
            after_sep = ""
        elif true:
            new_string += chars
        else:
            # capitalize next alphabet after non-alphabet character
            if text[j + 1] == text[j + 1].capitalize():
                continue
            else:
                after_sep = text[j + 1].capitalize()

    return new_string


#
# print(to_camel_case("The_pippi-is_Savage"))
# print(to_camel_case("The_eepi-was-Omoshiroi"))


def greatest(x: int, y: int, n: int) -> float:
    """
    Get integers from stdIN find the smallest biggest divisor below the given
    int n.

    :param x: int1
    :param y: int2
    :param n: the highest range
    :return: float
    """
    s = x * y / gcd(x, y)
    return (n - 1) / s * s


def smallest(x, y, n):
    """
    Get integers from stdIN find the smallest biggest divisor below the given
    int n.

    :param x: int1
    :param y: int2
    :param n: the lowest number
    :return: float
    """
    s = x * y / gcd(x, y)
    return n / s * s + s


#
# print(greatest(3, 2, 24))
# print(greatest(1000000007, 1000000009, 10000000000000000000))


def solution(number):
    number_sum = 0
    for numbers in range(number):
        if numbers % 3 == 0 or numbers % 5 == 0:
            number_sum += numbers
    return number_sum


#
# print(solution(10))


def create_phone_number(number: list) -> str:
    str1 = ""
    str2 = ""
    str3 = ""
    for n in range(0, len(number)):
        if n < 3:
            str1 += str(number[n])
        elif n < 6:
            str2 += str(number[n])
        else:
            str3 += str(number[n])

    return "({}) {}-{}".format(str1, str2, str3)


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def sum_of_digits(a: int, b: int) -> int:
    number_string = ""
    total_sum = 0

    for numbers in range(a, b + 1):
        number_string += str(numbers)

    for string_numbers in number_string:
        total_sum += int(string_numbers)

    return total_sum


print(sum_of_digits(1, 10000000))
