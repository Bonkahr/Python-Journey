def three_array(array: list) -> list:
    """
    Create a 3 by 3 square lists
    :param array: sudoku lists
    :return: new Array from the 3x3 squares
    """
    answer = []
    for i in range(3):
        for j in range(3):
            arr = []
            for lst in array[i * 3:(i + 1) * 3]:
                arr += lst[j * 3:(j + 1) * 3]
            answer.append(arr)
    return answer


def count_digits(lists):
    """
    Check occurrences of numbers 1-9 if it occurs more than one return
    False, else True
    :param lists:
    :return: bool
    """
    for list_ in lists:
        for n in range(1, 10):
            count = list_.count(n)
            if count != 1 or len(list_) > 9 or len(lists) > 9:
                return False
    return True


def valid_solution(array: list) -> bool:
    reverse_array = [[row[i] for row in array] for i in range(9)]
    return count_digits(array) and count_digits(reverse_array)# and
    # count_digits(three_array(array))


sudoku_1 = [
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

sudoku_2 = [
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
#
# print(valid_solution(sudoku_1))
# print(valid_solution(sudoku_2))

print(three_array(sudoku_2))
