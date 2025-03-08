import re
from utils import get_input_path


def main():
    file_path_1 = get_input_path(__file__, '2015_16_input.txt')
    file_path_2 = get_input_path(__file__, '2015_16_input_2.txt' )
    aunt_list = open(file_path_1)
    our_aunt_profile = open(file_path_2)
    parsed_aunt_profile = parse_input(our_aunt_profile.read())
    print(parsed_aunt_profile)
    parsed_aunt_list = []

    for line in aunt_list:
        line = line.rstrip()
        parsed_aunt_list.append(parse_input(line))
    print(parsed_aunt_list)

    for index, aunt in enumerate(parsed_aunt_list):
        if match_aunt_profile_with_aunt_list(parsed_aunt_profile, aunt):
            print(f"{index + 1}:{aunt}")


def parse_input(line):
    attributes = re.findall(r'(\w+): (\d+)', line)
    attributes_dict = {}
    for key, value in attributes:
        attributes_dict[key] = int(value)
    return attributes_dict


def match_aunt_profile_with_aunt_list(parsed_profile, parsed_dictionary):
    matched_values = 0
    for key, value in parsed_profile.items():
        if key in parsed_dictionary:
            if key == 'cats' or key == 'trees':
                if parsed_dictionary[key] >= value:
                    matched_values += 1
                else:
                    pass
            elif key == 'pomeranians' or key == 'goldfish':
                if parsed_dictionary[key] <= value:
                    matched_values += 1
                else:
                    pass
            else:
                if parsed_dictionary[key] == value:
                    matched_values += 1
                else:
                    pass
    if matched_values == len(parsed_dictionary):
        return True
    return False


if __name__ == "__main__":
    main()
