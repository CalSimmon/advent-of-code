from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")


def parse_input(data):
    # Function for parsing input.
    data_list = [list(num) for num in data.splitlines()]
    rolls = set()
    for r, row in enumerate(data_list):
        for c, item in enumerate(row):
            if item == "@":
                rolls.add((r, c))

    return (data_list, rolls)


def get_surrounding_coords(point: tuple, col_len: int, row_len: int):
    checklist = set()
    row, col = point
    for i in range(-1, 2, 1):
        if not (row + i < 0) and not (row + i >= col_len):
            for j in range(-1, 2, 1):
                if not (col + j < 0) and not (col + j >= row_len):
                    checkpoint = (row + i, col + j)
                    if not checkpoint == point:
                        checklist.add(checkpoint)
    return checklist


def part1(parsed_data, rolls_data):
    total_value = 0
    col_len = len(parsed_data)
    row_len = len(parsed_data[0])
    for roll in rolls_data:
        surrounding = 0
        surrounding_list = get_surrounding_coords(roll, col_len, row_len)
        for check in surrounding_list:
            if check in rolls_data:
                surrounding += 1
                if surrounding >= 4:
                    break
        if surrounding < 4:
            total_value += 1
            print(f"Roll {roll} is accessible.")

    return total_value


def part2(parsed_data, rolls_data):
    total_value = 0
    col_len = len(parsed_data)
    row_len = len(parsed_data[0])
    removed = None
    loops = 0
    while removed is None or removed > 0:
        loops += 1
        removed = 0
        removeable = set()
        for roll in rolls_data:
            surrounding = 0
            surrounding_list = get_surrounding_coords(roll, col_len, row_len)
            for check in surrounding_list:
                if check in rolls_data:
                    surrounding += 1
                    if surrounding >= 4:
                        break
            if surrounding < 4:
                total_value += 1
                removeable.add(roll)
        for r in removeable:
            rolls_data.remove(r)
            removed += 1
        print(f"Pass {loops} removed {removed} rolls.")

    return total_value


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        parsed_data, rolls_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data, rolls_data)

    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data, rolls_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - There are {answer1} that are accessible.")
    print(f"PART2 - There are {answer2} that accessible after multiple passes.")
