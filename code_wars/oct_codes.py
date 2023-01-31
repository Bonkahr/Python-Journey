def solution(matrix):
    d_arrow, u_arrow, v_x, r_arrow, l_arrow = [], [], [], [], []
    for j, m in enumerate(matrix):
        for i, n in enumerate(m):
            if n == 'x':
                v_x.append(j)
                v_x.append(i)
            elif n == '>':
                r_arrow.append(j)
                r_arrow.append(i)
            elif n == '<':
                l_arrow.append(j)
                l_arrow.append(i)
            elif n == '^':
                u_arrow.append(j)
                u_arrow.append(i)
            elif n == "v":
                d_arrow.append(j)
                d_arrow.append(i)
    print(f"up->{u_arrow}, down ->{d_arrow}, right->{r_arrow}, left->"
          f"{l_arrow}, x-position->{v_x}")
    if d_arrow:
        return d_arrow[0] < v_x[0] and d_arrow[1] == v_x[1]
    if u_arrow:
        return u_arrow[0] > v_x[0] and u_arrow[1] == v_x[1]
    if r_arrow:
        return r_arrow[1] < v_x[1] and r_arrow[0] == v_x[0]
    if l_arrow:
        return l_arrow[1] > v_x[1] and l_arrow[0] == v_x[0]
    return False


mat = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', '>', 'x', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

mat2 = [
    [' ', ' ', ' ', ' '],
    ['>', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    ['x', ' ', ' ', ' ']
]


#
# print(solution(mat))
# print(solution(mat2))


def is_crossed(distances):
    north = sum(distances[::4])
    west = sum(distances[1::4])
    south = sum(distances[2::4])
    east = sum(distances[3::4])
    print(north, west, south, east)
    if len(distances) < 4:
        return north >= south and east >= west
    return north >= south


print(is_crossed([5, 5, 7, 7, 5, 5]))
length = [64, 7, 29, 66, 41, 63, 88, 102, 105, 105, 85, 95, 18, 54, 45, 41, 68,
          96, 5, 80, 98, 63, 12, 62, 23, 14, 48, 61, 63, 61, 87, 40, 6, 89, 101,
          87, 21, 77, 17, 104, 96, 7, 58, 7, 42, 31, 85, 55, 29, 100, 66, 38,
          12, 59, 89, 36, 92, 29, 68, 50, 102, 1, 87, 68, 86, 99, 39, 42, 103,
          89, 50, 45, 70, 89, 91, 95, 11, 80, 45, 82, 49,
          ]
print(is_crossed(length))
print(len(length))
