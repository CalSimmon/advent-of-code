def parse_input(data):
    # Function for parsing input.
    fresh_ids, ing_ids = data.split("\n\n")
    fresh_ids = [list(map(int, id.split("-"))) for id in fresh_ids.splitlines()]
    fresh_ids.sort()
    ing_ids = set(int(id) for id in ing_ids.splitlines())
    return fresh_ids, ing_ids


def part1(parsed_data):
    total_value = 0
    fresh_ids, ing_ids = parsed_data

    for id in ing_ids:
        for id_range in fresh_ids:
            if id >= id_range[0] and id <= id_range[1]:
                print("{} is a fresh ID.".format(id))
                total_value += 1
                break

    return total_value


def part2(parsed_data):
    total_value = 0
    fresh_iter = iter(parsed_data[0])
    curr = next(fresh_iter)
    next_range = next(fresh_iter)
    while next_range is not None:
        if next_range[0] <= curr[1]:
            curr[1] = max([curr[1], next_range[1]])
            next_range = next(fresh_iter, None)
        else:
            print("Merged ranges to {}.".format(curr))
            total_value += curr[1] - curr[0] + 1
            curr = next_range
            next_range = next(fresh_iter, None)
    else:
        print("Merged ranges to {}.".format(curr))
        total_value += curr[1] - curr[0] + 1

    return total_value


def solve(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    answers = "\n--- ANSWERS ---"

    if part is None or part == 1:
        print("--- PART 1 ---")
        answer1 = part1(parsed_data)
        answers += f"\nPART1 - There are {answer1} fresh ingredients."

    if part is None or part == 2:
        print("\n--- PART 2 ---")
        answer2 = part2(parsed_data)
        answers += (
            f"\nPART2 - There are {answer2} ingredient IDs that are considered fresh."
        )

    print(answers)


def test(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    if part is None or part == 1:
        output = part1(parsed_data)
        expected = 3
        try:
            assert output == expected
        except AssertionError:
            print(
                "Example Failure:\n => Expected: {}\n => Output: {}".format(
                    expected, output
                )
            )
            exit(1)
        print(
            "Tests passed...\n => Expected: {}\n => Output: {}".format(expected, output)
        )

    if part is None or part == 2:
        output = part2(parsed_data)
        expected = 14
        try:
            assert output == expected
        except AssertionError:
            print(
                "Example Failure:\n => Expected: {}\n => Output: {}".format(
                    expected, output
                )
            )
            exit(1)
        print(
            "Tests passed...\n => Expected: {}\n => Output: {}".format(expected, output)
        )
