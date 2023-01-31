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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print('=' * 70)
meals = [meal for meal in menu if 'spam' not in meal]
# the code above filters and an else statement cant be added to the if condition

print(meals)

# add an else clause in comprehension
# filter is removed and condition put in comprehension
# if must be followed by an else and vice-varsa

meals = [meal if 'spam' not in meal else 'A meal skipped' for meal in menu]
