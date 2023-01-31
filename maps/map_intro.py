text = 'What have the Luos ever done to us'

capitals = [char.upper() for char in text]
print(capitals)

# Map version

map_capitals = list(map(str.upper, text))
print(map_capitals)


words_capital = [word.upper() for word in text.split(' ')]
print(words_capital)

# map version

map_word_capitals = list(map(str.upper, text.split(' ')))
print(map_word_capitals)


# while using a function as an argument, you dont include ()
