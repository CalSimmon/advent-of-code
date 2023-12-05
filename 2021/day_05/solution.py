### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

# This creates an instance of the over all grid, and increases it as information is added.
class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.col = len(self.grid[0])
        self.row = len(self.grid)
    
    # Make sure the size of the grid can support the current vent.  If not, run object.increase_size to fit
    def check_size(self, vent):
        for x in vent.x:
            if (x > self.col - 1):
                self.increase_size('x', x)
        for y in vent.y:
            if (y > self.row - 1):
                self.increase_size('y', y)
    
    # Works in conjunction with object.check_size to increase the size if cannot fit.
    def increase_size(self, direction, dist):
        if (direction == 'x'):
            toAdd = dist - (self.col - 1)
            for line in self.grid:
                for count in range(toAdd):
                    line.append(0)
            self.col = len(self.grid[0])
        
        if (direction == 'y'):
            toAdd = dist - (self.row - 1)
            for count in range(toAdd):
                addArray = [0 for _ in range(self.col)]
                self.grid.append(addArray)
            self.row = len(self.grid)
    
    # Use the vent to mark the vent on the grid
    def mark_grid(self, vent):
        xcoord = vent.x
        ycoord = vent.y
        xcoord.sort(reverse=True)
        ycoord.sort(reverse=True)
        xdiff = int(xcoord[0]) - int(xcoord[1])
        ydiff = int(ycoord[0]) - int(ycoord[1])

        if (xdiff == 0):
            for i in range(ycoord[1], ycoord[0] + 1):
                self.grid[i][xcoord[0]] += 1
        if (ydiff == 0):
            for i in range(xcoord[1], xcoord[0] + 1):
                self.grid[ycoord[0]][i] += 1

    # Find the number of crossings on the board.
    def calculate_answer(self) -> int:
        count = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (self.grid[y][x] >= 2):
                    count += 1
        
        return count

    # Print the grid for testing purposes.
    def print_grid(self):
        for line in self.grid:
            print(line)

class Grid2:
    def __init__(self, grid):
        self.grid = grid
        self.col = len(self.grid[0])
        self.row = len(self.grid)
    
    # Make sure the size of the grid can support the current vent.  If not, run object.increase_size to fit
    def check_size(self, vent):
        for x in vent.x:
            if (x > self.col - 1):
                self.increase_size('x', x)
        for y in vent.y:
            if (y > self.row - 1):
                self.increase_size('y', y)
    
    def increase_size(self, direction, dist):
        if (direction == 'x'):
            toAdd = dist - (self.col - 1)
            for line in self.grid:
                for count in range(toAdd):
                    line.append(0)
            self.col = len(self.grid[0])
        
        if (direction == 'y'):
            toAdd = dist - (self.row - 1)
            for count in range(toAdd):
                addArray = [0 for _ in range(self.col)]
                self.grid.append(addArray)
            self.row = len(self.grid)
    
    def mark_grid(self, vent):
        xcoord = vent.x[:]
        ycoord = vent.y[:]
        xcoord.sort(reverse=True)
        ycoord.sort(reverse=True)
        xdiff = int(xcoord[0]) - int(xcoord[1])
        ydiff = int(ycoord[0]) - int(ycoord[1])

        if (xdiff == 0):
            for i in range(ycoord[1], ycoord[0] + 1):
                self.grid[i][xcoord[0]] += 1
        elif (ydiff == 0):
            for i in range(xcoord[1], xcoord[0] + 1):
                self.grid[ycoord[0]][i] += 1
        else:
            xdir = 1
            ydir = 1

            if (vent.x[0] > vent.x[1]):
                xdir = -1
            if (vent.y[0] > vent.y[1]):
                ydir = -1

            currx = int(vent.x[0])
            curry = int(vent.y[0])

            for x in range(xcoord[1], xcoord[0] + 1):
                self.grid[curry][currx] += 1
                currx += xdir
                curry += ydir


    def calculate_answer(self) -> int:
        count = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (self.grid[y][x] >= 2):
                    count += 1
        
        return count

    def print_grid(self):
        for line in self.grid:
            print(line)


# This creates an object for each vent and will add them to the grid.
class Vent:
    def __init__(self, vent):
        self.vent = vent
        self.x = [int(self.vent[0][0]), int(self.vent[1][0])]
        self.y = [int(self.vent[0][1]), int(self.vent[1][1])]
    
    # Checks whether the entered object is a horizontal or vertical vent
    def is_horiz_vert(self) -> bool:
        if (self.vent[0][0] == self.vent[1][0]) or (self.vent[0][1] == self.vent[1][1]):
            return True
        else:
            return False

    # Parses line to get a coordinate pair.  i.e. [[X,Y], [X2,Y2]]
    @classmethod
    def organize(cls, line):
        vent = [[int(x) for x in coord.split(",")] for coord in line.split(" -> ")]
        return cls(vent)
    
class Vent2:
    def __init__(self, vent):
        self.vent = vent
        self.x = [int(self.vent[0][0]), int(self.vent[1][0])]
        self.y = [int(self.vent[0][1]), int(self.vent[1][1])]
    
    # Checks whether the entered object is a horizontal or vertical vent
    def is_horiz_vert(self) -> bool:
        if (self.vent[0][0] == self.vent[1][0]) or (self.vent[0][1] == self.vent[1][1]):
            return True
        else:
            return False

    # Parses line to get a coordinate pair.  i.e. [[X,Y], [X2,Y2]]
    @classmethod
    def organize(cls, line):
        vent = [[int(x) for x in coord.split(",")] for coord in line.split(" -> ")]
        return cls(vent)


### MAIN ###
if __name__ == "__main__":
    # Part 1
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
    
    # Uses object.organize() to split the messy lines into coordinate pairs
    vents = [Vent.organize(lines[x]) for x in range(len(lines))]
    
    # Use object.is_horiz_vert() to find only horizontal and vertical vents
    noDiag = []
    for vent in vents:
        if vent.is_horiz_vert():
            noDiag.append(vent)

    # Instantiate the grid
    currentGrid = Grid([[0], [0]])
    
    # Using organized list noDiag and run it through the grid
    for vent in noDiag:
        currentGrid.check_size(vent)
        currentGrid.mark_grid(vent)
    
    # Use grid.calculate_answer to find the number of crossing points.
    answer = currentGrid.calculate_answer() 
    print("There are " + str(answer) + " crossing points.")

    # Part 2
    # Uses object.organize() to split the messy lines into coordinate pairs
    vents = [Vent2.organize(lines[x]) for x in range(len(lines))]

    currentGrid = Grid2([[0], [0]])
    
    for vent in vents:
        currentGrid.check_size(vent)
        currentGrid.mark_grid(vent)
    
    answer = currentGrid.calculate_answer() 
    print("There are " + str(answer) + " crossing points.")