import math


def ball(h: int, bounce: float, window: float) -> int:
    if h < 0 or h < window or (bounce < 0 or bounce >= 1):
        return -1
    else:
        rounds = 1
        while h > window:
            h *= math.floor(bounce)
            rounds += 2

        return rounds


# print(ball(3, 0.66, 1.5))
# print(ball(30, 0.75, 1.5))


def digital_root(n: int) -> int:
    # if len(str(que)) == 1:
    #     return que
    # else:
    #     temp = 0
    #     result = 0
    #     while len(str(que)) != 1:
    #         for numbers in str(que):
    #             temp += int(numbers)
    #         result, que = temp, temp
    #         temp = 0
    # return result
    return n % 9 or n and 9


print(digital_root(132189))
print(digital_root(12087))
print(digital_root(2))
