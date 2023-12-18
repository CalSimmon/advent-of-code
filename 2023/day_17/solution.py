import heapq
from time import time
from collections import defaultdict
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Return a list of lists with all items converted to an int
    data_list = [list(map(int, line)) for line in data.splitlines()]
    return data_list

def check_part_one(curr_dr, curr_dc, dr, dc, straight):
    # If the direction is the same as the previous one, return None, if it's a new direction, return 1, and if it's the same direction,
    # return plus one to the straight variable
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if (dr, dc) != (curr_dr, curr_dc):
        return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1

def check_part_two(curr_dr, curr_dc, dr, dc, straight):
    # If direction is the same, add one to the straight variable, if it's opposite, add none, if it's gone for more than 4 spaces, return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if straight >= 4 or (curr_dr, curr_dc) == (0, 0):
        return 1

def dijkstra(grid, start, check_function, max_straight):
    # Use dijkstra's theorem to find the shortest distance from the start to the end
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distances = {
        (i, j): defaultdict(lambda: float("inf"))
        for j in range(len(grid[0]))
        for i in range(len(grid))
    }
    queue = [(0, start, (0, 0), 1)]
    while queue:
        current_dist, (x, y), (curr_dr, curr_dc), straight = heapq.heappop(queue)
        for dr, dc in directions:
            new_straight = check_function(curr_dr, curr_dc, dr, dc, straight)
            nx, ny = x + dr, y + dc
            if not new_straight or new_straight == max_straight:
                continue
            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = current_dist + grid[nx][ny]
                if new_dist < distances[(nx, ny)][(dr, dc, new_straight)]:
                    distances[(nx, ny)][(dr, dc, new_straight)] = new_dist
                    heapq.heappush(queue, (new_dist, (nx, ny), (dr, dc), new_straight))
    return distances

def part1(parsed_data):
    distances = dijkstra(parsed_data, (0, 0), check_part_one, 4)
    return min(distances[(len(parsed_data) - 1, len(parsed_data[0]) - 1)].values())

def part2(parsed_data):
    distances = dijkstra(parsed_data, (0, 0), check_part_two, 11)
    return min(heat_loss for (_, _, forwards), heat_loss in distances[len(parsed_data) - 1, len(parsed_data[0]) - 1].items() if forwards >= 4)

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())
    answer1 = part1(parsed_data)
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The minimum heat loss for the regular crucibles is {answer1}")
    print(f"PART2 - The minimum heat loss for the ultra crucibles is {answer2}")