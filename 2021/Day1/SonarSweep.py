def readFile(fileName):
    fileObj = open(fileName, "r")
    words = fileObj.read().splitlines()
    fileObj.close()
    return words

distances = readFile("Day1Input.txt")
increase = 0
i = 1
while i < len(distances):
    if (int(distances[i]) > int(distances[i - 1])):
        increase += 1
    i += 1

print("The distance increased " + str(increase) + " times")
