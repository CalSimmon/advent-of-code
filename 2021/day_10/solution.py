### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class Syntax:
    def __init__(self, lines):
        self.syntax = lines
        self.open = ["(", "[", "{", "<"]
        self.close = [")", "]", "}", ">"]

    def check_syntax(self) -> int:
        stack = []
        for symbol in self.syntax:
            if symbol in self.open:
                stack.append(symbol)
            elif symbol in self.close:
                pos = self.close.index(symbol)
                if (len(stack) > 0) and (self.open[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    self.print_line()
                    print("CORRUPTED.")
                    return pos
        if len(stack) > 0:
            return None

    def print_line(self):
        print(self.syntax)

    @classmethod
    def organize(cls, line):
        return cls(line)
    
class Syntax2:
    def __init__(self, lines):
        self.syntax = lines
        self.open = ["(", "[", "{", "<"]
        self.close = [")", "]", "}", ">"]

    def check_syntax(self):
        stack = []
        for symbol in self.syntax:
            if symbol in self.open:
                stack.append(symbol)
            elif symbol in self.close:
                pos = self.close.index(symbol)
                if (len(stack) > 0) and (self.open[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return None
        if len(stack) > 0:
            self.print_line()
            print("INCOMPLETE")
            needed = []
            for x in range(len(stack)):
                needed.append(self.open.index(stack.pop()))
            return needed

    def print_line(self):
        print(self.syntax)

    @classmethod
    def organize(cls, line):
        return cls(line)

### MAIN ###
if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()

    # Part 1
    subsystem = [Syntax.organize(lines[x]) for x in range(len(lines))]

    failureCodes = [0 for x in range(4)]
    failureValues = [3, 57, 1197, 25137]

    for syntax in subsystem:
        codeIndex = syntax.check_syntax()
        if codeIndex != None:
            failureCodes[codeIndex] += 1

    answer = 0
    for i in range(4):
        answer += (failureCodes[i] * failureValues[i])

    print(failureCodes)
    print("The answer is " + str(answer))

    # Part 2
    subsystem = [Syntax2.organize(lines[x]) for x in range(len(lines))]

    answerArr = []
    completionValue = [1,2,3,4]
    for syntax in subsystem:
        codeIndex = syntax.check_syntax()
        if codeIndex != None:
            count = 0
            for x in codeIndex:
                count *= 5
                count += completionValue[x]
            answerArr.append(count)

    answerArr.sort()
    answer = answerArr[int((len(answerArr) - 1) / 2)]
    
    print("The answer is " + str(answer))