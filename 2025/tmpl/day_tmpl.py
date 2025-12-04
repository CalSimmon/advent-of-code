def parse_input(data):
    # Function for parsing input.
    data_list = data.splitlines()
    return data_list


def part1(parsed_data):
    total_value = 0
    return total_value


def part2(parsed_data):
    total_value = 0
    return total_value


def solve(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    answers = "\n--- ANSWERS ---"

    if part is None or part == 1:
        print("--- PART 1 ---")
        answer1 = part1(parsed_data)
        answers += f"\nPART1 - {answer1}"

    if part is None or part == 2:
        print("\n--- PART 2 ---")
        answer2 = part2(parsed_data)
        answers += f"\nPART2 - {answer2}"

    print(answers)
