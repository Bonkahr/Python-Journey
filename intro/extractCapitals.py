quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

capitals = ""

for char in quote:
    if char.isupper():
        capitals = capitals + char
print(capitals)

for char in range(19, 11, -2):
    print(char)
print("*" * 50)
for number in range(0, 100, 7):
    #if number % 7 == 0:
    print(number)
