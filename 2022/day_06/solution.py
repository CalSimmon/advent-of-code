from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

def part1(data):
    # Run through the length of the data in chunks of 4
    for x in range(len(data) - 3):
        curr = data[x:x + 4]
        # Check if there are any duplicates in the chunk.  If there isn't, return the number of characters.
        if len(set(curr)) == len(curr):
            marker = x + 4
            break
    print(f"The first marker is after character {marker}.")
    
def part2(data):
    # Run through the length of the data in chunks of 14
    for x in range(len(data) - 13):
        curr = data[x:x + 14]
        # Check if there are any duplicates in the chunk.  If there isn't, return the number of characters.
        if len(set(curr)) == len(curr):
            message = x + 14
            break
    print(f"The first message is after character {message}.")


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        data = f.read()
    part1(data)
    part2(data)