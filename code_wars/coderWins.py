def filter_list(array: list) -> list:
    """
    Filter strings from the list
    :param array: A list with positive integers and strings
    :return: A list, strings filtered out
    """
    return [s for s in array if type(s) == int]


# print(filter_list([1, 2, 'aasf', '1', '123', 123]))


def find_uniq(arr: list) -> int:
    a = max(arr)
    b = min(arr)
    return a if arr.count(a) < arr.count(b) else b


# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))


def encrypt_this(text: str) -> str:
    """
    Encrypt the text as follows:
    The first letter must be converted to its ASCII code.
    The second letter must be switched with the last letter
    :param text: string_
    :return: encrypted string_
    # """
    # result = []
    # ans = ''
    # for word in text.split():
    #    if len(word) ==
    # return ' '.join(result)


print(encrypt_this("hello world"))
print(encrypt_this('A wise old owl lived in an oak'))
