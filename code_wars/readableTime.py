import math


def format_duration(seconds: int):
    years = seconds // (60 * 60 * 24 * 365)
    days = (seconds // (60 * 60 * 24)) - (years * 365)
    hours = (seconds // (60 * 60) - ((years * 365 * 24) + (days * 24)))
    minutes = (seconds // 60) - ((years * 365 * 24 * 60) + (days * 24 * 60)
                                 + (hours * 60))
    seconds = seconds - ((years * 365 * 24 * 60 * 60) + (days * 24 * 60 * 60)
                         + (hours * 60 * 60) + (minutes * 60))
    y = 'years' if years > 1 else 'year'
    d = 'days' if days > 1 else 'day'
    h = 'hours' if hours > 1 else 'hour'
    m = 'minutes' if minutes > 1 else 'minute'
    s = 'seconds' if seconds > 1 else 'second'

    # array with all 0 or more of the variables values
    result = f'{years} {y} {days} {d} {hours} {h} {minutes} {m} {seconds} ' \
             f'{s}'.split()

    # list with only the variables values greater than zero
    answer = [f'{result[n]} {result[n + 1]}' for n in range(0, 10, 2) if int(result[n]) != 0]
    # for que in range(0, 10, 2):
    #     if int(result[que]) != 0:
    #         answer.append(f'{result[que]} {result[que + 1]}')
    # print(answer)

    if len(answer) == 0:
        return 'now'
    elif len(answer) == 1:
        return answer[0]
    elif len(answer) == 2:
        return f'{answer[0]} and {answer[1]}'
    elif len(answer) == 3:
        return f'{answer[0]}, {answer[1]} and {answer[2]}'
    elif len(answer) == 4:
        return f'{answer[0]}, {answer[1]}, {answer[2]} and {answer[3]}'
    else:
        return f'{years} {y} {days} {d} {hours} {h} {minutes} {m} {seconds} ' \
             f'{s}'


print(format_duration(12344565))


def expanded_form(num: int) -> str:
    ans = ''
    multiplier = math.pow(10, len((str(num))) - 1)
    for n in str(num):
        if int(n) > 0:
            ans += f'{str(int(n) * int(multiplier))} + '
        multiplier /= 10
    return ans.rstrip(' +')


# # print(expanded_form(70304))
# print(list(reversed(range(1, 5))))
#
# print('simon'.upper())


def hero(bullets, dragons):
    return dragons * 2 <= bullets


print(hero(7, 4))
