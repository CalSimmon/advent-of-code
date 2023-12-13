from functools import cache
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split the lines of the input into the string and the tuple of the groups, and return the list
    data_list = [[line.split()[0], tuple(map(int, line.split()[1].split(',')))] for line in data.splitlines()]
    return data_list

@cache
def find_solutions(springs, sizes, group_size=0):
    # Dynamic programming solution using the cache to significantly speed up the processing
    # Run through each item in the string, if it's a question mark, try all options replacing each with either . or #
    # If the replacement results in a successful line, return one and continue
    if not springs:  # Return 1 if there are no more group sizes and there is no current group
        return not sizes and not group_size
    num_solutions = 0
    symbol = ['.', '#'] if springs[0] == '?' else springs[0]
    for sym in symbol:
        if sym == '#':  # If it's # expand the group
            num_solutions += find_solutions(springs[1:], sizes, group_size + 1)
        else:
            if group_size:  # If the . is at the end of a group and it matches the first size, continue
                if sizes and sizes[0] == group_size:
                    num_solutions += find_solutions(springs[1:], sizes[1:])
            else:  # If the . is at the end of a group and it doesn't match the first size, continue without removing a group
                num_solutions += find_solutions(springs[1:], sizes)
    return num_solutions

def part1(parsed_data):
    # Pipe each line into the find solutions function and return the sum
    return sum(find_solutions((springs + '.'), sizes) for springs, sizes in parsed_data)

def part2(parsed_data):
    # Expand each string and size tuple by 5 and return the sum of the find solutions function
    return sum(find_solutions(('?'.join([springs] * 5) + '.'), (sizes * 5)) for springs, sizes in parsed_data)

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - There are {answer1} possible arangements")
    print(f"PART2 - There are {answer2} possible arangements of the unfolded records")