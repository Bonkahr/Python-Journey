print(__name__)


def factorial(number):
    """ calculate number! iteratively"""
    fact = 1
    for n in range(1, number + 1):
        fact *= n
    return fact


def factorials(number):
    """ calculate number! recursively"""
    if number <= 1:
        return 1
    else:
        return number * factorials(number-1)


# print(factorials(130))
# print(factorial(130))


def fib(n):
    """ F(n) = F(n - 1) + F(n -2)"""
    fn, a, b = 0, 0, 1
    for n in range(0, n):
        a = b
        b = fn
        fn = a + b
    return fn
    # recursively is slower after 30 calls`
    # if n < 2:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)


print(fib(10))
# for q in range(0, 36):
#     print(f'{q} = {fib(q)}')
