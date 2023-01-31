import re

string = 'qwerty12345'
numbers = int(re.findall(r'\d+', string)[0])

print(numbers)

string = '12345'

print(re.findall(r'^\d+$', string))

string = "abc123xyz456_0"

# matches any string of chars with the numbers not starting with zero
print(re.findall(r'[1-9]\d*|0', string))

# email matching

email = 'karanja@gmail.com'
email1 = 'karanja@kenya.co.ke'

matcher = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
print(re.findall(matcher, email1))
print(re.findall(matcher, email))
k = re.fullmatch(matcher, email)
print(k)
print('*' * 70)
print(re.search(matcher, email1)[0])
