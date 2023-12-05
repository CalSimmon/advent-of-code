### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from typing import Pattern
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class Display:
    def __init__(self, segment):
        self.segment = segment
        self.signal = self.segment[0]
        self.output = self.segment[1]

    @classmethod
    def organize(cls, segments):
        segment = [[x for x in item.split()] for item in segments.split(" | ")]
        return cls(segment)
    
class Display2:
    def __init__(self, segment):
        self.segment = segment
        self.signal = self.segment[0]
        self.output = self.segment[1]
        self.one = ''
        self.four = ''
        self.seven = ''
        self.eight = ''
        self.fiveDigit = []
        self.sixDigit = []
        self.key = []

    def identify_numbers(self):
        # Identify the easy to find numbers / combine like numbers
        for digit in self.signal:
            if (len(digit) == 2):
                self.one = digit
            if (len(digit) == 4):
                self.four = digit
            if (len(digit) == 3):
                self.seven = digit
            if (len(digit) == 7):
                self.eight = digit
            if (len(digit) == 5):
                self.fiveDigit.append(digit)
            if (len(digit) == 6):
                self.sixDigit.append(digit)

    def find_pattern(self):
        pattern = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        # Get the top line
        pattern[0] = (list(set(self.one) ^ set(self.seven)))[0]

        # Find the middle and bottom line from the intersection of the five digit numbers to compare to 4
        temp = ((''.join((set(self.fiveDigit[0]).intersection(self.fiveDigit[1])).intersection(self.fiveDigit[2])))).replace(pattern[0], '')
        temp2 = (''.join(set(self.one) ^ set(self.four)))
        # Use the information to find position 4 and 7.
        if temp[0] in temp2:
            pattern[3] = temp[0]
            pattern[6] = temp[1]
        else:
            pattern[3] = temp[1]
            pattern[6] = temp[0]
        # Use the final letter to find position 2.
        pattern[1] = temp2.replace(pattern[3], '')
        # Use the difference of six digit numbers to compare to one.
        firstComp = ''.join(set(self.sixDigit[0]) ^ set(self.sixDigit[1]))
        secComp = ''.join(set(self.sixDigit[1]) ^ set(self.sixDigit[2]))
        comp = (''.join(list(set(firstComp + secComp)))).replace(pattern[3], '')
        # Find the difference between comp and one and add that to the third position
        pattern[2] = ''.join(set(comp) & set(self.one))
        pattern[4] = comp.replace(pattern[2], '')
        pattern[5] = self.one.replace(pattern[2], '')
        self.key = pattern
    
    def decode_output(self) -> int:
        # Define the patterns for each number to check later.
        zero = [''.join(sorted(self.key[0] + self.key[1] + self.key[2] + self.key[4] + self.key[5] + self.key[6])), 0]
        one = [''.join(sorted(self.key[2] + self.key[5])), 1]
        two = [''.join(sorted(self.key[0] + self.key[2] + self.key[3] + self.key[4] + self.key[6])), 2]
        three = [''.join(sorted(self.key[0] + self.key[2] + self.key[3] + self.key[5] + self.key[6])), 3]
        four = [''.join(sorted(self.key[1] + self.key[2] + self.key[3] + self.key[5])), 4]
        five = [''.join(sorted(self.key[0] + self.key[1] + self.key[3] + self.key[5] + self.key[6])), 5]
        six = [''.join(sorted(self.key[0] + self.key[1] + self.key[3] + self.key[4] + self.key[5] + self.key[6])), 6]
        seven = [''.join(sorted(self.key[0] + self.key[2] + self.key[5])), 7]
        eight = [''.join(sorted(self.key[0] + self.key[1] + self.key[2] + self.key[3] + self.key[4] + self.key[5] + self.key[6])), 8]
        nine = [''.join(sorted(self.key[0] + self.key[1] + self.key[2] + self.key[3] + self.key[5] + self.key[6])), 9]
        numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
        # Find the cooresponding number in the output.
        finalDig = ''
        for digit in self.output:
            for number in numbers:
                if ((''.join(sorted(digit))) == number[0]):
                    finalDig += str(number[1])
        
        return finalDig

    @classmethod
    def organize(cls, segments):
        segment = [[x for x in item.split()] for item in segments.split(" | ")]
        return cls(segment)


### MAIN ###
if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
    
    # Part 1
    displays = [Display.organize(lines[x]) for x in range(len(lines))]

    compare = [2,3,4,7]
    answer = 0
    for items in displays:
        for digit in items.segment[1]:
            if (len(digit) in compare):
                answer += 1

    print("There are " + str(answer) + " instances of the simple numbers.")

    # Part 2
    displays = [Display2.organize(lines[x]) for x in range(len(lines))]

    answer = 0
    for display in displays:
        display.identify_numbers()
        display.find_pattern()
        output = display.decode_output()
        answer += int(output)
    
    print("The answer is " + str(answer))