def get_words(file: str, common_words: list) -> dict:
    """
    Reads each word in a file and returns a dictionary of the
    number of times each word occurs in a file, ignoring all
    words contained in the list of common_words. This function
    should be case-insensitive.
    Input:
    filename (string): name of file to be processed
    common_words (list of strings): list of words to be ignored
    Returns:
    word_counts (dict: string -> int): dict containing the # of
    times each word appears
    :param file: string
    :param common_words: list
    :return: dict
    """

    file_contents = [f.lower() for f in file.split(' ') if f]
    words = [w for w in file_contents if w not in common_words]
    return {w: words.count(w) for w in words}


def get_n_words_frequent(words_count: dict, n: int) -> list:
    """
    Returns a sorted list containing tuples corresponding to the n
    words that have the highest counts in the word_counts dictionary.
    Each tuple should be formatted (word, word_frequency), where
    word is a string and word_frequency is an int. Output list is
    sorted in descending order.
    Input:
    word_counts (dict: string -> int): dict containing the # of
    times each word appears
    n (int): number of word tuples to return
    Returns:
    most_frequent_words (list of tuples): sorted list of the most
    frequent tuples of
    (word, word_frequency)
    :param words_count: dict
    :param n: int
    :return: tuple
    """

    tuple_list = []
    for key, num in words_count.items():
        if num >= n:
            tuple_list.append((key, num))
    # TODO ordering the returned dict in descending order of the values.
    ordered_l_tuples = [tuple_list[0]]

    return ordered_l_tuples


if __name__ == '__main__':
    sentence = 'hello and welcome  to our hello    Hello to Welcome pull pull ' \
               'pull pull '
    c_words = ['and', 'to']
    print(get_words(sentence, c_words))
    print(get_n_words_frequent(get_words(sentence, c_words), 2))
