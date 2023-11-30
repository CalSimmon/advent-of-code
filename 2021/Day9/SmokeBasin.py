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

### MAIN ###
if __name__ == "__main__":
    with open("Day9Input.txt") as f:
        lines = f.read().splitlines()

    smokeBasin = Basin(lines)
    answer = smokeBasin.search_points()
    print("The risk level is " + str(answer))
