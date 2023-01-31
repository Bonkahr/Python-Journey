import math
import statistics


def piggy(pig: str) -> str:
    return " ".join([word if len(word) == 1 and not word.isalpha() else
                     f'{word[1:]}{word[0]}ay' for word in pig.split()])


print(piggy('Pig latin is cool'))
print(piggy('Hello world !'))


# name = 'james'
# print(name[-1])
# print(name[1:])


def zero(n: int) -> int:
    return int(f"{str(n)[0:int(len(str(n)) / 2)]}"
               f"{'0' * (len(str(n)) - int(len(str(n)) / 2))}") if len(str(n)) \
                                                                   > 1 else n


# print(zero(4))


def stats(arr: list):
    mean = statistics.mean(arr)
    return mean


# print(stats([1, 2, 3, 4, 5, 6, 7, 7, 8, 9]))


def fake_bin(x):
    return ''.join(['1' if int(k) >= 5 else '0' for k in list(x)])


print(fake_bin('234578765421'))


def eureka(a: int, b: int) -> list:#
    result = []
    for que in range(a, b + 1):
        p_sum = 0
        for i, l in enumerate(str(que), start=1):
            p_sum += math.pow(int(l), i)
        if p_sum == que:
            result.append(int(p_sum))
            p_sum = 0
    return [x for x in range(a, b + 1)
            if sum(int(y) ** i for i, y in enumerate(str(x), start=1)) == x]


print(eureka(10, 100))
