from copy import deepcopy
from collections import Counter
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Return a list of columns from the input
    data_list = [''.join(line) for line in list(zip(*data.splitlines()))]
    return data_list

def cycle(curr_map):
    # Run the rotate and tilt four times for the full cycle
    for _ in range(4):
        curr_map = rotate(tilt(curr_map))
    return curr_map

def rotate(curr_map):
    # Reverse all lines and return the columns to simulate a single rotation
    return [''.join(line) for line in zip(*map(reversed, curr_map))]

def tilt(curr_map):
    # Once rotated, move all Os to the left and return the new map
    new_map = deepcopy(curr_map)
    for map_idx, line in enumerate(curr_map):
        line = ''.join(line).split("#")  # Group up all O and . between each #
        line_copy = deepcopy(line)
        for idx, section in enumerate(line_copy):
            if section != '':
                line[idx] = ''.join(sorted(section, reverse=True))  # Sort the O and . reversed to put the rocks on the left
        new_map[map_idx] = '#'.join(line)  # Rejoin the line with #s in between
    return new_map

def load(platform):
    # Get the total load for all rocks reversing the string to simply use index
    return sum(sum(i * (c == "O") for i, c in enumerate(col[::-1], 1)) for col in platform)

def part1(parsed_data):
    # With the load and tilt functions, this is just a simple one move check
    total_load = load(tilt(parsed_data))
    print(f"The total load on the north beams is {total_load}")
    return total_load

def part2(parsed_data):
    # Find the looping index, and use that to cut down on processing time
    # Once you've found the looping index, you can just find the remainder after looping towards one billion, and find the load on that index
    curr_map = deepcopy(parsed_data)
    map_list = [parsed_data]  # Add cycle 0 to the cycles list
    cycles = 1_000_000_000
    counter = 0
    while True:
        curr_map = cycle(curr_map)
        if curr_map in map_list:  # If the cycle is already in the cycle list, you've found the loop
            loop_idx = map_list.index(curr_map)  # Find the first looped map
            loop_len = counter + 1 - loop_idx  # Find the number of cycles between each loop
            print(f"After {counter} cycles, we found a loop starting from cycle {loop_idx} for {loop_len} cycles")
            break
        map_list.append(curr_map)
        counter += 1
    return load(map_list[(cycles - loop_idx) % loop_len + loop_idx])

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The load after one north tilt is {answer1}")
    print(f"PART2 - The north load after one billion cycles is {answer2}")