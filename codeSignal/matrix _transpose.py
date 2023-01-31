def matrix_transpose(matrix: list) -> list:
    transposed_matrix = []
    for i in range(len(matrix[0])):
        new_mat = []
        for x in matrix:
            new_mat.append(x[i])
        transposed_matrix.append(new_mat)
    return transposed_matrix


def remove_elements(arr: list) -> list:
    return [elem for i, elem in enumerate(arr) if i % 2 == 0]


def repeat_chars(sentence: str) -> str:
    new_str = ''
    for x in sentence:
        new_str += x * 2
    return new_str


def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res = res[1:len(res) - 1]
    return res


if __name__ == '__main__':
    list_a = [[1, 2, 3], [4, 5, 6]]
    list_b = [[1]]
    print(matrix_transpose(list_a))
    print(matrix_transpose(list_b))
    my_arr = [True, True, False, False, False, True, True]
    print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(remove_elements(my_arr))
    print(repeat_chars('Hello World!'))
    b = [3, 4, 2, 4, 38, 4, 5, 3, 2]
    print(solution(b))
