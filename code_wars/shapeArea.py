import math


def shape_area(a, b, c):
    shape = ''
    area = 0
    if a > 0 and a == b and c == 0:
        shape = 'Square'
        area = int(a * b)
    elif a > 0 and b == 0 and c == 0:
        shape = 'Circle'
        area = f'{int(a * a)}pi'
    elif a > 0 and b > 0 and c == 0:
        shape = 'Rectangle'
        area = int(a * b)
    elif a == b and c > 0:
        shape = 'Triangle'
        area = int(0.5 * a * b)
    else:
        return None
    return f"{shape} with area of {area}"


# print(shape_area(400.00, 400.00, 556.00))
# print(shape_area(4.00, 1.00, 18.00))
# print(shape_area(0.00, 0.00, 0.00))
# print(shape_area(12, 0, 0))
#


def sum_cubes(n):
    return sum(i ** 3 for i in range(n + 1))


print(sum_cubes(123))
