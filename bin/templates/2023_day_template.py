def parse_input(data):
    data_list = data.splitlines()
    # Add parsing code here
    return data_list

def part1(parsed_data):
    # Add part 1 code here
    return 'part1'

def part2(parsed_data):
    # Add part 2 code here
    return 'part2'

if __name__ == "__main__":
    with open("example.txt" , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - {answer1}")
    print(f"PART2 - {answer2}")