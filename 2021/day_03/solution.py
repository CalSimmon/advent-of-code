### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def calculate(readings, bits, gamma, epsilon):
    for lines in readings:
        for idx, val in enumerate(lines):
            if (int(val) == 1):
                bits[idx] += 1
    
    for value in bits:
        if (value > (len(readings) / 2)):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)

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

readings = readFile(INPUT_PATH)
bits = [0] * len(readings[0])
gamma = ''
epsilon = ''
powerCon = calculate(readings, bits, gamma, epsilon)

print("Power Consumption is " + str(powerCon))

oxReading = calculateOxygen(readings)
print(oxReading)
co2Reading = calculateCO2(readings)
print(co2Reading)
lifeSupport = oxReading * co2Reading

print("Life Support Rating is " + str(lifeSupport))