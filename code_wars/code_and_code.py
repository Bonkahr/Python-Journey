def remove_duplicates(string: str) -> str:
    result = []
    for s in string.split():
        if s not in result:
            result.append(s)
    return " ".join(result)


print(remove_duplicates("my cat is my cat fat"))


def reverse_array(arr: list) -> list:
    return [r for r in arr[::-1]]


# print(reverse_array([5, 4, 3, 2, 1]))


def reverse_alternate(string: str) -> str:
    return " ".join(
        j if i % 2 == 0 else j[::-1] for i, j in enumerate(string.split()))
    # returned = []
    # for index, words in enumerate(array.split()):
    #     word = words.strip()
    #     if index % 2 == 0:
    #         returned.append(word)
    #     else:
    #         s = word[::-1]
    #         returned.append(s)
    # return ' '.join(returned)


print(reverse_alternate("I really hope it works this time..."))
