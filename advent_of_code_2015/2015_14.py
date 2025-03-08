import re
from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_14_input.txt')
    instructions = open(file_path)
    reindeer_dict = {}
    for line in instructions:
        line = line.rstrip()
        parse_instructions(line, reindeer_dict)

    distances = {deer_name: 0 for deer_name in reindeer_dict.keys()}
    points = {deer_name: 0 for deer_name in reindeer_dict.keys()}

    for second in range(1, 2504):
        for deer_name, (speed, duration, rest_time) in reindeer_dict.items():

            cycle_time = duration + rest_time
            full_cycles = second // cycle_time
            remaining_time = second % cycle_time

            distance_traveled = full_cycles * duration * speed

            if remaining_time <= duration:
                distance_traveled += remaining_time * speed
            else:
                distance_traveled += duration * speed

            distances[deer_name] = distance_traveled

        max_distance = max(distances.values())

        for deer_name, distance in distances.items():
            if distance == max_distance:
                points[deer_name] += 1
    # Part one solution
    winning_deer = max(distances, key=distances.get)
    print('The winning deer is', winning_deer, 'with a distance of', distances[winning_deer], 'km')

    # Part two solution
    highest_points_deer = max(points, key=points.get)
    print('The reindeer with the most points is', highest_points_deer, 'with', points[highest_points_deer], 'points')


def parse_instructions(line, dictionary):
    match = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    deer_name = match.group(1)
    speed = int(match.group(2))
    duration = int(match.group(3))
    rest_time = int(match.group(4))
    dictionary[deer_name] = [speed, duration, rest_time]


if __name__ == "__main__":
    main()

