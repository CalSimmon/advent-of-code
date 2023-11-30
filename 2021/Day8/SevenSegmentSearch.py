class Display:
    def __init__(self, segment):
        self.segment = segment
        self.signal = self.segment[0]
        self.output = self.segment[1]

    @classmethod
    def organize(cls, segments):
        segment = [[x for x in item.split()] for item in segments.split(" | ")]
        return cls(segment)


### MAIN ###
if __name__ == "__main__":
    with open("Day8Input.txt") as f:
        lines = f.read().splitlines()

    displays = [Display.organize(lines[x]) for x in range(len(lines))]

    compare = [2,3,4,7]
    answer = 0
    for items in displays:
        for digit in items.segment[1]:
            if (len(digit) in compare):
                answer += 1

    print("There are " + str(answer) + " instances of the simple numbers.")