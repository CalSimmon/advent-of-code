import re
import copy
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Parse the data and split into a boolean map with the symbols, a list of horizontal positions of symbols, and a list of vertical positions of symbols
    # Return all three of those into a typle
    data_list = data.splitlines()
    hrz_sym = [[sym.start() for sym in re.finditer(r'[^\.]', line)] for line in data_list]
    vert_sym = [[sym.start() for sym in re.finditer(r'[^\.]', ''.join(line))] for line in zip(*data_list)]  # Use zip to get columns
    bool_map = [[False for _ in range(len(line))] for line in data_list]
    for idx, line in enumerate(hrz_sym):  # After creating boolean map, re-add the symbols into the map
        for sym in line: 
            bool_map[idx][sym] = data_list[idx][sym]
    return (bool_map, hrz_sym, vert_sym)

def sym_redirect_map():
    # Simple dictionary for determining which direction you should send based on origin
    redirect_map = {
        '\\': {
            'R': 'D',
            'L': 'U',
            'U': 'L',
            'D': 'R'
        },
        '|': {
            'R': 'UD',
            'L': 'UD',
            'U': 'U',
            'D': 'D'
        },
        '/': {
            'R': 'U',
            'L': 'D',
            'U': 'R',
            'D': 'L'
        },
        '-': {
            'R': 'R',
            'L': 'L',
            'U': 'LR',
            'D': 'LR'
        }
    }
    return redirect_map

def get_range(direction, a, z):
    # Return a range based on which direction you are heading
    match direction:
        case 'R' | 'D': return range(a, z, 1)
        case 'L' | 'U': return range((z + 1), (a + 1), 1)

def get_range_edge(direction, a, z):
    # Return the range to the end of the line based on where you are heading
    match direction:
        case 'R' | 'D': return range(a, z, 1)
        case 'L' | 'U': return range(0, (a + 1), 1)

def get_symbol_value(direction, a, m):
    # Create a list for all symbols that are in front of your current position based on direction
    match direction:
        case 'R' | 'D': return iter([idx for idx in m[a[0]] if idx >= a[1]])
        case 'L' | 'U': return iter(reversed([idx for idx in m[a[0]] if idx <= a[1]]))

def light_beam(point, m, bool_map, direction):
    # Find the symbol that's in front of you based on your current location in the grid and flip all position in between
    # to True for tracking.  Then find the redirect direction, and return the point of the next symbol, the updated bool_map, and the next direction(s)
    # If there is not a symbol in front, flip all to True up to the edge and return None, the bool_map, and None to let the program know you've hit a wall
    value = next(get_symbol_value(direction, point, m), None)
    if value is not None:
        for i in get_range(direction, point[1], value):
            if direction in 'LR':  # Change the positional parameters based on direction
                bool_map[point[0]][i] = True
            else:
                bool_map[i][point[0]] = True
        if direction in 'LR':  # Use the redirect map to determine where to send the light beam next based on direction
            next_directions = sym_redirect_map()[bool_map[point[0]][value]][direction]
            next_point = (point[0], value) 
        else:
            next_directions = sym_redirect_map()[bool_map[value][point[0]]][direction]
            next_point = (value, point[0])
        return next_point, bool_map, list(next_directions)
    else:
        for i in get_range_edge(direction, point[1], len(bool_map[point[0]])):  # You've hit an edge, let the program know to close this branch
            if direction in 'LR':
                bool_map[point[0]][i] = True
            else:
                bool_map[i][point[0]] = True
        return None, bool_map, None

def move(l, h, v, curr_point, curr_dir, mirror_hit):
    # Recursive function to follow each possible path for the light beam, and close the branch if you hit a wall or you run into a mirror in the same direction twice (loop)
    match curr_dir:  # Each direction is slightly different, so determine that first
        case 'R': 
            curr_point, l, new_dir = light_beam((curr_point[0], (curr_point[1] + 1)), h, l, curr_dir)
        case 'L': 
            curr_point, l, new_dir = light_beam((curr_point[0], (curr_point[1] - 1)), h, l, curr_dir)
        case 'D': 
            curr_point, l, new_dir = light_beam((curr_point[1], (curr_point[0] + 1)), v, l, curr_dir)
        case 'U': 
            curr_point, l, new_dir = light_beam((curr_point[1], (curr_point[0] - 1)), v, l, curr_dir)
    if curr_point is not None:  # If curr_point is None, you've hit a wall
        if curr_dir not in mirror_hit.setdefault(curr_point, []):  # If curr_dir is in mirror_hit(curr_point), you've already hit that mirrow from this direction (loop)
            mirror_hit.setdefault(curr_point, []).append(curr_dir)
            for direction in new_dir:  # If you haven't hit a wall or a loop, go deeper
                l, mirror_hit = move(l, h, v, curr_point, direction, mirror_hit)
    return l, mirror_hit

def get_energized_tiles(bool_map, mirror_hit):
    # Function to count all energized points based on their boolean value plus all mirrors hit
    return len(mirror_hit) + sum(1 for line in bool_map for item in line if item and isinstance(item, bool))

def check_all_options(data):
    # Function to run through all possible entry points for part2, return the highest value
    total_tiles = []
    length = len(data[0])
    for i in range(0, length):
        directions = [(i, -1, 'R'), (i, length, 'L'), (-1, i, 'D'), (length, i, 'U')]  # These are grouped into x value, y value, and direction
        for entry in directions:
            l, h, v = copy.deepcopy(data)  # Make a copy since you are going to need a fresh copy each time
            l, mirror_hit = move(l, h, v, (entry[0], entry[1]), entry[2], {})  # Run the recursive move function for each direction for value i
            curr_total_tiles = get_energized_tiles(l, mirror_hit)
            print(f"Entry point ({entry[0]}, {entry[1]}) has {curr_total_tiles} energized tiles")
            total_tiles.append(curr_total_tiles)
    return max(total_tiles)

def part1(parsed_data):
    # Make a copy of the list values and run a single move function for starting point (0,0)
    l, h, v = copy.deepcopy(parsed_data)
    l, mirror_hit = move(l, h, v, (0, -1), 'R', {})
    energized_tiles = get_energized_tiles(l, mirror_hit)
    print(f"Entry point (0,0) has {energized_tiles} energized tiles")
    return energized_tiles

def part2(parsed_data):
    # Use check_all_options to run through every possible entry point to return the highest energized sections
    return check_all_options(parsed_data)

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - Starting point (0,0) has {answer1} energized tiles")
    print(f"PART2 - The highest entry point has {answer2} energized tiles")