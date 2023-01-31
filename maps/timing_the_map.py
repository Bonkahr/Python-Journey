import timeit

text = 'What have the Luos ever done to us'


def time_one():
    capitals = [char.upper() for char in text]
    return capitals


# Map version


def time_two():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def time_three():
    words_capital = [word.upper() for word in text.split(' ')]
    return words_capital


# map version


def time_four():
    map_word_capitals = list(map(str.upper, text.split(' ')))
    return map_word_capitals


if __name__ == '__main__':
    timer_1 = timeit.timeit(time_one, number=100000)
    timer_2 = timeit.timeit(time_two, number=100000)
    timer_3 = timeit.timeit(time_three, number=100000)
    timer_4 = timeit.timeit(time_four, number=100000)

    print(f'comp v: {timer_1} -> map_v: {timer_2}')
    print(f'comp v: {timer_3} -> map_v: {timer_4}')

