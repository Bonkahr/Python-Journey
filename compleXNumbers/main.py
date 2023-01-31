import cmath

z1 = complex(2.8614, 4.07233)
z0 = complex(8.5842, 12.217)

line_length = 9.5

kn = ((z0 - z1) / (3 * z1))
print(abs(kn))
kn = abs(kn)

_20 = (z1 * (1 + kn)) * 0.2
_60 = (z1 * (1 + kn)) * 0.6
# _80 = z1.real * (1 + kn) * 0.8

# print(_20, _60, _80)

# print(kn)
# print((cmath.polar(kn)))
# print(abs(kn))


