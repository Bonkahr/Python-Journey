import string
import codecs


def convert_hash_to_array(h: dict) -> list[list]:
    """
    Covert any dict to a list of list consisting of the key and the value
    :param h: the dict
    :return: list of list
    """
    return [[k, v] for k, v in h.items()]


def rot13(message: str) -> str:
    m, k = string.ascii_lowercase[:13], string.ascii_lowercase[13:]
    returned_string = ''
    for let in message:
        if let.isalpha():
            string_index = string.ascii_lowercase.index(let.casefold())
            if let.isupper():
                returned_string += m[k.index(let.casefold())].capitalize()\
                    if string_index >= 13 \
                    else k[m.index(let.casefold())].capitalize()
            else:
                returned_string += m[k.index(let.casefold())] \
                    if string_index >= 13 else k[m.index(let.casefold())]
        else:
            returned_string += let
    # Easier
    # return codecs.encode(message, 'rot13')
    return returned_string


if __name__ == '__main__':
    print(
        convert_hash_to_array(
            {'name': 'Jeremy', 'age': 24, 'role': 'Software Engineer'}
        )
    )

    # print(rot13('b'))
    print(rot13('Hello Everyone'))
    print(codecs.encode('rot13', 'rot13'))
