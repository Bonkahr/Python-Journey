def solution(cards):
    res = -1

    for c in cards:
        for i in c:
            k = c.count(i)
            if k == 1 and i > res:
                res = i
    return res


print(solution([[5, 7, 3, 9, 4, 9, 8, 3, 1], [1, 2, 2, 4, 4, 1], [1, 2, 3]]))
