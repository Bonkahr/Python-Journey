import re


def matcher(string: str) -> bool:
    return bool(re.fullmatch(r'[+-]?\d*\.\d{2}', string))


#
# print(matcher("hellow 11.99"))
# print(matcher('+.99'))


def tribonacci(arr: list, n: int) -> list:
    a, b, c = arr[0], arr[1], arr[2]
    if n > 2:
        result = [arr[0], arr[1], arr[2]]
        for i in range(n - 3):
            a, b, c = b, c, (a + b + c)
            result.append(c)
        return result
    return [m for c in arr for m in range(n)]


print(tribonacci([1, 1, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([300, 200, 100], 0))
