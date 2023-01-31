a = 2
b = 3

print(f'a is {a} and b is {b}')

# swapping numbers.
a, b = b, a
print(f'a is {a} and b is {b}')


def fib():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fibonacci = fib()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))



