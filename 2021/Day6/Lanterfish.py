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

### MAIN ###
if __name__ == "__main__":
    with open("Day6Input.txt") as f:
        lines = f.read().split(",")
        ints = []
        for line in lines:
            ints.append(int(line))
    
    lanternFish = School(ints)
    for day in range(80):
        lanternFish.day_pass()

    print("The answer is " + str(len(lanternFish.school)))

    