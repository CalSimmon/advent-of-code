import re
import math


def parse_input(data):
    # Function for parsing input.
    data_list = [list(re.split(r"\s+", row.strip())) for row in data.splitlines()]
    col_list = list(zip(*data_list))
    return col_list


def part1(parsed_data):
    total_value = 0

    for idx, expression in enumerate(parsed_data):
        answer = 0
        match expression[-1]:
            case "+":
                answer = sum(list(map(int, expression[:-1])))
            case "*":
                answer = math.prod(list(map(int, expression[:-1])))

        print("Expression {} equals {}.".format(idx, answer))
        total_value += answer
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


def test(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    if part is None or part == 1:
        output = part1(parsed_data)
        expected = 4277556
        try:
            assert output == expected
        except AssertionError:
            print(
                "\nExample Failure:\n => Expected: {}\n => Output: {}".format(
                    expected, output
                )
            )
            exit(1)
        print(
            "\nTests passed...\n => Expected: {}\n => Output: {}".format(
                expected, output
            )
        )

    if part is None or part == 2:
        output = part2(parsed_data)
        expected = 14
        try:
            assert output == expected
        except AssertionError:
            print(
                "\nExample Failure:\n => Expected: {}\n => Output: {}".format(
                    expected, output
                )
            )
            exit(1)
        print(
            "\nTests passed...\n => Expected: {}\n => Output: {}".format(
                expected, output
            )
        )
