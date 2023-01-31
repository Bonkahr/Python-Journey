def adjacent_elements(arr: list) -> int:
    max_product = 0
    for i in range(1, len(arr)):
        if arr[i - 1] * arr[i] > max_product:
            max_product = arr[i - 1] * arr[i]
    return max_product


if __name__ == '__main__':
    print(adjacent_elements([3, 6, -2, -5, 7, 3]))
    print(adjacent_elements([5, 1, 2, 3, 1, 4]))