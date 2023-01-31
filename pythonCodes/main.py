def closest(numbers: str) -> list[int]:
    weight = {}
    for i, n in enumerate(numbers.split(' ')):
        total = 0
        for x in n:
            total += int(x)
        weight[total] = i
    return sorted(weight)


print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))
