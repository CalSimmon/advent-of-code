### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class Basin:
    def __init__(self, basinMap):
        self.map = basinMap

    def search_points(self) -> int:
        riskLevel = 0
        for mapDex, row in enumerate(self.map):
            for idx, col in enumerate(row):
                if (col != 9):
                    if self.is_low_point([mapDex, idx], col):
                        riskLevel += (int(col) + 1)
        
        return riskLevel

    def is_low_point(self, point, val) -> bool:
        directions = self.find_directions(point)
        
        lowest = True
        for check in directions:
            if (self.map[check[0]][check[1]] <= val):
                lowest = False

        return lowest

    def find_directions(self, point) -> list:
        directions = [[(point[0] - 1), point[1]], [(point[0] + 1), point[1]], [point[0], (point[1] - 1)], [point[0], (point[1] + 1)]]
        remove = []
        if (point[0] == 0):
            remove.append(directions[0])
        elif (point[0] == (len(self.map) - 1)):
            remove.append(directions[1])
        
        if (point[1] == 0):
            remove.append(directions[2])
        elif (point[1] == (len(self.map[0]) - 1)):
            remove.append(directions[3])
        
        for x in remove:
            directions.remove(x)

        return directions
    
class Basin2:
    def __init__(self, basinMap):
        self.map = basinMap
        self.basins = []

    def search_points(self) -> int:
        size = []
        for mapDex, row in enumerate(self.map):
            for idx, col in enumerate(row):
                if (col != 9):
                    if self.is_low_point([mapDex, idx], col):
                        count, found = ((self.basin_size(col, self.find_directions([mapDex, idx]), set({(mapDex, idx)}))))
                        size.append(int(count) + 1)
        
        return size

    def is_low_point(self, point, val) -> bool:
        directions = self.find_directions(point)
        
        lowest = True
        for check in directions:
            if (self.map[check[0]][check[1]] <= val):
                lowest = False

        return lowest

    def find_directions(self, point) -> list:
        directions = [[(point[0] - 1), point[1]], [(point[0] + 1), point[1]], [point[0], (point[1] - 1)], [point[0], (point[1] + 1)]]
        remove = []
        if (point[0] == 0):
            remove.append(directions[0])
        elif (point[0] == (len(self.map) - 1)):
            remove.append(directions[1])
        
        if (point[1] == 0):
            remove.append(directions[2])
        elif (point[1] == (len(self.map[0]) - 1)):
            remove.append(directions[3])
        
        for x in remove:
            directions.remove(x)

        return directions

    def basin_size(self, val, directions, found):
        basinSize = 0
        spaces = set()
        for check in directions:
            currVal = int(self.map[check[0]][check[1]])
            currPoint = (check[0], check[1])
            if (currVal != 9) and (currPoint not in found):
                basinSize += 1
                spaces.add(currPoint)
        found = found.union(spaces)
        for point in spaces:
            recurseBasin, found = self.basin_size(self.map[point[0]][point[1]], self.find_directions([point[0], point[1]]), found)
            basinSize += recurseBasin

        return basinSize, found

### MAIN ###
if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()

    # Part 1
    smokeBasin = Basin(lines)
    answer = smokeBasin.search_points()
    print("The risk level is " + str(answer))

    # Part 2
    smokeBasin = Basin2(lines)
    output = sorted(smokeBasin.search_points(), reverse=True)
    answer = 1
    for x in range(3):
        answer *= int(output[x])
    print("The top three basins multiplied is " + str(answer))
