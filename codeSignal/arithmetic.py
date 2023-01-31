def arith(a, b, c) -> bool:
    return True if (a + b == c or a - b == c or a / b == c or a * b == c) \
        else False


def tennis(s1: int, s2: int) -> bool:
    return True if ((s1 == 6 and s2 < 5) or (s2 == 6 and s1 < 5) or
                    (s1 == 7 and s2 <= 6) or s2 == 7 and s1 <= 6) else False


def beauty(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    elif (not young or not beautiful) and loved:
        return True
    else:
        return False


def metro_card(ln: int) -> list:
    return [28, 30, 31] if ln == 31 else [31, ]


if __name__ == '__main__':
    print(arith(2, 3, 5))
    print(tennis(9, 6))
    print(beauty(False, False, True))
