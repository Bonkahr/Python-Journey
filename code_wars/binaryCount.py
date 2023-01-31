def count_bits(n: int) -> int:
    binary_count = bin(n).count('1')
    while len(str(binary_count)) != 1:
        binary_count = bin(int(binary_count)).count('1')
    return binary_count if len(str(n)) > 1 else n


print(count_bits(9))
print(count_bits(98893457783110947374487))


def sort_vowels(s: str):
    try:
        return "\n".join(
            [f'|{char}' if char.lower() in 'aeiou' else f'{char}|' for
             char in s])
    except TypeError:
        return ''


print(sort_vowels('Code Wars'))


def page_numbers(pages: int) -> int:
    pass
