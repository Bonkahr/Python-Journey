import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]


def spamless_loop():
    result = []
    for meal in menu:
        if "spam" not in meal:
            result.append(meal)
    return result


def spamless_comp():
    meals = [meal for meal in menu if 'spam' not in meal]
    return meals
# the code above filters and an else statement cant be added to the if condition


# using filter to achieve the above, you have to create a function to do that


def not_spam(meal_list: list):
    return 'spam' not in meal_list


def spam_less_filter():
    spam_less_meals = list(filter(not_spam, menu))
    return spam_less_meals


if __name__ == '__main__':
    timer_1 = timeit.timeit(spamless_loop, number=10000)
    timer_2 = timeit.timeit(spamless_comp, number=10000)
    timer_3 = timeit.timeit(spam_less_filter, number=10000)

    print(f'for loop: {timer_1} -> comp: {timer_2} -> filter: {timer_3}')
