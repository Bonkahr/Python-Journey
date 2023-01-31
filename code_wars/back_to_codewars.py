import string


def function_num(number_list: list) -> (list, list):
    def prime_number(num):
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True

    primes = [number for number in number_list if prime_number(number)]

    divisors = dict()
    for number in number_list:
        divisors_count = 1
        div = []
        for n in range(1, int(number / 2) + 1):
            if number % n == 0:
                divisors_count += 1
                div.append(n)
        divisors[number] = divisors_count

    max_divisors = max(divisors.values())
    numbers_with_max_divisors = []
    for key, value in divisors.items():
        if value == max_divisors:
            numbers_with_max_divisors.append(key)

    return [len(number_list), len(primes), [max_divisors, sorted(numbers_with_max_divisors)]]


def rot13(message: str) -> str:
    alphabets = string.ascii_lowercase



if __name__ == '__main__':
    arr1 = [66, 36, 49, 40, 73, 12, 77, 78, 76, 8, 50,
            20, 85, 22, 24, 68, 26, 59, 92, 93, 30]

    arr2 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445,
            67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379, 35673]

    print(function_num(arr2))
    print(function_num(arr2))
