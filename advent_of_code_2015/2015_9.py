import itertools
from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_9_input.txt')
    instructions = open(file_path)
    adjacency_matrix = {}
    for line in instructions:
        line = line.rstrip()
        parse_instructions(line, adjacency_matrix)
    print(adjacency_matrix)
    cities = list(adjacency_matrix.keys())
    print(cities)
    city_permutations = itertools.permutations(cities)

    list_of_routes = []
    for perm in city_permutations:
        distance = calculate_distance(perm, adjacency_matrix)
        list_of_routes.append(distance)
    # Part one
    print('Part one result: the shortest route is', min(list_of_routes))
    # Part two
    print('Part two result: the longest route is', max(list_of_routes))


def parse_instructions(line, adjacency_list):
    instruction_body = line.split(' = ')
    left_part = instruction_body[0]
    distance = int(instruction_body[1])
    two_nodes = left_part.split( 'to' )
    node1, node2 = two_nodes[0].strip(), two_nodes[1].strip()
    if node1 not in adjacency_list:
        adjacency_list[node1] = []
    adjacency_list[node1].append((node2, distance))
    if node2 not in adjacency_list:
        adjacency_list[node2] = []
    adjacency_list[node2].append((node1, distance))


def calculate_distance(permutation, adjacency_list):
    total_distance = 0
    for i in range(len(permutation) - 1):
        city1 = permutation[i]
        city2 = permutation[i + 1]
        for neighbour, distance in adjacency_list[city1]:
            if neighbour == city2:
                total_distance += distance
                break
    return total_distance


if __name__ == "__main__":
    main()


