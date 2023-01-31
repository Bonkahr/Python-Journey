data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("melon", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]


# get ascii int for chars
# print(ord('a'))
# print(ord('c'))
# print(ord('f'))
# print(ord('z'))


def simple_hash(s: str) -> int:
    """
    Create a simple hash code calculator, the function takes the first letter
    from the passed string, gets its ascii code and finds it 10 modulo
    :param s: string
    :return: int
    """
    return ord(s[0]) % 10


def get(k: str):
    """
    Return  the value for a key, or None if the key doesnt exist
    :param k: str
    :return: str or None
    """
    if len(k) > 0:
        hash_code = simple_hash(k)
        if value[hash_code]:
            return values[hash_code]
        else:
            return None
    return None


keys = [''] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)  # python built in hash function
    print(f'key: {key} -> value: {value}')

    keys[h] = key
    values[h] = value


print(keys)
print(values)
print('=' * 80)
print(get('grape'))
print(get('apple'))
print(get('animal'))    # the hashcode for animal is the same as that of
# apple coz we are just checking the first char.


