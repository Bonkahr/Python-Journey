def solution(arr: list) -> str:
    new_arr = []
    for i, n in enumerate(arr):
        if i > 0:
            if arr[i] - 1 == arr[i - 1]:
                continue
            else:
                new_arr.append(('-', str(arr[i - 1]), str(n)))
    new_arr.pop(0)
    print(new_arr)
    trial = []
    q = ''
    # for i, que in enumerate(new_arr):
    #     if i < len(new_arr) - 1:
    #         if new_arr[i] == '-':
    #             q += new_arr[i - 1]
    #         else:
    #             trial.append(q)
    #             trial.append(que)

    # print(', '.join(trial))


test = [
    -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20
]

print(solution(test))

# print('-6'.isdigit())
