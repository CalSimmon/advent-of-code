# Return a grid of all the trees in input
def get_tree_grid(data):
    return [[x for x in line]for line in data.splitlines()]

# Create a bool grid to track visible trees using width and length of the tree_grid
def get_bool_grid(length, width):
    return [[False for i in range(width)] for x in range(length)]

# Get the column at index into a traversable list
def get_column_list(tree_grid, index):
    return [row[index] for row in tree_grid]

# Sum the entire bool_grid to find total number of visible trees
def get_sum_bool(bool_grid):
    return sum(sum(x) for x in bool_grid)

# Run through the supplied list and find which trees are visible, return filled bool_grid 
def record_tallest(tree_list, bool_grid, x, column=False):
    tallest = 0
    for idx, tree in enumerate(tree_list):
        # If the tree is taller than the tallest so far, track that it's visible in bool grid
        if int(tree) > tallest:
            tallest = int(tree)
            if idx != 0 and idx != len(tree_list) - 1:
                # If the tree_list is a column, track on a different axis
                if column:
                    bool_grid[idx][x] = True
                else:
                    bool_grid[x][idx] = True
    # Run the same test reversed
    bool_grid = record_tallest_reversed(tree_list, bool_grid, x, column)
    return bool_grid

# Run through the supplied list in reverse and find which trees are visible, return filled bool_grid 
def record_tallest_reversed(tree_list, bool_grid, x, column=False):
    tallest = 0
    # Since we need to find visible trees from both directions, run this check in reverse
    for idx, tree in reversed(list(enumerate(tree_list))):
        # If the tree is taller than the tallest so far, track that it's visible in bool grid
        if int(tree) > tallest:
            tallest = int(tree)
            if idx != 0 and idx != len(tree_list) - 1:
                # If the tree_list is a column, track on a different axis
                if column:
                    bool_grid[idx][x] = True
                else:
                    bool_grid[x][idx] = True
    return bool_grid

# Check all directions to find number of visible trees, return scenic score
def check_directions(ir, ic, tree_grid):
    # Total scenic score of tree
    scenic_score = 1
    curr_tree = int(tree_grid[ir][ic])
    left = ic
    right = ic
    up = ir
    down = ir
    # Direction score
    dir_score = 0
    # For directions left, right, up, and down: move in the respective directions, and if the tree is shorter
    # Add 1 to dir_score.  When it find a tree that is taller, or hits the end of the row / column, 
    # Multiple the dir_score with the scenic_score, and set dir_score back to 0
    while left > 0:
        left -= 1
        if curr_tree > int(tree_grid[ir][left]):
            dir_score += 1
        elif curr_tree <= int(tree_grid[ir][left]):
            dir_score += 1
            scenic_score *= dir_score
            dir_score = 0
            break
        if left == 0:
            scenic_score *= dir_score
            dir_score = 0
    while right < len(tree_grid[0]) - 1:
        right += 1
        if curr_tree > int(tree_grid[ir][right]):
            dir_score += 1
        elif curr_tree <= int(tree_grid[ir][right]) or right == len(tree_grid[0]) - 1:
            dir_score += 1
            scenic_score *= dir_score
            dir_score = 0
            break
        if right == len(tree_grid[0]) - 1:
            scenic_score *= dir_score
            dir_score = 0
    while up > 0:
        up -= 1
        if curr_tree > int(tree_grid[up][ic]):
            dir_score += 1
        elif curr_tree <= int(tree_grid[up][ic]):
            dir_score += 1
            scenic_score *= dir_score
            dir_score = 0
            break
        if up == 0:
            scenic_score *= dir_score
            dir_score = 0
    while down < len(tree_grid) - 1:
        down += 1
        if curr_tree > int(tree_grid[down][ic]):
            dir_score += 1
        elif curr_tree <= int(tree_grid[down][ic]):
            dir_score += 1
            scenic_score *= dir_score
            dir_score = 0
            break
        if down == len(tree_grid) - 1:
            scenic_score *= dir_score
            dir_score = 0
    return scenic_score

def part1(data):
    # Create the tree_grid and bool_grid to track tall trees
    tree_grid = get_tree_grid(data)
    bool_grid = get_bool_grid(len(tree_grid), len(tree_grid[0]))
    # Run through rows and columns in tree_grid and return the filled out bool_grid
    for x in range(1, len(tree_grid) - 1):
        bool_grid = record_tallest(tree_grid[x], bool_grid, x)
        bool_grid = record_tallest(get_column_list(tree_grid, x), bool_grid, x, True)
    # Get the total of all visible trees and exterior trees and answer will be them added together
    visible = get_sum_bool(bool_grid)
    exterior = (len(tree_grid) * 4) - 4
    print(f"There are {visible + exterior} tree visible.")
    return bool_grid
    
def part2(data, bool_grid):
    # Re-create tree_grid
    tree_grid = get_tree_grid(data)
    highest = 0
    for idxrow, row in enumerate(bool_grid):
        for idxtree, tree in enumerate(row):
            # If the tree is tracked as visible in the bool_grid, find the scenic_score
            if tree:
                scenic_score = check_directions(idxrow, idxtree, tree_grid)
                # If the scenic score is the highest so far, track it
                if scenic_score > highest:
                    highest = scenic_score
    print(f"The highest scenic score is {highest}.")


if __name__ == "__main__":
    with open("day8input.txt", "r") as f:
        data = f.read()
    # Return the bool_grid to pass into part2
    bool_grid = part1(data)
    part2(data, bool_grid)