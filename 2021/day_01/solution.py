### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def readFile(fileName):
    fileObj = open(fileName, "r")
    words = fileObj.read().splitlines()
    fileObj.close()
    return words

# Part 1
distances = readFile(INPUT_PATH)
increase = 0
i = 1
while i < len(distances):
    if (int(distances[i]) > int(distances[i - 1])):
        increase += 1
    i += 1

print("The distance increased " + str(increase) + " times")

# Part 2
increase = 0
i = 3
while i < len(distances):
    current = int(distances[i]) + int(distances[i - 1]) + int(distances[i - 2])
    previous = int(distances[i - 1]) + int(distances[i - 2]) + int(distances[i - 3])
    if (current > previous):
        increase += 1
    i += 1

print("The distance increased " + str(increase) + " times")