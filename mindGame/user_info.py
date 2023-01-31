def user_info() -> list:
    def is_number(to_test: str) -> bool:
        try:
            int(to_test)
            return True
        except ValueError:
            return False

    def keep_trying() -> str:
        return input('Please Enter a valid value > ')

    name = input('Enter your name > ')
    choices = ['Male', 'Female']
    print(f'Choose your gender: \n\t1. {choices[0]} \n\t2. {choices[1]}')
    user_input = input('Enter your choice > ')
    gender = ''

    while True:
        if is_number(user_input):
            if int(user_input) == 1 or int(user_input) == 2:
                gender = choices[int(user_input) - 1]
                break
            else:
                user_input = keep_trying()
                continue
        else:
            user_input = keep_trying()

    user_age = input('Enter your age > ')
    age = 0
    while True:
        if is_number(user_age):
            if 0 < int(user_age) < 100:
                age = int(user_age)
                break
            else:
                print('Age must be between 1 and 100')
                user_age = keep_trying()
                continue
        else:
            user_age = keep_trying()

    return [name, gender, age]


if __name__ == '__main__':
    pass
