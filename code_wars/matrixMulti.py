import numpy as np

a = [
    [1, 2],
    [3, 4],
]

b = [
    [3, 4],
    [5, 8],
]


def matrix_multi(matrix, matrix1):
    return np.array(matrix) @ np.array(matrix1)


print(matrix_multi(a, b))
#

