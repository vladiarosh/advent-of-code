import re
from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_19_input.txt')
    file = open(file_path)
    lines = file.readlines()
    file.close()
    lines = [line.rstrip().split() for line in lines]
    list_of_replacements, molecule = parse_input(lines)
    tokenized_input_molecule = re.findall(r'[A-Z][a-z]*', molecule)
    list_of_unique_molecules = get_new_molecules(tokenized_input_molecule, list_of_replacements)
    # Part 1 solution
    print('The number of unique molecules made by one change is', len(list_of_unique_molecules))
    steps = calculate_steps(molecule)
    print('The fewest number of steps to get from molecule to "e" is', steps)


def parse_input(list_of_replacements):
    replacement_list = []
    for i, instruction in enumerate(list_of_replacements):
        if not instruction:
            molecule = list_of_replacements[i + 1][0]
            break
        else:
            key = instruction[0]
            value = instruction[2]
            replacement_list.append((key, value))
    return replacement_list, molecule


def get_new_molecules(elements_in_molecule, replacement_list):
    new_molecules_list = []
    for i, element in enumerate(elements_in_molecule):
        for reactant, product in replacement_list:
            if element == reactant:
                new_list_of_elements = elements_in_molecule[:i] + [product] + elements_in_molecule[i + 1:]
                new_molecule = ''.join(new_list_of_elements)
                new_molecules_list.append(new_molecule)
    unique_molecules = set(new_molecules_list)
    return unique_molecules


def count_elements(molecule):
    tokens = re.findall(r'[A-Z][a-z]?', molecule)
    count_rn_ar = tokens.count('Rn') + tokens.count('Ar')
    count_y = tokens.count('Y')
    total_tokens = len(tokens)
    return total_tokens, count_rn_ar, count_y


def calculate_steps(molecule):
    total_tokens, count_rn_ar, count_y = count_elements(molecule)
    steps = total_tokens - count_rn_ar - 2 * count_y - 1
    return steps


if __name__ == "__main__":
    main()








