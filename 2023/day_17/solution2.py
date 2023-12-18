from collections import defaultdict
from heapq import heappop, heappush

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
FILENAME = "inputs/example1.txt"


def check_part_one(curr_dr, curr_dc, dr, dc, straight):
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if (dr, dc) != (curr_dr, curr_dc):
        return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1


def check_part_two(curr_dr, curr_dc, dr, dc, straight):
    if (dr, dc) == (curr_dr, curr_dc):
        return straight + 1
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if straight >= 4 or (curr_dr, curr_dc) == (0, 0):
        return 1


def dijkstra(matrix, start, check_function, max_straight):
    queue = [(0, start, (0, 0), 1)]
    distances = {
        (i, j): defaultdict(lambda: float("inf"))
        for j in range(len(matrix[0]))
        for i in range(len(matrix))
    }
    while queue:
        heat_loss, (row, col), (curr_dr, curr_dc), straight = heappop(queue)
        for dr, dc in DIRECTIONS:
            new_straight = check_function(curr_dr, curr_dc, dr, dc, straight)
            if not new_straight or new_straight == max_straight:
                continue
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
                new_heat_loss = heat_loss + matrix[new_row][new_col]
                if new_heat_loss < distances[new_row, new_col][dr, dc, new_straight]:
                    distances[new_row, new_col][dr, dc, new_straight] = new_heat_loss
                    new_element = (
                        new_heat_loss,
                        (new_row, new_col),
                        (dr, dc),
                        new_straight,
                    )
                    heappush(queue, new_element)
    print(distances)
    return distances


def main():
    with open(FILENAME, "r") as input_file:
        matrix = [[int(num) for num in row] for row in input_file.read().split("\n")]
    start = (0, 0)

    distances = dijkstra(matrix, start, check_part_one, 4)
    print(min(distances[len(matrix) - 1, len(matrix[0]) - 1].values()))

    # distances = dijkstra(matrix, start, check_part_two, 11)
    # print(min(
    #     heat_loss
    #     for (_, _, forwards), heat_loss in distances[len(matrix) - 1, len(matrix[0]) - 1].items()
    #     if forwards >= 4
    # ))


if __name__ == "__main__":
    main()
