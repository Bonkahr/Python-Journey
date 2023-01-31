def panagram(string: str) -> bool:
    return len(set([s.lower() for s in string if s.isalpha()])) == 26


# print(panagram('The quick brown fox jumps over the lazy dog?'))


def iq_test(s: str) -> int:
    evens = [i for i in s.split() if int(i) % 2 == 0]
    odds = [i for i in s.split() if int(i) % 2 != 0]
    if len(evens) == 1:
        return s.split().index(evens[0]) + 1
    else:
        return s.split().index(odds[0]) + 1


# print(iq_test("2 4 7 8 10"))


def find_reverse_number(n):
    to_return = []
    k = 0
    while len(to_return) < n:
        if str(k) == str(k)[::-1]:
            to_return.append(str(k))
        k += 1
    return ', '.join(to_return)


# print(find_reverse_number(100))


def findAdded(st1: str, st2: str) -> str:
    return ''.join(
        [n * (st2.count(n) - st1.count(n)) for n in sorted(set(st2))])


# print(findAdded('44554466', '447554466'))
# print(findAdded('9876521', '9876543211'))
# print(findAdded('4455446', '447555446666'))
