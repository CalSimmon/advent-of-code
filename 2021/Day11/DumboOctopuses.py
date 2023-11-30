class Octopi:
    def __init__(self, line):
        self.line = line
        self.flashed = [[False for _ in range(10)] for _ in range(10)]
        self.numberFlashed = 0

    def tick(self):
        for line in self.line:
            for idx, octopi in enumerate(line):
                line[idx] += 1
        
        self.check_flash()
        self.clear_flashed()

    def check_flash(self):
        for lindex, line in enumerate(self.line):
            for idx, octopi in enumerate(line):
                if (octopi > 9):
                    self.flash([lindex, idx])

    def flash(self, coord):
        self.numberFlashed += 1
        self.flashed[coord[0]][coord[1]] = True
        self.line[coord[0]][coord[1]] = 0
        directions = self.get_directions(coord)
        for step in directions:
            lindex = coord[0] + step[0]
            idx = coord[1] + step[1]
            if not (self.flashed[lindex][idx]):
                self.line[lindex][idx] += 1
                if (self.line[lindex][idx] > 9):
                    self.flash([lindex, idx])

        
    def get_directions(self, coord):
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        if (coord[0] == 0):
            del directions[0:3]
        elif (coord[0] == (len(self.line) - 1)):
            del directions[5:8]

        if (coord[1] == 0):
            if ([-1, -1] in directions):
                directions.remove([-1, -1])
            directions.remove([0, -1])
            if ([1, -1] in directions):
                directions.remove([1, -1])
        elif (coord[1] == (len(self.line[0]) - 1)):
            if ([-1, 1] in directions):
                directions.remove([-1, 1])
            directions.remove([0, 1])
            if ([1, 1] in directions):
                directions.remove([1, 1])
        
        return directions

    def clear_flashed(self):
        self.flashed = [[False for _ in range(10)] for _ in range(10)]

    def print_line(self, number):
        if number == 0:
            print("Octopi Line:")
            for x in self.line:
                print(x)
        if number == 1:
            print("\nFlashed Line:")
            for i in self.flashed:
                print(i)

### MAIN ###
if __name__ == '__main__':
    with open('Day11Input.txt') as f:
        lines = f.read().splitlines()
    
    octopiGrid = Octopi([[int(x) for x in line] for line in lines])
    
    for y in range(100):
        octopiGrid.tick()

    print(str(octopiGrid.numberFlashed) + " octopi flashed.")    