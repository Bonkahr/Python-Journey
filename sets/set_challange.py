# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

string = "i wasn't around"
vowels = frozenset("aeiou")
# vowels =("a", "e", "i", "o", "u")
final_set = sorted(set(string).difference(vowels))
print(final_set)

# string_set = set(string)
# print(string_set.difference(set(vowels)))
# print("".join(string_set))
#
# print(string_set)
