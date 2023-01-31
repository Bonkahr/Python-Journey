def remove_duplicate(s: str) -> str:
    """
    Remove duplicated numbers or letters in a string, and order them in
    ascending oder, works with any separator of 4 none alphanumeric characters
    :param s: string of numbers or string of strings
    :return: Sorted string with duplicates removed
    """
    separator = ''
    for x in s:
        if not x.isalnum():
            separator += x
            if len(separator) == 4:
                break
    sep = []
    for x in separator:
        if x not in sep:
            sep.append(x)
    sep = ''.join(sep)
    string1 = set(s.split(sep))
    string1 = sorted(list(string1))
    try:
        string1 = sorted([int(x) for x in string1])
        return sep.join(str(x) for x in string1)
    except ValueError:
        return sep.join(string1)


if __name__ == '__main__':
    dumps = 'alpha beta beta gamma gamma gamma delta alpha beta beta ' \
            'gamma gamma gamma delta'
    dumps2 = 'alpha beta delta gamma'

    print(remove_duplicate(dumps))
    print(remove_duplicate(dumps2))
    print(remove_duplicate("chicken my was here"))
    print(remove_duplicate("12, 2, 34, 6, 7, 9, 65, 78, 34, 5, 2, 54"))
    print(remove_duplicate("12, 2, 3p4, 6, 7, 9, 65, 78, 34, 5, 2, 54"))
    print(remove_duplicate('alpha/~beta/~beta/~gamma/~gamma/~gamma/~delta'
                           '/~alpha/~beta/~beta'))
