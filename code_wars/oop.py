name = 'James'
s_name = name

name = 'Martin'

print(name)
print(s_name)

n = [1, 2, 3, 4]
m = n

n.append(5)
print(m)

t = (1, 2, 3, 4)
s = t

t = (1, 3)
print(s)


d = {
    1: 34,
    2: 45,
    3: 98,
}

e = d

d[1] = 78

print(e)
