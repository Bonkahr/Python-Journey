def task(n: str) -> str:
    n_list = [int(i) for i in n]
    n_list.reverse()
    result = []
    multiplier = 2
    for number in n_list:
        if multiplier <= 7:
            result.append(number * multiplier)
            multiplier += 1
        else:
            multiplier = 2
            result.append(number * multiplier)
            multiplier = 3

    total = sum(result)
    remainder = total % 11

    if remainder == 0:
        n += '0'
    elif remainder == 1:
        n += 'X'
    else:
        n += str(11 - remainder)
    return n


print(task('036532'))
print(task("111111111"))
print(task('12388878'))



