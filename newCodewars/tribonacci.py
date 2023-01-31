def tribonacci(signature: list, n: int):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


print(tribonacci([1, 1, 1], 12))


def Xbonacci(signature: list, n: int) -> list:
    sign_len = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-sign_len:]))
    return signature[:n]


print(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10))
