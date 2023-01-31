import math


def luhn_algorithm(number: int) -> str:
    """
    The function verifies the conditions below:
    Starting from rightmost digit and moving left, double every second digit;
    If the new value is greater than 9, replace it with the sum of its digits.
    Sum up all the resulting values.
    The number is valid if (and only if) the checksum is a multiple of 10.
    Compute the check digit of a number.
    Input que [int] must be in Range: 0–10^{30}.
    Output [int]
    The check digit, an integer k (0 ≤ k < 10) such that que * 10 + k is valid.

    TODO -> Final conditions why I couldn't pass the code-war:
    THE CODE MUST NOT BE LONGER THAN 72BYTES. This must use lambdas...will
    visit after learning the topic.
    The code works in the below choice but too large, more than 500Bytes
    :param number:
    :return: array valid or invalid
    """
    #
    if 0 < number < math.pow(10, 30):
        number_string = str(number)
        numbers = ""
        sum_numbers = 0
        for n in range(0, len(number_string)):
            if n % 2 != 0:
                numbers += number_string[n]
            else:
                sum_numbers += int(number_string[n])
        for n in numbers:
            if int(n) < 9:
                sum_numbers += int(n) * 2
            else:
                multiplied = str(int(n) * 2)
                added = int(multiplied[0]) + int(multiplied[1])
                sum_numbers += added
        if sum_numbers % 10 == 0:
            return 'valid'
    return 'invalid'


print(luhn_algorithm(1234_5678_9012_345))


def closestPower(n):
    if n < 4:
        return 4
    else:

        n_sq_root = round(math.sqrt(n))
        
    return n_sq_root * n_sq_root


# print(closestPower(0))
# print(closestPower(9))
# print(closestPower(30))
# print(closestPower(34))
# print(closestPower(123321456654))


def palindrome(string: str) -> str:
    pal = True if string == string[::-1] else False
    return f"Its palindrome {string} -> {pal}"


if __name__ == '__main__':
    print(palindrome('()()'))
    print(palindrome('())('))

