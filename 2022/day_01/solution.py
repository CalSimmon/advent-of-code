from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def part1(data):
    datalist = data.splitlines()
    highest = 0
    individual_total = 0
    for item in datalist:
        if item != "":
            item = int(item)
            individual_total += item
        else:
            if individual_total > highest:
                highest = individual_total
            individual_total = 0
    print(f"The elf with the most calories has {highest} calories")
    
def part2(data):
    datalist = data.splitlines()
    highest = [0, 0, 0]
    individual_total = 0
    for item in datalist:
        if item != "":
            item = int(item)
            individual_total += item
        else:
            for i in range(0,3):
                if individual_total > highest[i]:
                    highest.insert(i, individual_total)
                    highest.pop(-1)
                    individual_total = 0
                    break
            individual_total = 0
    print(f"The sum of the top three elves is {sum(highest)} calories")


if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        data = f.read()
    part1(data)
    part2(data)