def solution_1(numbers: list, left: int, right: int) -> list:
    result = []
    for i, n in enumerate(numbers):
        for j in range(left, right + 1):
            if (i + 1) * j == n:
                result.append(True)
                break
        if len(result) < i + 1:
            result.append(False)
    return result


def solution_2(a: list) -> list:
    str_a = "".join(str(x) for x in a)
    str_b = ''.join(set(str_a))
    repeated_numbers = dict()
    for n in str_b:
        repeated_numbers[n] = str_a.count(n)
    result = []
    for k, v in repeated_numbers.items():
        if v == max(repeated_numbers.values()):
            result.append(int(k))
    return sorted(result)


if __name__ == '__main__':
    num = [8, 5, 6, 16, 5]
    print(solution_1(num, 1, 3))
    print(solution_2([25, 2, 3, 57, 38, 41]))
    g = [0, 1, 2, 3]
    for g[-1] in g:
        print(g[-1])
