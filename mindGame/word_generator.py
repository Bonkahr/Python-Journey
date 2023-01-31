from random_word import RandomWords


# words = RandomWords()
# l_words = words.get_random_words()
# print(type(l_words))
# print(len(l_words))


def hello(name=None):
    if name is None:
        name = 'Ronny'
    return f'hallo {name}'


print(hello())
print(hello('james'))
x = (format(1.233454, '.2f'))
print(type(x))
