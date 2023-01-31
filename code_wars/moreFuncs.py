import string


def connotation(s: str) -> bool:
    positive = [d[0].lower() for d in s.split() if d[0].lower() in
                string.ascii_lowercase[:13]]
    negative = [d[0].lower() for d in s.split() if d[0].lower() in
                string.ascii_lowercase[13:]]
    return len(positive) >= len(negative)


print(connotation("A big brown fox caught a bad rabbit"))
print(connotation("Xylophones can obtain Xenon."))
