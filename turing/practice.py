def cal_points(ops: list) -> int:
    result = []

    for x in ops:
        try:
            result.append(int(x))
        except ValueError:
            if x == '+':
                result.append(result[-1] + result[-2])
            elif x == 'D':
                result.append(result[-1] * 2)
            elif x == 'C':
                result.pop()
    return sum(result)


if __name__ == '__main__':
    print(cal_points(['5', '2', 'C', 'D', '+']))
    print(cal_points(['5', '-2', '4', 'C', 'D', '9', '+', '+']))
