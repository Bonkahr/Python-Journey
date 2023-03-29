def count(s):
    counts = {}
    n = set(s)

    for c in n:
        num = s.count(c)
        counts[c] = num
    return counts


if __name__ == '__main__':
    print(count(''))
