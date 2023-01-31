def arithmetic_arranger(arithmetic, results=False):
    if len(arithmetic) > 5:
        return 'Error: Too many problems.'

    all_numbers = []
    for q in arithmetic:
        if '+' in q:
            n = q.split(' + ')
            n.append('+')
            all_numbers.append(n)
        elif '-' in q:
            n = q.split(' - ')
            n.append('-')
            all_numbers.append(n)
        else:
            return "Error: Operator must be '+' or '-'."

    for numbers in all_numbers:
        for number in numbers[:2]:
            if len(number) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            for digit in number:
                if digit.isalpha():
                    return 'Error: Numbers must only contain digits.'

    totals = []
    for number in all_numbers:
        if '+' in number:
            sums = int(number[0]) + int(number[1])
            totals.append([number[0], '+', number[1], str(sums)])
        else:
            sums = int(number[0]) - int(number[1])
            totals.append([number[0], '-', number[1], str(sums)])

    to_return = ''
    nd_return = ''
    dashes = ''
    to_answers = ''
    for n in totals:
        max_n = max(len(x) for x in n[:3]) + 2
        if len(n[0]) <= len(n[2]):
            to_return += f"{n[0]:>{max_n}}    "
            nd_return += f"{n[1]} {n[2]}    "
        else:
            to_return += f"{n[0]:>{len(n[0]) + 2}}    "
            nd_return += f"{n[1]} {n[2]:>{max_n - 2}}    "

        dashes += ('-' * max_n) + '    '
        to_answers += f'{n[3]:>{max_n}}    '
    result = f'{to_return.rstrip()}\n{nd_return.rstrip()}\n{dashes.rstrip()}'
    return result + f'\n{to_answers.rstrip()}\n{dashes.rstrip()}' if results \
        else result


if __name__ == '__main__':
    print(
        arithmetic_arranger(["32 + 6498", "3801 - 9782", "45 + 43", "123 + "
                                                                    "49",
                             "1234 + 43"]))

    print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
