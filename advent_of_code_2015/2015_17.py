from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_17_input.txt')
    with open(file_path) as file_data:
        set_of_numbers = [int(line.strip()) for line in file_data]
    target_sum = 150
    subset = []
    valid_combinations = []
    total_numbers_in_set = len(set_of_numbers)
    valid_combinations = calculate_subset_sums(0, total_numbers_in_set, set_of_numbers,
                                               target_sum, subset, valid_combinations)
    # Part one solution
    print('Part 1 solution:', len(valid_combinations))
    shortest_combinations = min(len(i) for i in valid_combinations)

    list_of_shortest_combinations = []

    for i in valid_combinations:
        if len(i) == 4:
            list_of_shortest_combinations.append(i)
    # Part two solution
    print('Part 2 solution:', len(list_of_shortest_combinations))


def calculate_subset_sums(i, n, input_set, desired_sum, current_subset, valid_comb):

    if desired_sum == 0:
        valid_comb.append(current_subset.copy())
        return
    if i == n:
        return
    calculate_subset_sums(i + 1, n, input_set, desired_sum, current_subset, valid_comb)
    if input_set[i] <= desired_sum:
        current_subset.append(input_set[i])
        calculate_subset_sums(i + 1, n, input_set, desired_sum - input_set[i], current_subset, valid_comb)
        current_subset.pop()
    return valid_comb


if __name__ == "__main__":
    main()
