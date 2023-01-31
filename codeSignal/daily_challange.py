def solution(prices, notes, x):
    req = [n.split()[:2] for n in notes]
    print(req)
    percentages = [n[0] if n[1].lower() == 'higher' else '-' + n[0] for n in
                   req]
    print(percentages)

    pay = 0
    for i, n in enumerate(percentages):
        try:
            pay += (float(n[:-1]) / 100) * prices[i]
        except ValueError:
            pass

    print(pay)
    return True if pay <= x else False


if __name__ == '__main__':
    price = [110, 110, 110, 110, 110, 110, 110, 110, 110, 160]
    note = ["10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "10.0% higher than in-store",
            "60.0% higher than in-store"]
    print(solution(price, note, 150))
