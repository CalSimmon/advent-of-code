from math import gcd
from functools import reduce
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Parse input into two sections; the directions and the map key, split the map key into a dictionary of list pairs, and return both in a tuple
    directions, map_key = data.split('\n\n')
    map_key = {line.split(" = ")[0]: line.split(" = ")[1].strip("()").split(', ') for line in map_key.splitlines()}
    return (directions, map_key)

def find_first_z(start_point, data):
    # Brute force method to find the first step that has a Z at the end for the supplied start point
    directions, map_key = data
    curr_element = start_point
    count = 0
    while curr_element[-1] != 'Z':  # This worked fine for part1 so I left it here
        for direct in directions:
            selection = 0 if direct == "L" else 1  # Set left to 0 and right to 1 for list comprehension 
            curr_element = map_key[curr_element][selection]
            count += 1
    print(f"{start_point} takes {count} steps to find it's first Z")
        
    return count

def find_lcm(x, y):
    # Function for finding the least common multiple of two numbers using greatest common divisor function
    return (x * y) // gcd(x, y)

def part1(parsed_data):
    # Just pass AAA into find first Z and boom
    return find_first_z('AAA', parsed_data)

def part2(parsed_data):
    # Find all start points with an A at the end, find the number of steps it takes for each to find their first Z, then find the least common multiple
    start_points = [key for key in parsed_data[1].keys() if key[-1] == 'A']
    first_z = [find_first_z(start_point, parsed_data) for start_point in start_points]
    lcm = reduce(find_lcm, first_z)
    return lcm

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - It takes {answer1} steps to find ZZZ")
    print(f"PART2 - It takes {answer2} steps for all starting points to end up at a Z")