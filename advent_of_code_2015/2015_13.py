import itertools
from utils import get_input_path


def main():
    # Part one
    file_path_1 = get_input_path(__file__, '2015_13_input.txt')
    instruction = open(file_path_1)
    happiness_dictionary = {}
    for line in instruction:
        line = line.rstrip()
        parse_instructions(line, happiness_dictionary)
    instruction.close()

    guests = list(happiness_dictionary.keys())
    guests_permutations = itertools.permutations(guests)
    total_happiness_variations = []
    for perm in guests_permutations:
        net_happiness = calculate_total_happiness(perm, happiness_dictionary)
        total_happiness_variations.append(net_happiness)
    print("The value of the most optimal happiness configuration is", max(total_happiness_variations))

    # Part two
    file_path_2 = get_input_path(__file__, '2015_13_input_2.txt')
    instruction_2 = open(file_path_2)
    happiness_dictionary_2 = {}
    for line in instruction_2:
        line = line.rstrip()
        parse_instructions(line, happiness_dictionary_2)
    instruction.close()

    guests_2 = list(happiness_dictionary_2.keys())
    guests_permutations_2 = itertools.permutations(guests_2)
    total_happiness_variations_2 = []
    for perm in guests_permutations_2:
        net_happiness_2 = calculate_total_happiness(perm, happiness_dictionary_2)
        total_happiness_variations_2.append(net_happiness_2)
    print('The value of the most optimal happiness configuration including me is', max(total_happiness_variations_2))


def parse_instructions(line, adjacency_list):
    instruction_elements = line.split()
    name1, name2 = instruction_elements[0], instruction_elements[10].replace('.', '')
    if instruction_elements[2] == 'gain':
        happiness = int(instruction_elements[3])
    else:
        happiness = -int(instruction_elements[3])
    if name1 not in adjacency_list:
        adjacency_list[name1] = []
    adjacency_list[name1].append((name2, happiness))


def calculate_total_happiness(permutation, adjacency_list):
    total_happiness = 0
    number_of_guests = len(permutation)
    for i in range(number_of_guests):
        name1 = permutation[i]
        next_guest = permutation[(i + 1) % number_of_guests]
        prev_guest = permutation[(i - 1) % number_of_guests]
        # Calculate happiness contribution from next guest
        for neighbor, happiness in adjacency_list[name1]:
            if neighbor == next_guest:
                total_happiness += happiness

        # Calculate happiness contribution from previous guest
        for neighbor, happiness in adjacency_list[name1]:
            if neighbor == prev_guest:
                total_happiness += happiness
    return total_happiness


if __name__ == "__main__":
    main()

