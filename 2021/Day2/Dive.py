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


directions = readFile("Day2Input.txt")
horizontal = 0
depth = 0
answer = calculate(directions, horizontal, depth)
print("The answer is " + str(answer))