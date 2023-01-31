import math


def nb_months(old_price, new_price, saving, loss):
    if old_price < new_price:
        new_price -= new_price * 0.01 * loss
        old_price -= old_price * 0.01 * loss
        monthly_value = old_price - new_price + saving
        counter = 1
        months = 1
        while old_price >= new_price:
            if counter >= 2:
                loss += 0.5
                counter = 0
            new_price -= new_price * 0.01 * loss
            old_price -= old_price * 0.01 * loss
            monthly_value = old_price - new_price + saving
            months += 1
            counter += 1
        return [months, monthly_value]
    return [0, old_price - new_price]


print(nb_months(2000, 8000, 1000, 1.5))
print(nb_months(12000, 8000, 1000, 1.5))
# print(nb_months(8000, 12000, 500, 1.0))


def calculate_payment(p0, amortization, interest_rate):
    n = amortization * 12
    r = 0.01 * interest_rate / 12
    return float(format(r * (p0 / (1 - math.pow((1 + r), -n))), '.2f'))


print(calculate_payment(200000.0, 30, 6.5))
