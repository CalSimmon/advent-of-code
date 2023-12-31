### This came early on in my programming career and may contain a lot of excessive code.
### I will keep it up for posterity, but keep that in mind.

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

class Board:
    def __init__(self, grid):
        self.grid = grid

    def check_board(self, number):
        for line in self.grid:
            for idx, val in enumerate(line):
                if (val != 'X'):
                    if (int(val) == int(number)):
                        line[idx] = 'X'
    
    def has_won(self) -> bool:
        won = False
        for line in self.grid:
            count = 0
            for currentNumber in line:
                if (currentNumber == 'X'):
                    count += 1
            if (count == len(line)):
                won = True
        
        for column in range(len(self.grid[0])):
            count = 0
            for line in self.grid:
                if (line[column] == 'X'):
                    count += 1
            if (count == len(self.grid)):
                won = True

        return won

    def calculate_answer(self, currNum) -> int:
        unmarked = 0
        for line in self.grid:
            for item in line:
                if (item != 'X'):
                    unmarked += int(item)
        
        return unmarked * currNum

    def print_board(self):
        for line in self.grid:
            print(line)

    @classmethod
    def organize(cls, lines):
        grid = [[int(x) for x in line.split()] for line in lines]
        return cls(grid)

class Board2:
    def __init__(self, grid):
        self.grid = grid

    def check_board(self, number):
        for line in self.grid:
            for idx, val in enumerate(line):
                if (val != 'X'):
                    if (int(val) == int(number)):
                        line[idx] = 'X'
    
    def has_won(self) -> bool:
        won = False
        for line in self.grid:
            count = 0
            for currentNumber in line:
                if (currentNumber == 'X'):
                    count += 1
            if (count == len(line)):
                won = True
        
        for column in range(len(self.grid[0])):
            count = 0
            for line in self.grid:
                if (line[column] == 'X'):
                    count += 1
            if (count == len(self.grid)):
                won = True

        return won

    def calculate_answer(self, currNum) -> int:
        unmarked = 0
        for line in self.grid:
            for item in line:
                if (item != 'X'):
                    unmarked += int(item)
        
        return unmarked * currNum

    def print_board(self):
        for line in self.grid:
            print(line)

    @classmethod
    def organize(cls, lines):
        grid = [[int(x) for x in line.split()] for line in lines]
        return cls(grid)



if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()

# Part 1
picked = lines[0].split(",")

boards = [Board.organize(lines[i + 1 : i + 6]) for i in range(1, len(lines), 6)]

for number in picked:
    found = False
    for board in boards:
        board.check_board(number)
        #board.print_board()
        if board.has_won():
            print("\nYou found the winner!\n")
            board.print_board()
            print("\nYour score is " + str(board.calculate_answer(int(number))) + "\n")
            found = True
            break
    if found:
        break

# Part 2
picked = lines[0].split(",")

boards = [Board2.organize(lines[i + 1 : i + 6]) for i in range(1, len(lines), 6)]

for number in picked:
    temp = []
    for board in boards:
        board.check_board(number)
        if (len(boards) != 1):
            if board.has_won():
                temp.append(board)
        else:
            if board.has_won():
                print("\nYou have found the ideal loser board!\n")
                boards[0].print_board()
                print("\nThe answer is " + str(boards[0].calculate_answer(int(number))) + "\n")
                exit()
    
    for item in temp:
        if (len(temp) > 0):
            boards.remove(item)