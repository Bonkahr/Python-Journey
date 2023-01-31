def move_zeroes(arr: list) -> list:
    n_zeroes = arr.count(0)
    if 0 < n_zeroes < len(arr):
        for n in range(n_zeroes + 1):
            arr.remove(0)
            arr.append(0)
    return arr


# print(move_zeroes([1, 0, 1, 2, 0, 1, 3])) print(move_zeroes([9, 0, 0, 9, 1,\
# 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def next_square(square: int) -> int:
    return (int(square ** 0.5) + 1) ** 2 if (square ** 0.5).is_integer() \
        else -1


# print(next_square(5))
# print(next_square(4))


def binary(arr: list) -> int:
    return int(''.join([str(s) for s in arr]), 2)


# print(binary([1, 0, 1, 1, 0, 1]))


def anagram(word: str, arr: list) -> list:
    return [words for words in arr if sorted(words) == sorted(word)]


#
# print(anagram('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# print(anagram('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# print(anagram('laser', ['lazing', 'lazy',  'lacer']))


def prime(n) -> bool:
    if n > 1:
        for s in range(2, int(n ** 0.5) + 1):
            if n % s == 0:
                return False
        return True
    return False


# print(prime(4))

def namelist(names: list) -> str:
    if len(names) == 1:
        for key, name in names[0].items():
            return name
    elif len(names) == 2:
        return ' & '.join([name for item in names for key, name in item.items()])
    elif len(names) == 0:
        return ''
    all_names = [name for item in names for key, name in item.items()]
    first_names = [name for i, name in enumerate(all_names) if i < len(all_names) - 2]
    last_names = all_names[len(all_names) - 2:]
    return f"{', '.join(first_names)}, {' & '.join(last_names)}"


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([]))
print(namelist([{'name': 'Bart'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))

