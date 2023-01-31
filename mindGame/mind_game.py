# from random_word import RandomWords
from random_words import RandomWords, RandomNicknames
import sqlite3 as sq


def save_to_database(name, gender, age, score, percentage_win,
                     words_to_db, guessed_letters) -> str:
    with sq.connect('players.db') as connection:
        cursor = connection.cursor()
        # cursor.execute("CREATE TABLE Players(Name TEXT, Age INTEGER, "
        #                "Gender TEXT, Score INTEGER, Percentage_Win INTEGER, "
        #                "Words_Generated TEXT, Guessed_Words TEXT);")

        player = "INSERT INTO Players VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(player, (name, age, gender, score,
                                percentage_win, words_to_db,
                                guessed_letters))
        return 'Your game record has been saved to the database.'


def generated_names(letter: str, count: int, gender: str) -> list:
    return RandomNicknames().random_nicks(letter=letter, count=count,
                                          gender=gender)


def generated_words(letter: str, count: int) -> list:
    return RandomWords().random_words(letter=letter, count=count)


class MindGame:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def can_play(self):
        if self.age < 8:
            print(f"{self.name} is under 8, hence can't play "
                  f"this game")
            return False
        return True

    def game(self):
        if self.can_play():
            print('''
            **************************************************************
            * This is a word game, you guess will guess names or english *
            * words. You can choose the starting alphabet and gender when* 
            * names is chosen. The computer guesses a word or name,then  *
            * calculates your score depending with the correct letters in*
            * word/name the computer guessed.                            *
            **************************************************************
            ''')
            play = input('\tIf you wish to continue press C, q to quit. \n> '
                         '').capitalize()
            if play == 'C':
                player_times = input('How many times do you wish to play, '
                                     'Enter a number: > ')
                while True:
                    try:
                        int(player_times)
                        break
                    except ValueError:
                        player_times = input('Enter a valid number. > ')

                print('Choose to guess names or english word:>')
                word_to_guess = input("\t1. names \n\t2. english words: \n> ")

                while True:
                    try:
                        int(word_to_guess)
                        break
                    except ValueError:
                        word_to_guess = input('Enter a valid choice, 1 or 1 > ')

                letter = 's'
                gender = 'm'
                play_choice = 'names'

                if int(word_to_guess) == 1:
                    print('Do you want to provide the letter and '
                          'gender for names to guess, if No default '
                          '"s" and gender male will be chosen')
                    query = input('Y/N > ').lower()
                    if query == 'y':
                        letter = input('Enter letter > ')
                        gender = input('Enter gender m/f > ')
                        if letter:
                            try:
                                letter = int(letter)
                                print(
                                    'You chose a number, default s in '
                                    'chosen')
                                letter = 's'
                            except ValueError:
                                letter = letter[0]

                        if gender:
                            gender = gender[0]
                            if gender != 'f' and gender != 'm':
                                print(
                                    "Invalid choice 'm' is chosen by "
                                    "default")
                                gender = 'm'
                else:
                    play_choice = 'words'
                    letter_choice = input('Entre chosen 1st letter > ')
                    try:
                        int(letter_choice)
                        letter_choice = 's'
                    except ValueError:
                        letter = letter_choice[0]

                words_generated = 1
                guessed_words = []

                if play_choice == 'names':
                    all_words = generated_names(letter=letter, count=int(
                        player_times), gender=gender)

                else:
                    all_words = generated_words(
                        letter=letter, count=int(player_times))

                while words_generated <= int(player_times):
                    user_letters = input(f'Guess your {play_choice} '
                                         f'{words_generated}: > ')
                    guessed_words.append(user_letters)
                    words_generated += 1

                total_correct_words = 0
                total_correct_letters = 0
                total_correct_letters_places = 0
                total_letters = sum(len(i) for i in all_words)
                for word in all_words:
                    for name in guessed_words:
                        if word.lower() == name.lower():
                            total_correct_words += 1
                        for n in set(name.lower()):
                            total_correct_letters += word.lower().count(n)
                        if len(name) > len(word):
                            name = name[:len(name) - 1]
                        else:
                            word, name = name.lower(), word.lower()

                        for i, let in enumerate(word, start=0):
                            print(all_words)
                            if name[i] == let:
                                total_correct_letters_places += 1

                print('Thank you for playing the word Game, Here is your '
                      'score.')
                print('Score Calculation.\n\tCorrect words: 100\n\tEach '
                      'correct letter: 5\n\tEach correct letter place: 20')
                score = total_correct_letters * 5 + \
                        total_correct_letters_places * 20 + \
                        total_correct_words * 100

                possible_win = words_generated * 100 + total_letters * 5 + \
                               total_letters * 20
                percentage_win = score / possible_win * 100
                if percentage_win >= 10:
                    print(f'''
                    ********************************************
                            *CONGRATULATIONS {self.name}*
                    ********Less people get more than 10% ******
                    ********************************************
                    ''')
                elif score < 150:
                    print(f'''
                    **********************************************
                        I KNOW ITS A HARD GAME BUT REALLY A {int(percentage_win)}% 
                    **********************************************
                    ''')
                print(f"Correct Words: {total_correct_words}\nCorrect "
                      f"letters: {total_correct_letters}\nCorrect letter "
                      f"places: {total_correct_letters_places}\nTotal Score: "
                      f"{score}\nPossible Win: {possible_win}"
                      f"{score}\nPercentage win: {int(percentage_win)}%")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(f'Words were {all_words}')
                words = ', '.join(all_words)
                guessed_words = ', '.join(guessed_words)
                print(save_to_database(self.name, self.gender, self.age,
                                       score,
                                       float(format(percentage_win, '2f')),
                                       words,
                                       guessed_words))
            else:
                print('Sorry for bothering yourself!')

    def __str__(self):
        return f"User:{self.name}\nGender: {self.gender}\nAge: {self.age}"


if __name__ == '__main__':
    pass
