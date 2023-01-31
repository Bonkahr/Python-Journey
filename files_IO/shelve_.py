import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['Orange'] = "a sweet, orange , citrus fruit"
    fruit['Apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    # fruit.clear()

    for key in fruit:
        print(key, ': ', fruit[key])

    # print(fruit['lim'])
    # print(fruit['grape'])
    # print(fruit)
