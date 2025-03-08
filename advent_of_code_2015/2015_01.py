from utils import get_input_path
# PART ONE
# version 1 with O(2n)
file_path = get_input_path(__file__, '2015_01_input.txt')
file = open(file_path)
my_instructions = file.read()
file.close()
floor_up_count = my_instructions.count('(')
floor_down_count = my_instructions.count(')')
floor_total_count = floor_up_count - floor_down_count
print("Your floor is", floor_total_count)

# version 2 with O(n)
floor_total_count = 0
for char in my_instructions:
    if char == '(':
        floor_total_count += 1
    else:
        floor_total_count -= 1
print("Your floor is", floor_total_count)

# PART TWO, learning how enumerator works, writing conditions in for loops correctly, breaking for loops
floor_total_count = 0
for i, char in enumerate(my_instructions, 1):
    if char == '(':
        floor_total_count += 1
    else:
        floor_total_count -= 1
        if floor_total_count == -1:
            print("Position of the basement floor is", i)
            break
