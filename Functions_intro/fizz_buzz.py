import my_functions


def fizz_buzz(user_number: int) -> str:
    """
        Get an `integer` from standard input,
        check whether its divisible by `5, 3,
        or both` , then return a string containing either
        `fizz`, `buzz` or `fizz buzz`.

        :param user_number: int from stdIn
        :return: string containing either
        `fizz`, `buzz` , `fizz buzz` or the number string.
        """

    if user_number % 3 == 0 and user_number % 5 == 0:
        return "fizz buzz"
    elif user_number % 5 == 0:
        return "buzz"
    elif user_number % 3 == 0:
        return "fizz"
    else:
        return str(user_number)


input("Play Fizz Buzz. Press entre to continue: ")
print()

next_number = 0

while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))

    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("your go: ")

    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done you reached {}".format(next_number))
