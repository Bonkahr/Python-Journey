def find_roots(a: int, b: int, c: int) -> tuple:

    try:
        positive_sol = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    except ValueError:
        positive_sol = None
    try:
        negative_sol = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    except ValueError:
        negative_sol = None

    if negative_sol is None:
        return positive_sol
    elif positive_sol is None:
        return negative_sol
    else:
        return positive_sol, negative_sol


if __name__ == '__main__':
    print(find_roots(342, 10, 8))
