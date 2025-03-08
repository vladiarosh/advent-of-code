import json
from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_12_input.txt')
    with open(file_path) as file:
        data = json.load(file)
    part_one_result = sum_integers(data)
    print(part_one_result)
    part_two_result = sum_integers_ignore_red(data)
    print(part_two_result)


def sum_integers(data_file):
    sum_of_numbers = 0
    if isinstance(data_file, int):
        sum_of_numbers += data_file
    elif isinstance(data_file, list):
        for item in data_file:
            sum_of_numbers += sum_integers(item)
    elif isinstance(data_file, dict):
        for value in data_file.values():
            sum_of_numbers += sum_integers(value)
    return sum_of_numbers


def sum_integers_ignore_red(data_file):
    sum_of_numbers = 0
    if isinstance(data_file, int):
        sum_of_numbers += data_file
    elif isinstance(data_file, list):
        for item in data_file:
            sum_of_numbers += sum_integers_ignore_red(item)
    elif isinstance(data_file, dict):
        if 'red' in data_file.values():
            return 0
        for value in data_file.values():
            sum_of_numbers += sum_integers_ignore_red(value)
    return sum_of_numbers


if __name__ == "__main__":
    main()

