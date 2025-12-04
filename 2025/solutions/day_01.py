def parse_input(data):
    # Function for parsing input.
    data_list = []
    for line in data.splitlines():
        direction = 1 if line[0] == "R" else -1
        amount = int(line[1:])
        data_list.append((direction, amount))
    return data_list


def part1(parsed_data):
    # Subtract for L and add for R and if the value divided by 100
    # has a 0 remainder, add to the total
    total_value = 0
    location = 50
    for direction, amount in parsed_data:
        print(f"Moved {direction * amount}")
        location += direction * amount
        if location % 100 == 0:
            total_value += 1
            print("=> Landed on zero!")
    return total_value


def part2(parsed_data):
    total_value = 0
    location = 50
    for direction, amount in parsed_data:
        past_total = total_value
        past_local = location
        # If move amount is greater than 100, add to total number of times it passes 0
        while amount >= 100:
            total_value += 1
            amount -= 100
        # Subtract for L and add for R
        location += direction * amount
        if location % 100 == 0:
            total_value += 1
            location = 0
        elif location < 0 or location > 100:
            if past_local != 0:  # If last value was 0, don't add a pass
                total_value += 1
            location += (direction * -1) * 100
        print(
            f"Moved {direction * amount}, passed zero {total_value - past_total} times."
        )
    return total_value


def solve(part, input_path):
    with open(input_path, "r") as f:
        parsed_data = parse_input(f.read())

    answers = "\n--- ANSWERS ---"

    if part is None or part == 1:
        print("--- PART 1 ---")
        answer1 = part1(parsed_data)
        answers += f"\nPART1 - The dial lands on zero {answer1} times."

    if part is None or part == 2:
        print("\n--- PART 2 ---")
        answer2 = part2(parsed_data)
        answers += f"\nPART2 - The dial passes zero {answer2} times."

    print(answers)
