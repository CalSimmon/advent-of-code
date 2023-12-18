from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split each map and then return that list
    data_list = data.split("\n\n")
    return data_list

def split_horizontal_vertical(ash_map):
    # Return a list of both rows and columns from the passed map
    ash_map_split = ash_map.splitlines()
    return ash_map_split, list(zip(*ash_map_split))

def find_reflect_point(ash_map, part2=False):
    # Run through each line of the passed map and the lines match spread out and find matching lines until you hit the end of the list
    # If this is part2, introduce smudge function and return x value if a reflection is found
    for idx, line in enumerate(ash_map):
        try:  # Use a try except to avoid tracking length
            smudge = False if not part2 else find_smudge(line, ash_map[idx + 1])  # Return a bool from find_smudge only if part2 is True
            if ash_map[idx + 1] == line or smudge:  # If the line matches, or if it's part2 and smudge matches, spread out and check for matches
                reflected = True
                close_end = (idx + 1) if (len(ash_map) // 2) > idx else len(ash_map) - (idx + 1)  # Find the length to the closest end of the list
                for i in range(1, close_end):
                    if ash_map[idx + i + 1] != ash_map[idx - i]:  # If the lines don't match, reflection is False unless it's part2
                        if part2 and not smudge and find_smudge(ash_map[idx + i + 1], ash_map[idx - i]):  # If it's part2, and we have not found a smudge yet, check for smudge
                            smudge = True
                            continue
                        else:
                            reflected = False
                if part2:
                    if reflected and smudge:  # Part2 only counts if a smudge has been found
                        return (idx + 1)
                elif reflected:
                    return (idx + 1)
        except IndexError:  # Continue on if you found an index error
            pass
    return

def find_smudge(line1, line2):
    # If there's only one character different between the lists, return True else False
    return sum(line1[i] != line2[i] for i in range(len(line1))) == 1

def part1(parsed_data):
    # Go through each map, split the maps into horizontal and vertical, and process starting with horizontal first
    # If reflected on the horizontal, multiply by 100 before adding to total
    count = 1
    total = 0
    for ash_map in parsed_data:
        row_map, column_map = split_horizontal_vertical(ash_map)
        horizontal_reflect = find_reflect_point(row_map)
        if horizontal_reflect is None:
            vertical_reflect = find_reflect_point(column_map)
            print(f"Map {count} had a vertical reflect point between column {vertical_reflect} and {vertical_reflect + 1}")
            count += 1
            total += vertical_reflect
        else:
            print(f"Map {count} had a horizontal reflect point between column {horizontal_reflect} and {horizontal_reflect + 1}")
            count += 1
            total += (horizontal_reflect * 100)

    return total

def part2(parsed_data):
    # Go through each map, split the maps into horizontal and vertical, and process starting with horizontal first using the smudge mechanic
    # If reflected on the horizontal, multiply by 100 before adding to total
    count = 1
    total = 0
    for ash_map in parsed_data:
        row_map, column_map = split_horizontal_vertical(ash_map)
        horizontal_reflect = find_reflect_point(row_map, True)
        if horizontal_reflect is None:
            vertical_reflect = find_reflect_point(column_map, True)
            print(f"Map {count} had a vertical reflect point between column {vertical_reflect} and {vertical_reflect + 1}")
            count += 1
            total += vertical_reflect
        else:
            print(f"Map {count} had a horizontal reflect point between column {horizontal_reflect} and {horizontal_reflect + 1}")
            count += 1
            total += (horizontal_reflect * 100)
    return total

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The summarized notes come out to {answer1}")
    print(f"PART2 - The summarized smudges notes come out to {answer2}")