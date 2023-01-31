import math


def is_valid_IP(ip: str) -> bool:
    sep = ip.count('.')
    if sep < 3 or sep >= 4:
        return False
    ip_list = ip.split('.')
    for n in ip_list:
        for m in n:
            if m.isalpha() or m == " ":
                return False
        if int(n) < 0 or int(n) > 255:
            return False
        elif len(n) > 1:
            if int(n[0]) == 0:
                return False
    return True


# print(is_valid_IP('1.2.5 .255'))
# print(is_valid_IP(''))


def in_array(array1: list, array2: list) -> list:
    array3 = []
    for i in array1:
        for l in array2:
            if i in l:
                array3.append(i)
    array3.sort()
    return list(dict.fromkeys(array3))


a4 = ['live', 'arp', 'arp', 'strong']
a5 = ['lively', 'alive', 'harp', 'sharp', 'armstrong']


# print(in_array(a4, a5))


def likes(like: list) -> str:
    no_of_likes = len(like)
    if no_of_likes == 0:
        return "no one likes this"
    elif no_of_likes == 1:
        return f'{like[0]} likes this'
    elif no_of_likes == 2:
        return f'{like[0]} and {like[1]} like this'
    elif no_of_likes == 3:
        return f'{like[0]}, {like[1]} and {like[2]} like this'
    else:
        n = no_of_likes - 2
        return f'{like[0]}, {like[1]} and {n} others like this'


# print(likes(['james', 'Alex', 'Mark', 'Max', 'John']))


def last_survivor(string: str) -> str:
    ans = list(string)
    abc = list(map(chr, range(97, 123)))  # all letters
    abc.append('a')  # append the first letter at last z - a - b ...

    for f in range(len(string)):
        for i in ans:
            if ans.count(i) >= 2:
                index = abc.index(i)
                ans.remove(i)
                ans.remove(i)
                ans.append(abc[index + 1])

    return "".join(ans)


# print(last_survivor('xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhx'
#                     'tqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh'))


def names(name=" "):
    if name == 'Zach':
        return 18
    return 0


# print(names('Zach'))
# print(names())


def tortoise_race(v1, v2, d):
    time = 0
    if v1 > v2 or v1 == 0 or v2 == 0:
        return None
    while d > 0:
        if d < 0.003:
            break
        time_taken = d / (v2 / 60)
        d = time_taken * (v1 / 60)
        time += time_taken
    time *= 60
    hours = math.floor(time // 3600)
    minutes = math.floor(time // 60) - (hours * 60)
    seconds = math.floor(time - (hours * 3600 + minutes * 60))
    return [math.floor(hours), math.floor(minutes), math.floor(seconds)]


print(tortoise_race(720, 850, 70))
print(tortoise_race(80, 91, 37))
print(tortoise_race(820, 81, 550))


def duplicate_count(string):
    # check = '1234567890abcdefghijklmnopqrstuvwxyz'
    # a = 0
    # for char in check:
    #     count = array.lower().count(char)
    #     if count > 1:
    #         a += 1
    # return a

    duplicates = ''
    for chars in set(string):
        counter = string.lower().count(chars)
        if counter > 1:
            duplicates += chars
    return len(duplicates)

#
# print(duplicate_count('abcde'))
# print(duplicate_count('aabBcde'))
