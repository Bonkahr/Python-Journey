import string


def bits_battle(numbers: list) -> str:
    odds = [odd for odd in numbers if odd % 2 != 0]
    evens = [even for even in numbers if even % 2 == 0 and even != 0]
    odd_ones_count = ''.join(bin(x)[2:] for x in odds).count('1')
    evens_zeros_count = ''.join(bin(x)[2:] for x in evens).count('0')
    if odd_ones_count == evens_zeros_count:
        return 'tie'
    return 'odd wins' if odd_ones_count > evens_zeros_count else 'even wins'


def clean_string(s: str) -> str:
    punctuations = [',', '?', '!', ' ', '.'] + (list(string.ascii_letters))
    return ''.join([x for x in s.lower() if x in punctuations]).capitalize()


def number(bus_stops):
    return sum(x[0] - x[1] for x in bus_stops)


def bonus(arr, s):
    pass


if __name__ == '__main__':
    print(bits_battle([3, 8, 22, 15, 78]))
    print(bits_battle([1, 13, 16]))
    print(clean_string('Ani@23mal]s a1[}r{e} ~#g=£o0o4d.'))
    print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))
    w = string.ascii_letters
    print(w)

    print(type(w))
