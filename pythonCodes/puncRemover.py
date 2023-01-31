import getpass


def remove_punctuations(sentence: str):
    return ''.join(char for char in sentence if char.isalnum() or char.isspace())


def count_words(sentence: str):
    words_count = {}
    words = [''.join(char for char in word if char.isalnum()) for word in
             sentence.split()]
    for word in words:
        words_count[word] = words.count(word)

    dict_words = 0
    for _, item in words_count.items():
        dict_words += item

    print(len(sentence.split()) == dict_words)
    return words_count


def pass_inputs(user_pass=None):
    user_name = getpass.getuser()
    password = getpass.getpass(f'Input password for {user_name}:')
    counter = 1
    while counter < 3:
        if password != user_pass:
            password = getpass.getpass('Incorrect Password! Try again.')
            counter += 1
        else:
            print('You are logged in.')
            break


if __name__ == '__main__':
    print(remove_punctuations("Hello! every]one do9'you know who am i??"))
    print(count_words("when i was young, my young sister was also young at 9 "
                      "years, while my neighbour sister was also young at 9"))
    pass_inputs()
