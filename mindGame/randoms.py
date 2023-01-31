from random_words import RandomWords, RandomNicknames, RandomEmails, LoremIpsum

rw = RandomWords()
word = rw.random_word()
print(word)

word = rw.random_word('t')
print(word)

words = rw.random_words(letter='u', count=10)
print(words)

# random nicknames
rn = RandomNicknames()
nick = rn.random_nicks(letter='s', gender='m', count=5)
print(nick)

# Random Emails
email = RandomEmails()
print(email.randomMail())
emails = email.randomMails(count=5)
print(emails)

# Lorem Ipsum
li = LoremIpsum()
print(li.get_sentence())
print(li.get_sentences(sentences=3))
print(li.get_sentences_list(sentences=3))
