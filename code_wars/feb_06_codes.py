def dbl_linear(n: int) -> int:
    numbers = [1]

    for x in numbers:
        if len(numbers) < n * 2:
            to_append = 2 * x + 1
            to_append1 = 3 * x + 1
            if to_append not in numbers:
                numbers.append(to_append)
            if to_append1 not in numbers:
                numbers.append(to_append1)
        else:
            break
    # print(numbers)
    # print(len(numbers))
    return sorted(numbers)[n]


def solution(n: int, d: int) -> list:
    n = [int(x) for x in str(n)]
    if d <= 0:
        return []
    return n[len(n) - d:] if d < len(n) else n


if __name__ == '__main__':
    print(dbl_linear(50))
    print(solution(34625647867585, 10))
    print(solution(123767, 10))
