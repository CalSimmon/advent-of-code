def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def calculateOxygen(readings):
    ephemeral = readings
    for x in range(len(ephemeral[0])):
        temp = []
        majority = 0
        for line in ephemeral:
            if (int(line[x]) == 1):
                majority += 1

        if (majority >= (int(len(ephemeral)) / 2)):
            majority = 1
        else:
            majority = 0

        for line in ephemeral:
            if (int(line[x]) == majority):
                temp.append(line)

        ephemeral = temp
            
    return int(ephemeral[0], 2)

def calculateCO2(readings):
    ephemeral = readings
    for x in range(len(ephemeral[0])):
        temp = []
        majority = 0
        for line in ephemeral:
            if (int(line[x]) == 1):
                majority += 1

        if (majority < (int(len(ephemeral)) / 2)):
            majority = 0
        else:
            majority = 1

        for line in ephemeral:
            if (int(line[x]) != majority):
                temp.append(line)

        if (int(len(ephemeral)) != 1):
            ephemeral = temp
            
    return int(ephemeral[0], 2)

readings = readFile("Day3Input.txt")
oxReading = calculateOxygen(readings)
print(oxReading)
co2Reading = calculateCO2(readings)
print(co2Reading)
lifeSupport = oxReading * co2Reading

print("Life Support Rating is " + str(lifeSupport))