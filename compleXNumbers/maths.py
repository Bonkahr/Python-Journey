# import numpy, math, cmath
voltage = 132000
tx_power = 23 * 1000000
impedance1 = 9.64
impedance2 = 9.6
# print(f'{((voltage ** 2) / tx_power)}')
resistance1 = ((voltage ** 2) / tx_power) * impedance1
resistance2 = ((voltage ** 2) / tx_power) * impedance2

total_resistance = (resistance1 * resistance2) / (resistance1 + resistance2)
print(f'Total resistance = {total_resistance}')

# line = 2 + 3j
# line1 = 13.45 + 23j
# total_line = line1 + line
# polar = cmath.polar(total_line)
# print(numpy.degrees(polar[1]))
