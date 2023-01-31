from time import perf_counter
from functools import wraps, lru_cache


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}s')
        return result

    return wrapper


@lru_cache(maxsize=None)    # improve performance like charm
@timer
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    s = perf_counter()
    print(fib(50))
    print(perf_counter() - s)
