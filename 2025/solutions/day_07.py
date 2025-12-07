def parse_input(data):
    # Function for parsing input.
    data_list = data.splitlines()
    start = None
    splitter_list = []
    for r, row in enumerate(data_list):
        splitter_row = set()
        for c, item in enumerate(list(row)):
            if item == "S":
                start = (r, c)
            elif item == "^":
                splitter_row.add(c)
        splitter_list.append(splitter_row)
    print(start)
    for row in splitter_list:
        print(row)
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


def test(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    if part is None or part == 1:
        output = part1(parsed_data)
        expected = 21
        try:
            assert output == expected
        except AssertionError as e:
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
        expected = 0
        try:
            assert output == expected
        except AssertionError as e:
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
