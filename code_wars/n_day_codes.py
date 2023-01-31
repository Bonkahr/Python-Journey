import re
import string


def maskify(cc: str) -> str:
    return ''.join('#' if i < len(cc) - 4 else l for i, l in enumerate(cc))


# print(maskify('SF$SDfgsd2eA'))


def wub(word: str) -> str:
    n = len(word)
    return re.sub(",{1,10}", " ", ','.join(re.split('WUB',
                                                    word))).strip(' ')


print(wub("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(wub("AWUBBWUBC"))
print(wub("AWUBWUBWUBBWUBWUBWUBC"))


def bouncing_ball(h: float, b: float, w: float) -> int:
    if 0 < h > w and 1 > b > 0:
        seen = 1
        h *= b
        while h > w:
            h *= b
            seen += 2
        return seen
    return -1


#
# print(bouncing_ball(3, 0.66, 1.5))
# print(bouncing_ball(30, 0.75, 1.5))


def high(x: str) -> str:
    chars_sum = []
    for s in x.split():
        char_sum = 0
        for c in s:
            char_sum += string.ascii_lowercase.index(c) + 1
        chars_sum.append(char_sum)
    return x.split()[(chars_sum.index(max(chars_sum)))]


# print(high('what time calnovo are we climbing up the volcano'))
# print(high('aa b'))


def find_missing_letter(chars):
    alphas = string.ascii_lowercase  # alphabets in lowers cases
    # ranges of alphabets in alphas
    range1, range2 = alphas.index(chars[0].lower()), alphas.index(chars[len(
        chars) - 1].lower()) + 1
    for char in alphas[range1: range2]:
        if char not in ''.join(chars).lower():  # check the char not in the
            # range
            return char if chars[0] == chars[0].lower() else char.capitalize()


#
# print(find_missing_letter('ABCEF'))
# print(find_missing_letter(['O', 'Q', 'R', 'S']))
# print(find_missing_letter(['a','b','c','d','f']))


def solution(s: str) -> list:
    s_list = list(s)
    if len(s_list) % 2 != 0:
        s_list.append('_')
    result = []
    two = ''
    for n in s_list:
        two += n
        if len(two) == 2:
            result.append(two)
            two = ''
    return result


# print(solution("asdfadsfg"))


def add_binary(a, b):
    # add = bin(a + b)
    # print(add)
    # s = re.findall('\d+$', add)
    # print(s)
    return re.findall('\d+$', bin(a + b))


print(add_binary(2, 5))
