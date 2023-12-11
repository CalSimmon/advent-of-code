import re
import copy
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Create a bool map for easy identification of empty rows and columns, and create a list of all galaxy points
    # Return a tuple of bool_map and galaxy_points
    bool_map = [[False if symbol == '.' else True for symbol in line]for line in data.splitlines()]
    galaxy_points = [[galaxy.start(), idx] for idx, line in enumerate(data.splitlines()) for galaxy in re.finditer('#', line)]
    return (bool_map, galaxy_points)

def expand_universe(bool_map, galaxy_points, distance):
    # Search through the bool map vertically and horizontally and find the index for all rows and columns that have no galaxies 
    # Based on those indices, update all galaxy points that fall after each of the indices based on the distance provided
    # Return the updated galaxy_points list
    ex_row = []
    ex_column = []
    for idx, row in enumerate(bool_map):
        if not any(row):
            ex_row.append(idx)
    for idx, column in enumerate(list(rows) for rows in zip(*bool_map)):  # Use zip() to create a column list
        if not any(column):
            ex_column.append(idx)
    counter = 0
    for item in ex_row:  # Increase the y value by distance if higher than item
        for point in galaxy_points:
            if point[1] > (item + counter):  # Be sure to add counter so the next iteration is accurate to the new value
                point[1] += distance
        counter += distance
    counter = 0
    for item in ex_column:  # Increase the x value by distance if higher than item
        for point in galaxy_points:
            if point[0] > (item + counter):  # Be sure to add counter so the next iteration is accurate to the new value
                point[0] += distance
        counter += distance
    print(f"The galaxy expanded vertically by {len(ex_row) * distance} and horizontally by {len(ex_column) * distance}")

    return galaxy_points

def find_total(expanded_universe):
    total = 0
    for idx, point in enumerate(expanded_universe):
        for next_point in expanded_universe[(idx + 1):]:
            distance = abs(next_point[1] - point[1]) + abs(next_point[0] - point[0])
            total += distance
    return total

def part1(parsed_data):
    galaxy_map_copy = copy.deepcopy(parsed_data[1])  # Have to use copy.deepcopy to ensure we don't accidentally edit the original galaxy_point list
    return find_total(expand_universe(parsed_data[0], galaxy_map_copy, 1))

def part2(parsed_data):
    galaxy_map_copy = copy.deepcopy(parsed_data[1].copy())  # Have to use copy.deepcopy to ensure we don't accidentally edit the original galaxy_point list
    return find_total(expand_universe(parsed_data[0], galaxy_map_copy, 999999))  # The instructions say "replaced" so we are only actually adding 999,999 sections


if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total sum of the distance between each galaxy is {answer1}")
    print(f"PART2 - The total sum of the distance between the extremely old galaxy is {answer2}")