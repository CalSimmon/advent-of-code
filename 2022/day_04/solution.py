from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def check_groups(group, number, operator):
    if operator == "<=":
        return int(group[0][number]) <= int(group[1][number])
    else:
        return int(group[0][number]) >= int(group[1][number])

def check_overlap(group):
    if int(group[0][0]) in range(int(group[1][0]), int(group[1][1]) + 1):
        return True
    elif int(group[0][1]) in range(int(group[1][0]), int(group[1][1]) + 1):
        return True
    elif int(group[1][0]) in range(int(group[0][0]), int(group[0][1]) + 1):
        return True
    elif int(group[1][1]) in range(int(group[0][0]), int(group[0][1]) + 1):
        return True
    else:
        return False

def part1(data):
    assignments = [[elf.split('-') for elf in groups.split(',')] for groups in data.splitlines()]
    total = 0
    for group in assignments:
        if check_groups(group, 0, "<=") and check_groups(group, 1, ">="):
            total += 1
        elif check_groups(group, 0, ">=") and check_groups(group, 1, "<="):
            total += 1
    print(f"There are {total} contained pairs.")
    
def part2(data):
    assignments = [[elf.split('-') for elf in groups.split(',')] for groups in data.splitlines()]
    total = 0
    for group in assignments:
        if check_overlap(group):
            total += 1
    print(f"There are {total} groups that overlap.")


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        data = f.read()
    part1(data)
    part2(data)