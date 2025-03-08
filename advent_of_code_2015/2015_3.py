from utils import get_input_path

file_path = get_input_path(__file__, '2015_3_input.txt')
file = open(file_path)
instruction = file.read()
file.close()
all_houses = []
unique_houses = set()
x = 0
y = 0
unique_houses.add((0, 0))
for char in instruction:
    match char:
        case '>':
            x += 1
        case '<':
            x -= 1
        case '^':
            y += 1
        case 'v':
            y -= 1
    house_position = (x, y)
    unique_houses.add(house_position)
    all_houses.append(house_position)
print("Number of houses that received at least one present is", len(unique_houses))
print("Total number of presents delivered is", len(all_houses))

# PART TWO
santa_unique_houses = set()
robo_santa_unique_houses = set()
santa_unique_houses.add((0, 0))
robo_santa_unique_houses.add((0, 0))
# Coordinates for Robo Santa's positions
x = 0
y = 0
# Coordinates for Santa's positions
j = 0
k = 0
for i, char in enumerate(instruction, 1):
    if i % 2:
        match char:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        robo_house_position = (x, y)
        robo_santa_unique_houses.add(robo_house_position)
    else:
        match char:
            case '>':
                j += 1
            case '<':
                j -= 1
            case '^':
                k += 1
            case 'v':
                k -= 1
        santa_house_position = (j, k)
        santa_unique_houses.add(santa_house_position)
all_unique_houses = santa_unique_houses.union(robo_santa_unique_houses)
print(len(all_unique_houses))
