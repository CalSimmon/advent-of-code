import re
import math


def parse_input(data):
    # Function for parsing input.
    data_list = data.splitlines()
    col_len_list = [len(col) for col in re.split(r"\s(?=[+\*])", data_list[-1])]
    col_list = []
    for row in data_list:
        cols = []
        idx = 0
        for col_len in col_len_list:
            idx_next = idx + col_len
            cols.append(row[idx : idx_next])
            idx = idx_next + 1
        col_list.append(cols)
    col_list = list(zip(*col_list))
    return col_list


def part1(parsed_data):
    total_value = 0

    strip_list = [num.strip() for num in parsed_data]
    for idx, expression in enumerate(strip_list):
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

    for col in parsed_data:
        rev_col = list(zip(*[list(num[::-1]) for num in col[: -1]]))
        join_numbers = [int(''.join(num).strip()) for num in rev_col]
        answer = 0
        match col[-1].strip():
            case '+':
                answer = sum(list(map(int, join_numbers)))
            case '*':
                answer = math.prod(list(map(int, join_numbers)))
        total_value += answer
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
        expected = 3263827
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
