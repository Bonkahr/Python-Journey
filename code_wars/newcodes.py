import math


def to_uppercase(string: str) -> str:
    """
    Remove any spaces to separate words in the string then convert all
    letters to uppercase.
    :param string: the given string
    :return: the upper-cased string with no spaces to separate words
    """
    return ' '.join(''.join(string.split()).upper())


print(to_uppercase("i am here but tomorrow i'll be there"))


def prime_numbers(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# print(prime_numbers(9))


def change_vowels(string: str, vowel: str):
    result = ""
    for item in string:
        if item.lower() in 'aeiou':
            result += vowel
        else:
            result += item
    return result


# print(change_vowels('hannah hannah bo-bannah banana fanna fo-fannah fee',
# 'i'))


def reverse_array(arr: list):
    new_arr = [arr[len(arr) - 1]]
    for n in range(1, len(arr)):
        new_arr.append(arr[(len(arr) - (n + 1))])
    return new_arr


print(reverse_array([5, 4, 3, 2, 1]))
print(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 34, 67, 56]))
print(reverse_array(['?', 'you', 'are', 'how', 'world', 'hello']))
print(reverse_array([{'a': 1}, {'b': 2}]))
print(reverse_array(['hello', 'world', 'how', 'are', 'you', '?']))
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 34, 67, 56]
# print(len(a))
# a[0] = a[len(a) - 1]
# print(a)
