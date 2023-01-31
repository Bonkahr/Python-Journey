def solution(code, x):
    code = code.replace('\t', (' ' * x))
    return code


def century(year):
    return year // 100 if year % 100 == 0 else (year // 100) + 1


def sol(arr):
    if arr:
        n, arr = arr[0], arr[1:]
        max_p = min(arr)
        for x in arr:
            pro = n * x
            n = x
            if pro > max_p:
                max_p = pro

        return max_p


def solute(n):
    time = str(n // 60) + str(n % 60)
    return sum(int(x) for x in time)


def minutes(min1, min2_10, min11, s):
    m = 0
    if s >= min1:
        m = 1
        s -= min1
    for x in range(2, 11):
        if s > min2_10:
            m += 1
            s -= min2_10
        else:
            break
    if s > min11:
        m += s // min11
    return m


def salute(v1, w1, v2, w2, mx):
    d = {w1: v1, w2: v2}
    if mx >= w1 + w2:
        return v1 + v2
    elif mx >= max(w1, w2):
        return max(v1, v2)
    elif mx >= min(w1, w2):
        return d[min(w1, w2)]
    else:
        return 0


if __name__ == '__main__':
    word = "\treturn False"
    print(solution(word, 2))
    print(century(2005))
    print(sol([1, 0, 1, 0, 1000]))
    print(808 % 60)
    print(solute(808))
    print(minutes(2, 2, 1, 2))
    print(salute(2, 5, 3, 4, 5))
    print(5 % 1)
    print(1 % 2)