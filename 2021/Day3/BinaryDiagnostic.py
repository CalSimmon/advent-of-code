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

readings = readFile("Day3Input.txt")
bits = [0] * len(readings[0])
gamma = ''
epsilon = ''
powerCon = calculate(readings, bits, gamma, epsilon)

print("Power Consumption is " + str(powerCon))