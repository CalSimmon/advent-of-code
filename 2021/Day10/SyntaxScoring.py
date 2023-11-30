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

### MAIN ###
if __name__ == "__main__":
    with open("Day10Input.txt") as f:
        lines = f.read().splitlines()

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