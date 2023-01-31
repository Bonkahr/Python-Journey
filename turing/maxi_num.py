def maxi_number(*args):
    largest = args[0]
    for n in args:
        if n > largest:
            largest = n
    return largest


if __name__ == '__main__':
    print(maxi_number(1, 54, 31, 54, 67, 78, 56, 87, 78))
    print(max(1, 54, 31, 54, 67, 78, 56, 87, 78))
