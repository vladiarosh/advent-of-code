# version 1 with O(2n)
file = open('2015_1_input.txt')
my_instructions = file.read()
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
