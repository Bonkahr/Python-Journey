import math
import string


def pillars(num_pill, dist, width):
    return (num_pill - 1) * dist * 100 + (num_pill - 2) * width if \
        num_pill > 1 else 0


def check_prime(number: int) -> bool:
    for n in range(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return False
    return True


def prime(number: int) -> list:
    primes = []
    for num in range(2, number + 1):
        if check_prime(num):
            primes.append(num)
    return primes


def rank(name_string: str, weight: list, name_search: int) -> str:
    alphabets_dict = {x: n for n, x in
                      enumerate(string.ascii_lowercase, start=1)}
    name = name_string.lower().split(',')
    all_weight = []
    for x in name:
        all_weight.append(sum(alphabets_dict[y] for y in x)) * weight[name.index(x)]
    print(all_weight)


def iter_next(numbers: list):
    x = iter(numbers)
    return [w for w in x if next(x) % 2]


if __name__ == '__main__':
    print(pillars(2, 20, 25))
    print(pillars(533, 10, 33))
    print(prime(25))
    print(check_prime(4))
    print(iter_next(list(range(10))))
    rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
         [4, 2, 1, 4, 3, 1, 2], 4)
