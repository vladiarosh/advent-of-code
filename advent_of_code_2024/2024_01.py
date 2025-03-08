from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2024_01_input.txt')
    file = open(file_path)
    instructions = file.readlines()
    file.close()

    left_side = []
    right_side = []
    for line in instructions:
        line.rstrip()
        number_pair = line.split()
        left_side.append(int(number_pair[0]))
        right_side.append(int(number_pair[1]))

    left_side_sorted = sorted(left_side)
    right_side_sorted = sorted(right_side)

    sum_of_distances = 0
    similarity_score = 0
    for i, element in enumerate(left_side_sorted):
        distance_between_numbers = abs(right_side_sorted[i] - left_side_sorted[i])
        sum_of_distances += distance_between_numbers
        repeats_on_right_side = right_side_sorted.count(element)
        similarity_score += element * repeats_on_right_side

# Part 1 result
    print('Distance between lists is',sum_of_distances)
# Part 2 result
    print("Similarity score between lists is", similarity_score)


if __name__ == "__main__":
    main()

