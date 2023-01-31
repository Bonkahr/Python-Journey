import math

a = [1, 2, 3, 4, 5, 5, 2, 7, 8, 8, 4, 6, 7, 5, 2, 2]
b = 2
# a.remove(2)
# print(a)


def remove_occurence(order: list, max_e: int) -> list:
    result = []
    for item in order:
        counts = result.count(item)
        if counts < max_e:
            result.append(item)
    return result

#
# print(remove_occurence(a, b))
c = "testing"
d = "test"


def return_middle(string: str) -> str:
    length = len(string)
    if length % 2 == 0:
        return f'{string[(length // 2) - 1]}{string[length // 2]}'
    else:
        return string[length // 2]


#
# print(return_middle(c))
# print(return_middle(d))


def remove_outline(integers: list) -> int:
    # count = 0
    # for i in range(4):
    #     if integers[i] % 2 == 0:
    #         count += 1
    # if count > 1:
    #     for item in integers:
    #         if item % 2 != 0:
    #             return item
    # else:
    #     for item in integers:
    #         if item % 2 == 0:
    #             return item
    evens = [n for n in integers if n % 2 == 0]
    odds = [n for n in integers if n % 2 != 0]
    return evens[0] if len(evens) == 1 else odds[0]


print(remove_outline([2, 4, 0, 100, 4, 11, 2602, 36]))
print(remove_outline([160, 3, 1719, 19, 11, 13, -21]))


def narcissistic_number(value: int) -> bool:
    return sum([math.pow(int(num), len(str(value))) for num in str(value)]) \
           == value
    # result = 0
    # for num in str(value):
    #     result += math.pow(int(num), len(str(value)))
    # return result == value


print(narcissistic_number(153))


def triple_x(s: str) -> bool:
    for index, char in enumerate(s):
        if index > len(s) - 3:
            return False
        if char == 'x' and s[index + 1] == 'x' and s[index + 2] == 'x':
            return True
        elif char == 'x' and s[index + 1] != 'x':
            return False


my_list = 'xxx'
list2 = 'xoxotreolxxx'


#
# print(triple_x(my_list))
# print(triple_x(list2))


def booleans(sheeps: list) -> int:
    return sheeps.count(True)


#
# print(booleans([True, True, True, False,
#                 True, True, True, True,
#                 True, False, True, False,
#                 True, False, False, True,
#                 True, True, True, True,
#                 False, False, True, True]))


def mubling(string: str) -> str:
    # new_string = ''
    # for index, chars in enumerate(array):
    #     new_string += chars.capitalize() + chars.lower() * index + '-'
    # return new_string.strip('-')
    return '-'.join(char.upper() + char.lower() * index for index, char in
                    enumerate(string))


# print(mubling("RqaEzty"))

