import random


def not_int(n: str) -> bool:
    try:
        int(n)
        return False
    except ValueError:
        return True


def welcome() -> tuple:
    print("""
    Hello, this is a guessing guessing game. 
    You can choose the range of numbers you want to guess or go default.
    """)
    print("""
    Do you think you are lucky Enough, you only have 5 chances to guess right!! 
    Lucky doesn't require hints,
    Choose "n" for unlucky,
    Different choice assumes you are lucky! 
    """)
    choice = input('>>> ')

    choose = input("Do you want to choose range by your self? y/n >> ")
    if choose == "y":
        minimum = input("Enter the lowest range >> ")
        maximum = input("Enter the maximum range >> ")
        while not_int(minimum) or not_int(maximum) or minimum >= maximum:
            print("Enter valid ranges")
            minimum = input("Minimum >> ")
            maximum = input("Maximum >> ")
        return int(minimum), int(maximum), choice
    print("You choose 'n' or invalid character, your range will be 1 to 100 ")

    return 1, 100, choice


def guessing_game():
    minimum, maximum, lucky = welcome()
    random_number = random.randint(minimum, maximum)
    # print(f'Guessed number = {random_number}')

    guessed_number = input("Enter your guess >>> ")

    while not_int(guessed_number):
        guessed_number = input("Enter your number >>> ")

    if lucky == "n".casefold():
        print("""
        Hello unlucky Guy!!
        
        """)
        counter = 1
        while int(guessed_number) != random_number:
            guessed_number = int(guessed_number)
            if guessed_number < random_number:
                guessed_number = input("Sorry, that was SMALL, try again >>> ")
                while not_int(guessed_number):
                    guessed_number = input("What's wrong, a NUMBER please >> ")
            else:
                guessed_number = input("Sorry, that was BIG, try again >>> ")
                while not_int(guessed_number):
                    guessed_number = input("What's wrong, a NUMBER please >> ")
            counter += 1
            if counter > 4:
                print(f"You are too UNLUCKY, or too DUMB, the answer was -->"
                      f" {random_number}")
                break
        if random_number == int(guessed_number):
            print(f"You guessed correct after {counter} trials")
    else:
        print("""
        LUCKY GUY
        """)
        counter = 1
        while int(guessed_number) != random_number:
            guessed_number = input("That was not correct, try again >> ")
            while not_int(guessed_number):
                guessed_number = input("What's wrong, a NUMBER please >> ")
            if counter >= 4:
                print(f"I guess you thought WRONG, you ain't LUCKY BYE!!! "
                      f"answer was --> {random_number}")
                break
            counter += 1
        if int(guessed_number) == random_number:
            print(f"You won after {counter} trials")


guessing_game()
