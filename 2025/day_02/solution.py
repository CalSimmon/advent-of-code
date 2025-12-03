from pathlib import Path
import re

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")


def parse_input(data):
    # Function for parsing input.
    data_list = [pair.split("-") for pair in data.splitlines()[0].split(",")]
    return data_list


def part1(parsed_data):
    total_value = 0
    for item in parsed_data:
        for num in range(int(item[0]), (int(item[1]) + 1)):
            num_str = str(num)
            if (
                len(str(num)) % 2 == 0
                and num_str[: int(len(num_str) / 2)] == num_str[int(len(num_str) / 2) :]
            ):
                total_value += num
                print(f"{num} in an invalid ID.")
    return total_value


def part2(parsed_data):
    total_value = 0
    for item in parsed_data:
        for num in range(int(item[0]), (int(item[1]) + 1)):
            s = str(num)
            match = re.fullmatch(r"(.+?)\1+", s)
            if match:
                print(f"{num} is an invalid ID.")
                total_value += num
    return total_value


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)

    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total of invalid IDs is {answer1}.")
    print(f"PART2 - The dial passes zero {answer2} times.")
