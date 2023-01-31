LOW = 1
HIGH = 1000


# print("Please think of a user_number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer: int, low: int, high: int) -> int:
    """
    Gets the given high point and low points, then through the `Binary
    Search` it guesses for numbers that may have been guessed.

    :param answer: Guessed user_number
    :param low: Lowest point for the guess
    :param high: Highest point for the guess
    :return: returns an integer guess
    """

    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1


for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))
