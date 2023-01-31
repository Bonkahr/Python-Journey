def max_ball(v: int) -> int:
    str1 = str(v)
    concat = ''
    for digits in str1:
        concat += str(int(digits) ** 2)
    return int(concat)


def insurance(age: int, size: str, no_of_days: int) -> int:
    if no_of_days > 0:
        charges = 0
        if age < 25:
            charges += 10 * no_of_days
        if size == "economy".casefold():
            charges += 0
        elif size == "medium".casefold():
            charges += 10 * no_of_days
        else:
            charges += 15 * no_of_days
        return charges + (50 * no_of_days)
    return 0


if __name__ == '__main__':
    print(max_ball(9119))
    print(insurance(21, "economy", -30))
