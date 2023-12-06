import math
import bisect
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split the input into lines for the future parsing
    data_list = data.splitlines()
    return data_list

def parse_part1(parsed_data):
    # Return a generator of tuple pairs that are (time, distance) and converted to int
    return zip(list(map(int, parsed_data[0].split()[1:])), list(map(int, parsed_data[1].split()[1:])))

def parse_part2(parsed_data):
    # Return the pair of time and distance with all spaces remove and converted to int
    return [int(parsed_data[0].split(": ")[1].replace(' ','')), int(parsed_data[1].split(": ")[1].replace(' ',''))]

def check_h(time, distance, h):
    # Returns a boolean for the formula (total_time - held_time) * held_time = distance_traveled
    return (time - h) * h > distance

def branching_win_range(time, distance):
    # Run a binary search to quickly find the maximum and minimum hold values that are higher than the record distance, return the length of the range
    direction_list = [-1, 1]  # This just simplifies the while loop so I can just run it in both directions, start with highest and find lowest
    win_range = []
    for direction in direction_list:
        low, high = (0, time)
        while low < high:
            mod = 1 if direction == -1 else 0  # Changes the modifier if finding high or low
            mid = (low + high + mod) // 2
            if check_h(time, distance, mid):
                if direction == -1:
                    low = mid
                else:
                    high = mid 
            else:
                if direction == -1:
                    high = mid + direction
                else:
                    low = mid + direction
        win_range.append(low)
    total = win_range[0] - (win_range[1] - 1)
    print(f"For a race of {time}ms and {distance}mm, there are {total} ways to win.")
    return total

def part1(parsed_data):
    # Run through each race and find the win range
    parsed_data = parse_part1(parsed_data)
    answer = math.prod([branching_win_range(*race) for race in parsed_data])
    return answer

def part2(parsed_data):
    # Run through the big race and find the win range
    parsed_data = parse_part2(parsed_data)
    answer = branching_win_range(*parsed_data)
    return answer

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The number of ways to win multiplied is {answer1}")
    print(f"PART2 - The big race can be won in {answer2} ways")