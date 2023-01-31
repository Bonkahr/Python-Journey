burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

# equivalent for loop
meals = []
for burger in burgers:
    for topping in toppings:
        meals.append((burger, topping))
print(meals)
print()

# more on nested comp
for nested_meals in [[(burger, topping) for burger in burgers] for topping in
                     toppings]:
    print(nested_meals)

print()
for nested_meals in [[(burger, topping) for topping in toppings] for burger
                     in burgers]:
    print(nested_meals)
