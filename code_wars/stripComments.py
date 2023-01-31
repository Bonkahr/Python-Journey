import re


def solution(string: str, markers: list) -> str:
    matched = re.findall(f'{"".join(markers)}.*\n', string)
    return '  '.join(matched)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))


def title_case(title: str, m_words='') -> str:
    result = [word.title() if word.lower() not in m_words.lower().split() else word.lower() for
              word in title.split()]
    result[0] = title.split()[0].title()
    return " ".join(result)


print(title_case('THE WIND IN THE WILLOWS', 'The In'))
