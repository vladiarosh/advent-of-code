from utils import get_input_path

file_path = get_input_path(__file__, '2015_2_input.txt')
file = open(file_path)
boxes = file.read()
file.close()

lines = boxes.split('\n')
dimensions_split = [row.split("x") for row in lines]

dimensions_split_int = []
for lines in dimensions_split:
    sublist_int = [int(i) for i in lines]
    dimensions_split_int.append(sublist_int)

total_paper_length = 0
for i in dimensions_split_int:
    l = i[0]
    w = i[1]
    h = i[2]
    sides = [l*w, w*h, h*l]
    paper_length = sum(sides)*2 + min(sides)
    total_paper_length += paper_length

print("Elves need to order", total_paper_length, "square feet of paper")

# PART TWO


def find_len(sublist):
    length = len(sublist)
    sublist.sort()
    largest = sublist[length - 1]
    smallest = sublist[0]
    second_smallest = sublist[1]
    return largest, smallest, second_smallest


total_ribbon_length = 0
for i in dimensions_split_int:
    largest, smallest, second_smallest = find_len(i)
    ribbon_length = (2 * smallest + 2 * second_smallest) + largest * smallest * second_smallest
    total_ribbon_length += ribbon_length
print("Elves need to order", total_ribbon_length, "feet of ribbon")
