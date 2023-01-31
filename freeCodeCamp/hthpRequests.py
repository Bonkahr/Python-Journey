from urllib import request, parse, error


# using urllib library

f_hand = request.urlopen('https://ketraco.co.ke')
with open('ketraco.html', 'w') as text:
    for line in f_hand:
        text.write(line.decode().strip() + '\n')
