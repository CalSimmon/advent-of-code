class Syntax:
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
    with open("Day10Input.txt") as f:
        lines = f.read().splitlines()

    subsystem = [Syntax.organize(lines[x]) for x in range(len(lines))]

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