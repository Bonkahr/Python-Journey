# the comprehensions works with any iterable data: lists, strings,
# dictionaries or sets

squares = [number * number for number in range(1, 20)]

print(squares)

text = 'When will you be a real python developer?'

title = [word.title() for word in text.split(' ')]

print(title)


