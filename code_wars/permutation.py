from itertools import permutations


#
# d = permutations(['a', 'b', 'c', 'd'])
# for i in list(d):
#     print(i)


def perm(string: str):
    result = []
    lst = [char for char in string]
    p = permutations(lst)
    for e in p:
        x = "".join(e)
        result.append(x)
    return list(set(result))


print(perm('aabb'))

test_array = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

test_array1 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]


def valid_solution(array: list) -> bool:
    def _(lists):
        for row in lists:
            if len(row) != len(set(row)):
                return False
        return True

    # def three_by_three(arraylist, low, high):
    #     for que in range(low, high):
    #         for m in range(low, high):
    #             three_col.append(array[que][m])

    col_array = []
    for i in range(9):
        list1 = []
        for row in array:
            list1.append(row[i])
        col_array.append(list1)
        list1 = []
    three_col = []
    # print(col_array)
    for n in range(3):
        for m in range(3):
            three_col.append(array[n][m])
    for n in range(3, 6):
        for m in range(3):
            three_col.append(array[n][m])

    return _(array) and _(col_array)


#
# print(valid_solution(test_array))
# print(valid_solution(test_array1))
#
# print(test_array1[1][2])


def hi_lo(string: str) -> str:
    s = [int(n) for n in string.split()]
    return f'{min(s)} {max(s)}'


print(hi_lo("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


def ends_with(string: str, ending: str) -> bool:
    end = string[len(string) - len(ending):len(string)]
    return end == ending
