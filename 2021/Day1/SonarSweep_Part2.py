def readFile(fileName):
    fileObj = open(fileName, "r")
    words = fileObj.read().splitlines()
    fileObj.close()
    return words

distances = readFile("Day1Input.txt")
increase = 0
i = 3
while i < len(distances):
    current = int(distances[i]) + int(distances[i - 1]) + int(distances[i - 2])
    previous = int(distances[i - 1]) + int(distances[i - 2]) + int(distances[i - 3])
    if (current > previous):
        increase += 1
    i += 1

print("The distance increased " + str(increase) + " times")