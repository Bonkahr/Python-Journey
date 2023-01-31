def smallest(s: int) -> list:
    list_a = list(str(s))
    list_b = sorted(list_a)
    shifted = 0
    i = 0
    for index, number in enumerate(list_b):
        if number != list_a[index]:
            shifted = number
            i = index
            break
    list_a.pop(str(s).index(shifted))
    print(list_a)
    list_a.insert(i, shifted)
    return [int("".join(list_a)), str(s).index(shifted), i]


# print(smallest(261235))
print(smallest(209917))


# print(smallest(123754))
# print(smallest(1234546))


def max_sum(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2


# print(max_sum([10, 14, 2, 23, 19]))


def persistence(num: int) -> int:
    list_num = list(str(num))
    counter = 0
    while len(list_num) > 1:
        ans = 1
        for n in list_num:
            ans *= int(n)
        list_num = list(str(ans))
        counter += 1
    return counter


# print(persistence(999))


def multiple(n, *args):
    sums = 0
    # return sum(que for que in range(2, que) for m in subjects if que % m == 0)

    for n in range(2, n):
        for m in args:
            if n % m == 0:
                sums += n
                break
            # else:
            #     continue
    return sums


# print(multiple(40, 2, 7, 23, 3, 21))


def split_numbers(word_n: str) -> str:
    numbers_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                    'seven', 'eight', 'nine', 'ten']
    string = ''
    word_numbers = []
    for char in word_n:
        string += char
        if string in numbers_word:
            word_numbers.append(string)
            string = ''
    return ' '.join(word_numbers)


print(split_numbers('zeronineoneoneeighttwoseventhreesixfourtwofive'))


def over_the_road(address: int, n: int) -> int:
    return 2 * n + 1 - address


print(over_the_road(3, 5))

