import timeit
from statistics import mean, stdev


def fact(n=100):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n=100):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(timeit.timeit('x= fact(130)', setup='from __main__ import fact',
                        number=10000))
    print(timeit.timeit('x = factorial(130)', setup='from __main__ import '
                                                    'factorial', number=10000))

    # using the timeit.repeat

    list1 = timeit.repeat('x= fact(130)', setup='from __main__ import fact',
                          number=10000, repeat=6)
    list2 = timeit.repeat('x = factorial(130)', setup='from __main__ import '
                            'factorial', number=10000, repeat=6)

    print(f'mean: {mean(list1)}, stdev: {stdev(list1)}')
    print(f'mean: {mean(list2)}, stdev: {stdev(list2)}')

