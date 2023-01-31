import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# numpy array can only hold one data type, when mixed numpy doesnt raise an
# error but instead change the dat type to match all the matrix

print(matrix)
print(matrix[0, 1])
