def count_substring(string, sub_string):
    string_l = list(string)
    new_l = []

    while len(string_l) >= len(sub_string):
        word = ''.join(string_l[:len(sub_string)])
        new_l.append(word)
        string_l.remove(string_l[0])
    return new_l.count(sub_string)


if __name__ == '__main__':
    print(count_substring('ABCDCDCDFCD', 'CD'))
    name = 'ui123'
    print(name.isalpha())
    print(name.isalnum())
