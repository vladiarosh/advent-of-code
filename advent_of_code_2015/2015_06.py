import numpy as np
import re
from utils import get_input_path


# Part one
file_path = get_input_path(__file__, '2015_06_input.txt')
with open(file_path) as file:
    instructions = [line.rstrip() for line in file]

x_axis_span = 1000
y_axis_span = 1000
square_grid = np.zeros((x_axis_span, y_axis_span), dtype=np.int32)

for step in instructions:
    list_of_coordinates = re.findall(r"(\d+)", step)
    x1 = int(list_of_coordinates[0])
    x2 = int(list_of_coordinates[2])
    y1 = int(list_of_coordinates[1])
    y2 = int(list_of_coordinates[3])

# Rule of thumb for slicing in Python - first index is included, starting from 0, the last is excluded,
# therefore, +1 at the end
    if "turn on" in step:
        square_grid[x1:x2 + 1, y1:y2 + 1] = 1
    if "turn off" in step:
        square_grid[x1:x2 + 1, y1:y2 + 1] = 0
    if "toggle" in step:
        square_grid[x1:x2 + 1, y1:y2 + 1] = 1 - square_grid[x1:x2 + 1, y1:y2 + 1]
lights_on = square_grid[square_grid == 1]
print('The total number of lights on is', len(lights_on))


# Part two

# Generating new grid for part 2 since the gris in part 1 is already modified, and some values are set to 1
square_grid_2 = np.zeros((x_axis_span, y_axis_span), dtype=np.int32)
# Mostly the same code, but now I am using addition or subtraction
# Also, at the 'turn off' step, I double-check that values do not go below 0 using np.maximum() method
for step in instructions:
    list_of_coordinates = re.findall(r"(\d+)", step)
    x1 = int(list_of_coordinates[0])
    x2 = int(list_of_coordinates[2])
    y1 = int(list_of_coordinates[1])
    y2 = int(list_of_coordinates[3])
    if "turn on" in step:
        square_grid_2[x1:x2 + 1, y1:y2 + 1] += 1
    if "turn off" in step:
        square_grid_2[x1:x2 + 1, y1:y2 + 1] -= 1
        square_grid_2[x1:x2 + 1, y1:y2 + 1] = np.maximum(square_grid_2[x1:x2 + 1, y1:y2 + 1], 0)
    if "toggle" in step:
        square_grid_2[x1:x2 + 1, y1:y2 + 1] += 2


brightness = square_grid_2.sum()
lights_on_2 = square_grid[square_grid >= 1]
print('The combined brightness is', brightness)
print('The total number of lights on for part two is', len(lights_on_2))







