import random


def bagel(b):
    """
    Bagels, a deductive logic game.
    :return: none
    """

    print(
        """
        Hello Buddy, welcome to Bagels.
        The computer will generate a 3-digit number (non - repeated), your task 
        is to guess the number:
            * Pico: means your guess has a correct digit in the wrong place.
            * Fermi: your guess has a correct digit in the right place.
            * Bagels: your guess has no correct digit.
        You have at most 10 tries.
        """
    )

    print("""
    *******************************************************************
    *******ON A SCALE OF 1 to 10, HOW SMART DO YOU THINK YOU ARE?******
    *******************1 being smartest and 10 dumbest********************
    *******************************************************************
    """)
    smartness = input('Enter your smartness: ')
    try:
        smartness = int(smartness)
        if smartness <= 3:
            print('You believe in yourself, now lets gauge you.')
        else:
            print('You may be smarter than you think.')
    except ValueError:
        smartness = 10
        print('You are so dumb, anyway continue with the game. Your smartness '
              'has been defaulted to 10.')

    repeated_numbers = 1
    while repeated_numbers > 0:
        secret_number = str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
                        str(random.randint(0, 9))
        # print(secret_number)
        for n in secret_number:
            count = secret_number.count(n)
            if count != 1:
                repeated_numbers += 1
        if repeated_numbers == 1:
            repeated_numbers = 0
        else:
            repeated_numbers = 1

    user_guess = input('Enter your guess: ')

    trials = 1

    while user_guess != secret_number and trials < 10:
        trials += 1
        while len(user_guess) != 3 or not user_guess.isdigit():
            user_guess = input('Your guess should have only three digits, '
                               'try again: ')
        counter = 0
        for i, num in enumerate(user_guess):
            if int(num) == int(secret_number[i]):
                counter += 1
        if counter > 0:
            print('Fermi')

        if counter == 0:
            c = 0
            for num in user_guess:
                if num in secret_number:
                    c += 1
            if c == 0:
                print('Bagels')
            else:
                print('Pico')
        user_guess = input(f'Guess #{trials}: ')

        if smartness + 1 == trials:
            print(
                'You are not as smart as you thought, anyway continue....'
                .upper())

    if user_guess == secret_number:
        print(f"CONGRATS. You got it right with {trials} trials -> "
              f"secret number: {secret_number}.")
        if smartness < 4 and trials < 5:
            print('That was crazy, smart guy.')
        elif smartness > 6 > trials:
            print('You are smarter than you though, good work.')
        else:
            print('That was good.')

    else:
        print(f'Sorry! Run the program again to continue play.\n\t Secret '
              f'number was {secret_number}.')
        if smartness < 4:
            print('You are not smart, You may more dumb than you think.')
        else:
            print('You knew you are dumb, but you may be smarter if you '
                  'practice more.')


if __name__ == '__main__':
    bagel(3)
    print("""
    *********************************************************
    *************Made with love by B.Gakingo*****************
    *********************************************************
    """)
