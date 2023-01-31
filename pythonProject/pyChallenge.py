import random

answer = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

counter = 0
while guess != answer and counter < 5:
    counter += 1
    print("You have {} remaining guesses".format(5 - counter))

    if guess < answer:
        guess = int(input("Please guess higher: "))
    else:
        guess = int(input("Please guess lower: "))

if guess == answer:
    print("You guessed correct!")
