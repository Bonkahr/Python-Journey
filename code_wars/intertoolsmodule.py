from itertools import permutations


def next_bigger(n):
    """
    Form the next bigger number from the arg
    :param n: number
    :return: next bigger number, None if no bigger number

    TODO: Fix time, can't pass in code_wars but works fine
    """
    perm_arr = sorted(set([int("".join(n)) for n in permutations(str(n))]))
    try:
        return None if len(perm_arr) == 1 else perm_arr[perm_arr.index(n) + 1]
    except IndexError:
        return None


print(next_bigger(414))
