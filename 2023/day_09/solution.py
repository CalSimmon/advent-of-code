from functools import reduce
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Parse input into a list of lists and return the data
    data_list = [list(map(int, line.split())) for line in data.splitlines()]

    return data_list

def get_history(report):
    # Until the report is all zeros, loop through and set report equal to the difference between each of the previous pairs
    # Return a generator that will output all levels of the report's history
    yield report
    while any(report):
        curr_history = []
        for i in range(len(report) - 1):
            curr_history.append(report[i + 1] - report[i])
        report = curr_history.copy()
        yield curr_history

def part1(parsed_data):
    # Get the history for each entry, find the last item of each list, and add them progressively
    total = 0
    for idx, reading in enumerate(parsed_data):
        next_values = [section[-1] for section in reversed(list(get_history(reading)))]  # Reverse the list for logical processing
        next_value = reduce(lambda x,y: x+y , next_values)  # Use reduce to add and then use the ouput to add to the next item in the list
        print(f"Next value of reading {idx + 1} is {next_value}")
        total += next_value

    return total

def part2(parsed_data):
    # Get the history for each entry, find the first item of each list, and subtract them progressively
    total = 0
    for idx, reading in enumerate(parsed_data):
        next_values = [section[0] for section in reversed(list(get_history(reading)))]  # Reverse the list for logical processing
        first_value = reduce(lambda x,y: y-x , next_values)  # Use reduce to subtract and then use the ouput to add to the next item in the list
        print(f"First value of reading {idx + 1} is {first_value}")
        total += first_value
    
    return total

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The sum of all next values is {answer1}")
    print(f"PART2 - The sum of all first values is {answer2}")