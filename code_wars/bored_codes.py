import string


def small_abs(n: int) -> int:
    no_zeros = [n for n in str(abs(n)) if n != '0']
    zero_counts = str(n).count('0')
    n_str = sorted([n for n in no_zeros], reverse=False)
    if zero_counts > 0:
        inserted = '0' * zero_counts
        n_str.insert(1, inserted)
        # n_str.append(inserted)
    if len(str(n)) == 2 and str(n)[-1] == '0':
        return n
    ans = int(''.join(str(n) for n in n_str))
    return ans if n > 0 else -ans


def base64_base10(s: str) -> int:
    alphas = string.ascii_uppercase + string.ascii_lowercase + \
        ''.join(str(n) for n in range(10)) + '+/'
    decimal_s_list = []
    k = len(s) - 1
    for i in s:
        decimal_s_list.append(alphas.index(i) * 64 ** k)
        k -= 1
    return sum(decimal_s_list)


if __name__ == '__main__':
    print(small_abs(-46700))
    print(base64_base10('adc'))
