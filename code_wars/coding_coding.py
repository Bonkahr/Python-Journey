def most_frequent(string: str):
    my_list = [word for word in string.strip().split(" ")]
    result = []
    for item in my_list:
        lst = [char for char in item]
        for char in lst:
            if char.isalnum() or char == "'":
                continue
            else:
                lst.remove(char)
        result.append("".join(lst))

    answer = []
    a = 0
    b = 0
    c = 0

    for item in result:
        d = result.count(item)
        if d > a:
            b = a
            a = d
            answer.insert(0, item)
        elif d > b:
            c = b
            b = d
            answer.insert(1, item)
        elif d > c:
            c = d
            answer.insert(2, item)
        while d != 0:
            result.remove(item)
            d -= 1
    print(answer)


z = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
w = "In a village of La Mancha, the name of which I have no desire to call to " \
    "mind, there lived not long since one of those gentlemen that keep a " \
    "lance in the lance-rack, an old buckler, a lean hack, and a greyhound " \
    "for coursing. An olla of rather more beef than mutton, a salad on most " \
    "nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so " \
    "extra on Sundays, made away with three-quarters of his income. "

v = "  //wont won'tellers won'tellers"
most_frequent(z)
most_frequent(w)
most_frequent(v)


print("/".isalnum())
