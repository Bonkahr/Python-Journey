import my_functions

print(my_functions.multiply())

word = input("Enter your word: ")

if my_functions.is_palindrome(word):
    print("'{}'- is palindrome".format(word))
else:
    print("'{}'- is not palindrome".format(word))


sentence = input("Entre a sentence: ")

if my_functions.palindrome_sentence(sentence):
    print("'{}'- is palindrome".format(sentence))
else:
    print("'{}'- is not palindrome".format(sentence))

number = input("entre a user_number: ")

print(my_functions.is_numeric(number))


