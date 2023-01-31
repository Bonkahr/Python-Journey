def solve(s):
    if len(s.split()) <= 2:
        return ' '.join(n.capitalize() for n in s.split())
    else:
        f_name, l_name = s.split()[0].capitalize(), s.split()[-1].capitalize()
        return f"{f_name} {' '.join(s.split()[1:-1])} {l_name}"


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


if __name__ == '__main__':
    print(solve('heading north'))
    name = 'jane francis micheal francis'
    print(solve(name))
    print('f13asd'.capitalize())

    print('*' * 23)

    print(is_leap(200))
