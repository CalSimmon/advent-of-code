from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")


def parse_input(data):
    # Function for parsing input.
    data_list = [list(map(int, list(num))) for num in data.splitlines()]
    return data_list


def part1(parsed_data):
    total_value = 0
    for idx, bank in enumerate(parsed_data):
        # Make sure the highest is not at the end since there wouldn't be a second left
        highest = max(bank[:-1])
        next_high = max(bank[bank.index(highest) + 1 :])
        joltage = f"{highest}{next_high}"
        total_value += int(joltage)  # Convert from string and add to total
        print(f"Battery {idx + 1} joltage is {joltage}")
    return total_value


def part2(parsed_data):
    total_value = 0
    for idx, bank in enumerate(parsed_data):
        battery_str = ""
        curr_idx = 0
        # Find the max, limit the range to that digit and the leftover, then loop.
        for i in range(12, 0, -1):
            curr_range = bank[curr_idx : len(bank) - i + 1]
            curr_max = max(curr_range)
            battery_str += str(curr_max)
            curr_idx += curr_range.index(curr_max) + 1
        print(f"Battery {idx + 1} mega joltage is {battery_str}")
        total_value += int(battery_str)  # Convert from string and add to total
    return total_value


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)

    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - Total joltage output is {answer1}")
    print(f"PART2 - Total mega joltage output is {answer2}")
