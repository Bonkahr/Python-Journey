def sol(n: int, a: list) -> list:
    solution = [a[0] + a[1]]

    for i in range(1, n):
        if i < len(a) - 1:
            solution.append(a[i - 1] + a[i] + a[i + 1])
        else:
            solution.append(a[i - 1] + a[i])
    return solution


if __name__ == '__main__':
    print(sol(5, [4, 0, 1, -2, 3]))
