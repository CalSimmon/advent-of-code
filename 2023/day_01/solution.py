import re
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Function for parsing input.
    # Not special here, but will be in future days
    data_list = data.splitlines()
    return data_list

def part1(parsed_data):
    # Use regex to find all numbers within each line, turn that into the value, and add to the total
    total_value = 0
    pattern = r'\d'  # Pattern for only digits
    for line in parsed_data:
        digits = re.findall(pattern, line)
        calibration_value = (int(digits[0]) * 10) + int(digits[-1])  # Multiply the first digit by ten and add the second digit
        print(f"Calibration value of {line} is {calibration_value}")
        total_value += calibration_value
    
    return total_value

def part2(parsed_data):
    # Use regex to find all instances of digits and numbers spelled out, use the dict to turn that into the value, and add to the total
    total_value = 0
    number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'  # Match either a digit or any of the numbers spelled out
    for line in parsed_data:
        matches = re.finditer(pattern, line)  # Use finditer to also include overlapping words
        match_list = [match.group(1) for match in matches]  # Since it's an iterable, turn matches into a list
        first_digit = match_list[0] if match_list[0].isdigit() else number_dict[match_list[0]]  # If match is not digit, get digit value from number_dict
        second_digit = match_list[-1] if match_list[-1].isdigit() else number_dict[match_list[-1]]
        calibration_value = (int(first_digit) * 10) + int(second_digit) # Multiply the first digit by ten and add the second digit
        print(f"Calibration value of {line} is {calibration_value}")
        total_value += calibration_value

    return total_value

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The sum of all calibration values is {answer1}")
    print(f"PART2 - The sum of all correct calibration values is {answer2}")