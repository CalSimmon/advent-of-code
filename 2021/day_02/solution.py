### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def readFile(fileName):
    fileObj = open(fileName, "r")
    instructions = fileObj.read().splitlines()
    fileObj.close()
    return instructions

def calculate(instructions, horizontal, depth):
    for line in instructions:
        steps = line.split()
        if (steps[0] == 'forward'):
            horizontal += int(steps[1])
        if (steps[0] == 'down'):
            depth += int(steps[1])
        if (steps[0] == 'up'):
            depth -= int(steps[1])

    return horizontal * depth 

def calculate_part2(instructions, horizontal, depth, aim):
    for line in instructions:
        steps = line.split()
        if (steps[0] == 'forward'):
            horizontal += int(steps[1])
            depth += int(steps[1]) * aim
        if (steps[0] == 'down'):
            aim += int(steps[1])
        if (steps[0] == 'up'):
            aim -= int(steps[1])

    return horizontal * depth 

# Part 1
directions = readFile(INPUT_PATH)
horizontal = 0
depth = 0
answer = calculate(directions, horizontal, depth)
print("The answer is " + str(answer))

# Part 2
horizontal = 0
depth = 0
aim = 0
answer = calculate_part2(directions, horizontal, depth, aim)
print("The answer is " + str(answer))