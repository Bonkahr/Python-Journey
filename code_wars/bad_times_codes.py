def group_ints(lst: list, key=0) -> list:
    # YOUR CODE HERE.
    # GOOD LUCK!

    # AND SINCE THIS IS THE INTERNET, HERE IS A CAT:
    #
    #               _ |\_
    #               \` ..\
    #          __,.-" =__Y=
    #        ."        )
    #  _    /   ,    \/\_
    # ((____|    )_-\ \_-`
    # `-----'`-----` `--`

    to_return_list = []
    to_append = []

    for n in range(len(lst)):
        if to_append and n < len(lst) - 1:
            if lst[n - 1] >= key and lst[n] >= key:
                to_append.append(lst[n])
            elif lst[n - 1] <= key and lst[n] <= key:
                to_append.append(lst[n])
            else:
                to_return_list.append(to_append)
                to_append = []
        else:
            to_append.append(lst[n])

    return to_return_list


my_cat = """                   _ |\\_
                   \\` ..\\
              __,.-" =__Y=
            ."        )
      _    /   ,    \\/\\_
     ((____|    )_-\\ \\_-`
     `-----'`-----` `--`"""
print(my_cat)


if __name__ == '__main__':
    print(group_ints([0, 1, 1, 1, 0, 0, 6, 10, 5, 10], 6))
