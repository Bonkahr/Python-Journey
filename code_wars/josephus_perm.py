import re


def remove(s: str) -> str:
    k = s.count("!")
    new_s = []
    for word in s.split():
        x = ""
        for char in word:
            if char != "!":
                x += char
        new_s.append(x)
    return " ".join(new_s) + "!" * k


def number(lines: list):
    return [f'{i}:{x}' for i, x in enumerate(lines, 1)]


def save(n: list, cap: int):
    counter, total = 0, 0
    for x in n:
        total += x
        if total <= cap:
            counter += 1
    return counter


def dbl_linear(n):
    u = 0
    i = 0
    result = []
    while len(result) < n * 2:
        result.append(2 * u + 1)
        result.append(3 * u + 1)
        u = result[i]
        i += 1
    result = sorted(set(result))
    return result[n]


def solve(s):
    return max(len(v) for v in re.findall(r'[aeiou]+', s))


def medians(array: list):
    # array = sorted(array)
    return sorted(array)[len(array) // 2] if len(array) % 2 != 0 \
        else (array[(len(array) // 2)] + sorted(array)[(len(array) // 2 - 1)]) / 2


if __name__ == '__main__':
    print(remove("H!i! Hi! hi! well! war!"))
    print(number(["a", "b", "c"]))
    print(save([4, 4, 4, 3, 3], 11))
    print(dbl_linear(10))
    # # print(result.index(22), result.index(57), result.index(91),
    # #       result.index(130), result.index(189))
    # result = sorted(set(result))
    # print(len(result))
    # print(result.index(22), result.index(57), result.index(91),
    #       result.index(130), result.index(189))
    # print(result[10], result[20], result[30], result[40], result[50])

    print(solve("ultrarevolutionariees"))
    print(medians([1234, 345, 78, 81]))
    print(medians([3, 2, 1]))
    print(medians([33, 99, 100, 30, 29, 50]))
