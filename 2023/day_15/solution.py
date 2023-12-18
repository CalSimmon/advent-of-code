from contextlib import suppress
from functools import reduce
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Since it's a single line, separate by comma and return 
    return data.strip().split(',')

def hash_algorithm(value, char):
    # The hash algorithm that is the previous value plus the ascii value of the character multiplied by 17 and modulo of 256
    return ((value + ord(char)) * 17) % 256

def part1(parsed_data):
    # Just use the reduce function to use the hash algorithm on every entry in the input
    return sum([reduce(hash_algorithm, list(entry), 0) for entry in parsed_data])

def part2(parsed_data):
    # Create a hashmap, add each entry into their respective hash algorithm'd box, and then delete if it ends in -
    hashmap = {}
    for entry in parsed_data:
        with suppress(KeyError):
            match entry.strip('-').split('='):
                case [ls, fl]: hashmap.setdefault(reduce(hash_algorithm, ls, 0), {})[ls] = fl  # Use setdefault to add an empty nested dict if one doesn't exist already
                case [ls]: del hashmap[reduce(hash_algorithm, entry[:-1], 0)][entry[:-1]]  # Suppress ignores KeyError if the key hasn't shown up yet
    
    # Return the sum of the hashmap using the (box_number + 1) * (position) * (value) formula in the prompt
    return sum([(key + 1) * (idx + 1) * int(hashmap[key][sub_key]) for key in hashmap for idx, sub_key in enumerate(hashmap[key]) if hashmap[key]])

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())
    answer1 = part1(parsed_data)
    answer2 = part2(parsed_data)

    print("--- ANSWERS ---")
    print(f"PART1 - The sum of the HASH algorithm is {answer1}")
    print(f"PART2 - The focusing power of this configuration is {answer2}")