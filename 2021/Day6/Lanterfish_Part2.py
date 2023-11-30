class School:
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
    with open("Day6Input.txt") as f:
        lines = f.read().split(",")
        ints = []
        for line in lines:
            ints.append(int(line))
    
    lanternFish = School()
    lanternFish.fill_school(ints)
    for day in range(256):
        lanternFish.increment_day()

    print(lanternFish.school)
    print("The answer is " + str(sum(lanternFish.school)))

    