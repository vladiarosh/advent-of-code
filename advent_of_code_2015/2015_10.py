from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_10_input.txt')
    with open(file_path) as input_file:
        test_input = input_file.read().strip()
    # n = 40 for Part one, n = 50 for Part two
    n = 40
    result = test_input
    for k in range(n):
        result = look_and_say(result)
    print(len(result))


def look_and_say(input_number):
    result = ""
    i = 0
    while i < len(input_number):
        count = 1
        while i + 1 < len(input_number) and input_number[i] == input_number[i + 1]:
            count += 1
            i += 1
        result += str(count) + input_number[i]
        i += 1
    return result


if __name__ == "__main__":
    main()

