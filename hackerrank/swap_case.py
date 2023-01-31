def swap_case(s: str) -> str:
    return ''.join(letter.lower() if letter == letter.capitalize() else letter.capitalize() for letter in list(s))


def mutate_string(string, position, character):
    return string[:position] + character + string[position:]


def magnitude(k: (list, list), m: int) -> float:
    totals = 0
    for l in k:
        totals += max(l) ** 2
    return totals % 1000


if __name__ == '__main__':
    word = 'Www.HackerRank.com'
    print(swap_case(word))
