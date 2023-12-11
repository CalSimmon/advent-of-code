import re
from itertools import groupby
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Convert the map to the readable form, split the map into lines, and find the start point
    #  Return a tuple of the map and the start point
    data = readable_map(data)
    data_list = data.splitlines()
    start = [(re.search('S', line).start(), idx) for idx, line in enumerate(data_list) if re.search('S', line)][0]
    # Add parsing code here
    return (data_list, start)

def readable_map(data):
    # Replace the letters and numbers with unicode icons that look like pipes for more readability
    replace_list = [(r'\|', '║'),('-', '═'), ('L', '╚'), ('J', '╝'), ('7', '╗'), ('F', '╔')]
    for replacement in replace_list:
        data = re.sub(*replacement, data)
    return data

def connection_map():
    # Return a dict of all possible symbols with a list of what they connect to and what direction they can accept from
    connection_map = {
        '║': ['NS', 'NS'],
        '═': ['EW', 'EW'],
        '╚': ['NE', 'SW'],
        '╝': ['NW', 'ES'],
        '╗': ['SW', 'NE'],
        '╔': ['ES', 'NW'],
        'S': ['NESW', 'NESW'],
        '.': ['', '']
    }
    return connection_map

def direction_map():
    # Return a list of modifiers for each cardinal direction
    direction_map = {
        'N': [0, -1],
        'E': [1, 0],
        'S': [0, 1],
        'W': [-1, 0]
    }
    return direction_map

def check_around_symbol(data, pos, last=None):
    # This checks all tiles in the cardinal directions around a point, and returns the x and y of a connecting pipe
    # along with the direction that it was last connected to
    conn_map = connection_map()
    direct_map = direction_map()
    opposite_list = ['NS', 'EW']  # This is just a quick way to find the opposite of the last checked direction
    x, y = pos
    symbol = data[y][x]
    for direction in conn_map[symbol][0]:  # Always starts from the top and goes to the right
        if direction != last:
            modx, mody = direct_map[direction]  # Find the modifiers from the direction map
            if 0 <= (x + modx) < (len(data[0])) or 0 <= (y + mody) < (len(data)):  # Makes sure we haven't hit the beginning or end on the x or y axis
                if direction in conn_map[data[y + mody][x + modx]][1]:  # Uses the connection_map to make sure that symbol can accept connections from the current direction
                    last = opposite_list[0].replace(direction, '') if direction in opposite_list[0] else opposite_list[1].replace(direction, '')
                    return ((x + modx), (y + mody)), last

def check_inside_polygon(grouped_range, map_cleaned):
    # Uses the range of the loop pipe for each line to quickly find all pieces that are stuck inside the loop
    pattern = r'╚═*╗|║|╔═*╝'  # Regex pattern for finding a pipe that goes across
    total_inside = 0
    trapped_list = []  # Simply for creating a visual and is not required for logic
    for idx, line in enumerate(map_cleaned):
        prev_good = False  # prev_good and prev_ground allow you to avoid checking a . symbol if the previous was confirmed good
        prev_ground = False
        for i in range(*grouped_range[idx]):
            if line[i] == '.':
                if not prev_good:
                    if prev_ground:  # If the previous was a ground that was confirmed stuck, just add another stuck
                        total_inside += 1
                        trapped_list.append((i, idx))
                    else:  # Use the even-odd rule to determine if the point is within the loop
                        cross_lines = re.findall(pattern, ''.join(line[grouped_range[idx][0]:(i + 1)]))
                        if len(cross_lines) % 2 == 1:  # If there were an odd number of cross pipes, the point is within the loop
                            trapped_list.append((i, idx))
                            total_inside += 1
                            prev_good = False
                        else:  # If there was an even number of cross pipes, the point is outside of the loop
                            prev_good = True
                prev_ground = True
            else:  # Reset the switches whenever a pipe is hit
                prev_ground = False
                prev_good = False
    
    return total_inside, trapped_list

def part1(parsed_data):
    # Find the list of pipes from the start point using the check_around_symbol function, return the midpoint and the list of pipe points
    data, start = parsed_data
    point_list = [start]
    next_point, last = check_around_symbol(data, start)  # Find the first pipe connected to S before the while loop
    while next_point != start:  # Break when you get back to the start point
        point_list.append(next_point)
        next_point, last = check_around_symbol(data, next_point, last)
    for line in parsed_data[0]: 
        print(''.join(line))
    return len(point_list) // 2, point_list

def part2(parsed_data, point_list):
    # Group the point list into a nested list based on y value and convert to a range of noteable coordinates
    # Clean up the map to remove all extraneous pipes that are not in the loop, and use check_inside_polygon to find all trapped points
    sorted_coordinates = sorted(point_list, key=lambda coord: (coord[1], coord[0]))  # Sort coordinates by y first then x
    grouped_coordinates = [list(group) for key, group in groupby(sorted_coordinates, key=lambda coord: coord[1])]
    grouped_range = [(group[0][0], (group[-1][0] + 1)) for group in grouped_coordinates]  # Group coordinates into nested list based on y value
    map_cleaned = [['.' for _ in range(len(parsed_data[0][0]))] for _ in range(len(parsed_data[0]))]  # Create a blank map of .'s for quick cleaning
    for point in point_list:  # Based on the grouped pipe points, add them into the blank map
        map_cleaned[point[1]][point[0]] = parsed_data[0][point[1]][point[0]]
    total_inside, trapped_list = check_inside_polygon(grouped_range, map_cleaned)
    for point in trapped_list:  # Prep the map for printing and print for a nice visual
        map_cleaned[point[1]][point[0]] = 'I'
    for line in map_cleaned: 
        print(''.join(line))

    return total_inside

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1, point_list = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data, point_list)

    print("\n--- ANSWERS ---")
    print(f"PART1 - There are {answer1} steps to the center of the loop")
    print(f"PART2 - There are {answer2} trapped tiles")