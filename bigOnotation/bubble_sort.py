def bubble_sort(data: list) -> None:
    """
    Sorts a list in place
    :param data: list
    :return: None
    """
    n = len(data)
    comparison_count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        print(f'End of pass {i}. "data" is now {data}')
    print(f'comparison_count is {comparison_count}')


number = [3, 2, 4, 1, 5, 7, 6]
bubble_sort(number)
