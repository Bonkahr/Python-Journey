import string


def grid(grid_size: int) -> str:
    alphabets = string.ascii_lowercase
    n_loops = 0
    grid_change = grid_size
    result = ''

    for x in range(grid_size):
        alpha_index = n_loops
        for y in range(grid_size):
            if alpha_index > len(alphabets) - 1:
                alpha_index = 0
            else:
                result += alphabets[alpha_index]
                if alpha_index + 1 < grid_change:
                    result += ' '
                alpha_index += 1

        if n_loops + 1 < grid_size:
            result += '\n'
        n_loops += 1
        grid_change += 1

    return result if grid_size >= 0 else None


if __name__ == '__main__':
    print(grid(14))
