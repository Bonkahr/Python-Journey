import math
import re


def are_squares(numbers: list):
    if numbers:
        return len([n for n in numbers if math.sqrt(n).is_integer()]) == len(
            numbers)
    return None


# print(are_squares([1, 4, 9, 16, 25]))
# print(4.00.is_integer())


def pad(string):
    mobile_pads = {
        1: 7, 2: 8, 3: 9, 4: 4, 5: 5, 6: 6, 7: 1, 8: 2, 9: 3, 0: 0
    }
    return ''.join([str(mobile_pads[int(i)]) for i in string])


# print(pad("0789456123"))


def remove_non_str(string):
    return ''.join(n for n in string if n.isalpha() or n == ' ')


# print(remove_non_str("that's a pie$ce o_f p#ie!"))


def divisors(integer):
    divisor = [n for n in range(2, int(integer / 2 + 1)) if integer % n == 0]
    return divisor if divisor else f'{integer} is prime'


# print(divisors(13))


def row_weights(array):
    # return sum([array[n] for n in range(0, len(array), 2)]), \
    #        sum([array[n] for n in range(1, len(array), 2)])
    return sum(array[::2]), sum(array[1::2])


# print(row_weights([50, 60, 70, 80]))
# print(row_weights([29, 83, 67, 53, 19, 28, 96]))
# print(row_weights([80]))
# print(row_weights([]))


def invite_more_women(arr: list) -> bool:
    return sum(arr) > 0


# print(invite_more_women([1, -1]))


def is_nice(arr):
    for x in arr:
        if x + 1 not in arr and x - 1 not in arr:
            return False
    return True


# print(is_nice([2, 10, 9, 3, 6]))


def show_sequence(n):
    if n == 0:
        return '0==0'
    return f"{'+'.join([str(n) for n in range(n + 1)])} = " \
           f"{sum(range(n + 1))}" if n > 0 else f"{n}<0"


# print(show_sequence(-7))


def automorphic(n: int) -> str:
    return 'Automorphic' if str(n) == str(n * n)[-len(str(n)):] else 'Not!!'


print(automorphic(625))

array_1 = [1, 2, 3, 4, 5, 6]
print(array_1[1::2])
