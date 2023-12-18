from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split each line into three pieces based on spaces and return the nested list
    data_list = [line.split() for line in data.splitlines()]
    return data_list

def next_point(point, direction, dist):
    # Based on direction and distance, return the next point
    match direction:
        case 'R': return (point[0] + dist, point[1])
        case 'L': return (point[0] - dist, point[1])
        case 'U': return (point[0], point[1] - dist)
        case 'D': return (point[0], point[1] + dist)

def area_of_polygon(p, perimeter):
    # Use the shoelace formula to get the area of an irregular polygon based on points
    a = 0
    for i in (range(len(p) - 1)):
        a += p[i][0] * p[i + 1][1]
        a -= p[i][1] * p[i + 1][0]
    a += perimeter  # Don't forget the items in the perimeter
    return ((a // 2) + 1)  # Add one to include the first point

def hex_number(num):
    # int can convert hex to dec if it begins with 0x and includes base 0 at the end, so add those and return the decimal value
    # of only the first 5 numbers
    return int((num.strip('()').replace('#', '0x')[:7]), 0)

def get_direction(num):
    # Return the direction based on the last number of the hex number
    match num:
        case '0': return 'R'
        case '1': return 'D'
        case '2': return 'L'
        case '3': return 'U'

def parse_points(data):
    # Start at point (0, 0) and get use next_point to get an ordered list of all points after moving, include the perimeter
    # and plug into area_of_polygon to return the total area of the hole
    curr_point = (0, 0)
    all_points = [curr_point]  # Shoelace method needs both ends to have the starting point
    perimeter = 0
    for line in data:
        print(f"Found point {curr_point}")
        curr_point = next_point(curr_point, line[0], int(line[1]))
        perimeter += int(line[1])
        all_points.append(curr_point)
    return area_of_polygon(all_points, perimeter)

def convert_hex_to_directions(data):
    # Helper function to convert the hex number into directions
    for line in data:
        yield [get_direction(line[2][-2]), hex_number(line[2])]

def part1(parsed_data):
    # Return the area of the instructions without hex number
    return parse_points(parsed_data)

def part2(parsed_data):
    # Convert the hex number into directions based on instructions and return the area of the new polygon
    return parse_points(convert_hex_to_directions(parsed_data))

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The hole could carry {answer1} cubic meters of lava")
    print(f"PART2 - {answer2}")