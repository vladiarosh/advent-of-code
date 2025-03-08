from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_18_input.txt')
    file = open(file_path)
    grid = file.read()
    file.close()

    grid_padded_with_zeros = pad_grid_with_zeros(grid)
    one_dim_list_grid = list(grid_padded_with_zeros.replace('\n', ''))

    # For Part one answer, deactivate next  3 rows of code
    lights_stuck_in_on_state = [103, 202, 10300, 10201]  # These are indices of input grid corners
    for k in lights_stuck_in_on_state:
        one_dim_list_grid[k] = '#'
    # Empty grid to start tracking changes to lights on each iteration
    new_grid = ['0'] * len(one_dim_list_grid)
    for i in range(100):
        for index, char in enumerate(one_dim_list_grid):
            # For Part one answer, deactivate next  3 rows of code
            if index in lights_stuck_in_on_state:
                new_grid[index] = '#'
                continue
            if char != '0':
                current_window = [one_dim_list_grid[index - 103], one_dim_list_grid[index - 102],
                                  one_dim_list_grid[index - 101], one_dim_list_grid[index - 1],
                                  one_dim_list_grid[index + 1],
                                  one_dim_list_grid[index + 101], one_dim_list_grid[index + 102],
                                  one_dim_list_grid[index + 103]]
                sum_sharps = current_window.count('#')

                if char == '#':
                    if sum_sharps == 2 or sum_sharps == 3:
                        new_grid[index] = '#'
                    else:
                        new_grid[index] = '.'
                if char == '.':
                    if sum_sharps == 3:
                        new_grid[index] = "#"
                    else:
                        new_grid[index] = '.'

        one_dim_list_grid = new_grid[:]  # Update the grid after each iteration

    total_sharps = one_dim_list_grid.count("#")
    print('Total number of lights on is', total_sharps)


# I pad the whole grid with one layer of zeros to always use the same indexing for window of neighboring lights
def pad_grid_with_zeros(string_grid):
    rows = string_grid.splitlines()
    padded_rows = ['0' + row + '0' for row in rows]
    padded_grid = ['0' * len(padded_rows[0])]
    padded_grid.extend(padded_rows)
    padded_grid.append('0' * len(padded_rows[0]))
    return '\n'.join(padded_grid)


if __name__ == "__main__":
    main()

