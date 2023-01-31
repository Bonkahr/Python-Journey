font = "The Quick Brown Fox Jumps Over the Lazy Dog"
letters = sorted(font)
print(letters)

# sorting without caring of capitals

letters_new = sorted(font, key=str.casefold)
del letters_new[0: 8]
print(letters_new)
