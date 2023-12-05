### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class School:
    def __init__(self, school):
        self.school = school
    
    def day_pass(self):
        newFish = 0
        for idx, fish in enumerate(self.school):
            if (fish != 0):
                self.school[idx] -= 1
            else:
                newFish += 1
                self.school[idx] = 6
        if (newFish > 0):
            for new in range(newFish):
                self.fish_birth()

    def fish_birth(self):
        self.school.append(8)

class School2:
    def __init__(self):
        self.school = [0 for i in range(9)]

    def fill_school(self, fish):
        for fishAge in fish:
            self.school[fishAge] += 1

    def increment_day(self):
        fullTerm = self.school.pop(0)
        self.school.append(fullTerm)
        self.school[6] += fullTerm

### MAIN ###
if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().split(",")
        ints = []
        for line in lines:
            ints.append(int(line))
    
    # Part 1
    lanternFish = School(ints)
    for day in range(80):
        lanternFish.day_pass()

    print("The answer is " + str(len(lanternFish.school)))

    # Part 2
    lanternFish = School2()
    lanternFish.fill_school(ints)
    for day in range(256):
        lanternFish.increment_day()

    print(lanternFish.school)
    print("The answer is " + str(sum(lanternFish.school)))

    