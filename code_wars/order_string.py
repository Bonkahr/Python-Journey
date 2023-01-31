def order(s: str) -> str:
    """
    Sorts the words in a sentence depending on the number given in-between the
    sentence in ascending order
    :param s: a sentence with a digit in-between
    :return: sorted words in the sentence
    """
    numbers = [int(char) for w in s.split(' ') for char in w if char.isdigit()]
    word_dict = {w: s.split(' ')[n] for n, w in enumerate(numbers)}
    sorted_words = [word for _, word in sorted(word_dict.items())]
    return ' '.join(sorted_words)


def rankings(arr: list) -> list:
    """
    The function take a list of randomly numbers, then returns a list of
    position it takes when sorted in descending order
    :param arr: list of numbers
    :return: a list of position the number takes
    """
    return [{n: i for i, n in enumerate(sorted(arr, reverse=True), start=1)}[n]
            for n in arr]


def reverse_words(s: str) -> str:
    """
    Reverses the words in a sentence
    :param s: sentence to be reversed
    :return: reversed sentence
    """
    return ' '.join(s.split(' ')[::-1])


def add(num1: int, num2: int) -> int:
    """
    Given two non-negative integers, pad the number with fewer digits with
    leading zeros so each number has same numbers of digits.
    Example: 99 and 621 should return 61110
    :param num1: int number greater than zero
    :param num2: int number greater than zero
    :return: int of the stupid sum
    """
    str_num1, str_num2 = str(num1), str(num2)
    length = max(len(str(num1)), len(str(num2)))
    if len(str(num1)) > len(str(num2)):
        str_num2 = '0' * (length - len(str(num2))) + str(num2)
    else:
        str_num1 = '0' * (length - len(str(num1))) + str(num1)

    total_sum = ''
    for i, n in enumerate(str_num1):
        total_sum += str(int(n) + int(str_num2[i]))
    return int(total_sum)


if __name__ == '__main__':
    sentence = "4of Fo1r pe6ople go3od th5e the2"
    print(order(sentence))
    print(rankings([22, 33, 18, 9, 110, 4, 1, 88, 6, 50]))
    print(reverse_words("hello world!"))
    print(add(99, 621))
