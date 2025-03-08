from utils import get_input_path

file_path = get_input_path(__file__, '2015_08_input.txt')
with open(file_path) as file:
    instructions = [line.rstrip() for line in file]

# Part one

total_characters_in_memory = 0
literal_length = 0
for line in instructions:
    literal_length += len(line)
    i = 1
    while i < len(line) - 1:
        if line[i] == '\\':
            if line[i + 1] == 'x':
                i += 3
            else:
                i += 1
        total_characters_in_memory += 1
        i += 1

print('Part one result is:', literal_length - total_characters_in_memory)

# Part two

length_of_encoded_representation = 0
for line in instructions:
    encoded_line = '"'
    for character in line:
        if character == '"' or character == '\\':
            encoded_line += '\\' + character
        else:
            encoded_line += character
    encoded_line += '"'
    length_of_encoded_representation += len(encoded_line)

print('Part two result is:', length_of_encoded_representation - literal_length)
