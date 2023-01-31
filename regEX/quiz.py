import re


def is_sum_of_cubes(string: str):
    numbers = re.findall(r'\d{1,3}', string)
    cubic_s = []
    for s in numbers:
        total = 0
        for n in s:
            total += int(n) * int(n) * int(n)
        if total == int(s):
            cubic_s.append(s)
    totals = 0
    for n in cubic_s:
        totals += int(n)
    if len(cubic_s) > 0:
        return f"{' '.join(cubic_s)} {totals} Lucky"
    return 'Unlucky'


strings = "aqdf&0#1xyz!22[153(777.7747797"
string1 = "&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y " \
          "-721&() "


# print(is_sum_of_cubes(strings))
# print(is_sum_of_cubes(string1))


def to_jaden_case(string: str):
    # result = []
    # for s in string.split():
    #     new_s = s[0].capitalize()
    #     new_s += s[1:len(s)]
    #     result.append(new_s)
    #     new_s = ""
    return ' '.join(
        s.capitalize() for s in string.split())  # [n.title() for n in
    # string.split()])


# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


def spin_words(sentence: str):
    return ' '.join(
        [word if len(word) < 4 else word[::-1] for word in sentence.split()])


# print(spin_words("Hey fellow warriors"))


def descending_order(num: int) -> int:
    alternatively = int(''.join(sorted(str(num), reverse=True)))
    print(alternatively)
    return int(''.join(sorted(str(num)))[::-1])


# print(descending_order(42145))


def duplicate_encode(word: str) -> str:
    return ''.join(['(' if word.lower().count(s) == 1 else ')' for s in
                    word.lower()])


# print(duplicate_encode("v hC@@xzEYeGB(oFWlfmndd sy@Q@wNxAXCuW"))


def count_bits(n: int) -> int:
    return str(bin(n)).count('1')


# print(count_bits(7))


def is_valid_walk(walk: list) -> bool:
    return len(walk) == 10 and walk.count('n') == walk.count('s') and \
           walk.count('e') == walk.count('w')


# print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
# print(is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']))
# print(is_valid_walk(['n', 's', 's', 'w', 'n', 's', 'e', 'w', 'n', 's']))
