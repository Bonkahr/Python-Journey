import math


def make_readable(seconds: int) -> str:
    hours = math.floor(seconds / 3600)
    rem_h = seconds % 3600
    minutes = math.floor(rem_h / 60)
    second = rem_h % 60

    return f'{hours:0>2}:{minutes:0>2}:{second:0>2}'


# print(make_readable(359999))
# print(make_readable(86399))
# print(make_readable(60))


def return_in_order(chars) -> list:
    new = []
    for n in range(len(chars)):
        if n < len(chars) - 1:
            if chars[n + 1] == chars[n]:
                continue
            else:
                new.append(chars[n])
        else:
            new.append(chars[n])
    return new


# print(return_in_order('AAAABBBCCDAABBBC'))
# print(return_in_order([10, 10,
#                        10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#                        10, 10, 10, 10, 10]))


def remove_dup(a: list, b: list) -> list:
    new_list = []
    for n in a:
        if n not in b:
            new_list.append(n)
    return new_list


# print(remove_dup([1, 2, 2, 2, 3], [2]))


def no_repeat(string: str) -> bool:
    for letter in string:
        counter = string.lower().count(letter)
        if counter > 1:
            return False
    return True


# print(no_repeat("Dermatoglyphics"))
# print(no_repeat('aba'))
# print(no_repeat('mOose'))


def find_x_o(string: str) -> bool:
    string = string.lower()
    return string.count('x') == string.count('o')


def valid_pin(pin: str):
    if len(pin) != 4 and len(pin) != 6:
        return False
    for char in pin:
        if char.isdigit():
            continue
        else:
            return False
    return True


#
# print(valid_pin('ab3456'))
# print(valid_pin('aa1234'))
# print(valid_pin('-23456'))
# print(len('1234'))

n = [3, 4, 7, 5, 6, 8, 9]


def sort_odds(source_array: list) -> list:
    # arr_odds = []
    result = []

    # create a list of odd numbers only

    arr_odds = [n for n in source_array if n % 2 != 0]
    # for item in source_array:
    #     if item % 2 != 0:
    #         arr_odds.append(item)

    sorted_arr = sorted(arr_odds)
    count = 0  # count number of odds inserted

    for item in source_array:
        # append even items
        if item % 2 == 0:
            result.append(item)

        # append odd items
        else:
            result.append(sorted_arr[count])
            count += 1
    return result


print(sort_odds(n))

