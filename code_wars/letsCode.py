import math


def is_sum_of_cubes(string: str):
    string5 = "".join([n if n.isdigit() else '-' for n in string]).split('-')
    result = [x for x in string5 if x]
    array_1 = []
    for item in result:
        start = 0
        stop = len(item)
        while stop > 0:
            array_1.append(item[start: start + 3])
            stop -= 3
            start += 3
    new_array = [int(sum(math.pow(int(n), 3) for n in items)) for items in
                 array_1 if sum(math.pow(int(n), 3) for n in items) == int(
            items) and int(items) > 0]
    return f"{' '.join(str(n) for n in new_array)} {sum(new_array)} Lucky" if\
        new_array else 'Unlucky'


print(is_sum_of_cubes("aqdf&0#1xyz!22[153(777.777"))
print(is_sum_of_cubes("&z _upon 41072987786a --- ???ry, ww/100 I thought, "
                      "631str*ng and w===y -721&()"))


#
# a = "1,2,3,4,5,6,7,8,9,7,6,6,"
# b = a.split(",")
# print(b)


def comp(a: list, b: list) -> bool:
    if a is None or b is None:
        return False
    for n in a:
        if n * n in b:
            b.remove(n * n)
        else:
            return False
    if len(b) != 0:
        return False
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
b1 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144,
      19 * 19]

a2 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144,
      19 * 19]

a3 = [121, 144, 19, 161, 19, 144, 19, 11]
b3 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144,
      19 * 19]


#
# print(comp(a1, b1))
# print(comp(a2, b2))
# print(comp(a3, b3))


def multiple3(x):
    if x % 3 == 0:
        return x
    while x > 0:
        if x % 3 == 0:
            return x
        x = math.floor(x / 10)
    return None


# print(multiple3(25))


def sort_array(a: list) -> list:
    return sorted(a) if a else []


s = [1, 3, 6, 3, 9, 0, 3, 5, 7]
b = []


# print(sort_array(s))


# shortest word


def find_short(string: str) -> int:
    n = len(string.split(" ")[0])
    for word in string.split(" "):
        if len(word) < n:
            n = len(word)
    return n

# print(find_short("bitcoin take over the world maybe who knows perhaps"))


# def valid_braces(array: str):
#     for i in range(len(array)):
#
#         if array[i] != array[(len(array) - 1) - i]:
#             return False
#     return True
#
#
# print()
# alid_braces = "[(])"
# f = (len(alid_braces))
# print(f)
# print(alid_braces[(f - 1) - 1])



