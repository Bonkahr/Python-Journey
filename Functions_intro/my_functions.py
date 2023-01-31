def multiply():
    return 4 * 6


def is_palindrome(word: str) -> bool:
    """
    Get string  from the standard input or from a var.
    Reverses the string and checks whether its same as passed string

    :param word: string
    :return: bool
    """
    return word[::-1].casefold() == word.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Get string from standard input and extract every character from the
    string.
    Finally call the is_palindrome function and compares them.

    :param sentence: string in form of a sentence
    :return: bool
    """
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def is_numeric(prompt: str) -> int:
    """
    Gets a string from stdIN and checks whether its numeric,
    if numeric returns an integer, if not it loops until
    the user enters a numeric number

    :param prompt: user string
    :return: an integer
    """

    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("'{}'- Not valid user_number, try again".format(temp))


def sum_eo(n: int, t: str) -> int:
    sums = 0
    if t == "e":
        for numbers in range(n):
            if numbers % 2 == 0:
                sums += numbers
        return sums
    elif t == "o":
        for numbers in range(n):
            if numbers % 2 != 0:
                sums += numbers
        return sums
    return -1


def sum_even_odd(n: int, t: str) -> int:
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1
    return sum(range(start, n, 2))


def fibonacci(n: int) -> int:
    """
    Return the `n` th fibonacci, for positive integers
    """

    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


