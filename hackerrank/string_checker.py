def string_checker(s) -> None:
    query = {
        'alphanum': False,
        'alpha': False,
        'digit': False,
        'lower': False,
        'upper': False,
    }

    for char in s:
        if char.isalnum():
            query['alphanum'] = True
            break

    for char in s:
        if char.isalpha():
            query['alpha'] = True
            break

    for char in s:
        if char.isdigit():
            query['digit'] = True
            break

    for char in s:
        if char.islower():
            query['lower'] = True
            break

    for char in s:
        if char.isupper():
            query['upper'] = True
            break

    for _, value in query.items():
        print(value)


if __name__ == '__main__':
    string_checker('qA2')
