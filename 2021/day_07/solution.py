### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class Crabs:
    def __init__(self, frontLine):
        self.frontLine = frontLine
        self.min = min(self.frontLine)
        self.max = max(self.frontLine)

    def test_formation(self) -> list:
        minFuel = [0, 0]
        for position in range(self.min, self.max):
            currFuel = 0
            for fish in self.frontLine:
                currFuel += abs(fish - position)
            if (minFuel[1] == 0):
                minFuel[0] = position
                minFuel[1] = currFuel
            else:
                if (currFuel < minFuel[1]):
                    minFuel[0] = position
                    minFuel[1] = currFuel
                    
        return minFuel
    
class Crabs2:
    def __init__(self, frontLine):
        self.frontLine = frontLine
        self.min = min(self.frontLine)
        self.max = max(self.frontLine)

    def test_formation(self) -> list:
        minFuel = [0, 0]
        for position in range(self.min, self.max):
            currFuel = 0
            for fish in self.frontLine:
                posDiff = abs(fish - position)
                currFuel += ((posDiff * (posDiff + 1)) / 2)
            if (minFuel[1] == 0):
                minFuel[0] = position
                minFuel[1] = currFuel
            else:
                if (currFuel < minFuel[1]):
                    minFuel[0] = position
                    minFuel[1] = currFuel
                    
        return minFuel

### MAIN ###
if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().split(",")
        ints = []
        for line in lines:
            ints.append(int(line))

    # Part 1
    crabLine = Crabs(ints)
    fuelEfficient = crabLine.test_formation()

    print("The crabs should align at position " + str(fuelEfficient[0]) + " to use " + str(fuelEfficient[1]) + " fuel.")

    # Part 2
    crabLine = Crabs2(ints)
    fuelEfficient = crabLine.test_formation()

    print("The crabs should align at position " + str(fuelEfficient[0]) + " to use " + str(fuelEfficient[1]) + " fuel.")