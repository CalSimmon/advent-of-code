import string

def part1(data):
    total = 0
    for line in data.splitlines():
        line_split = [line[:len(line)//2], line[len(line)//2:]]
        for character in line_split[0]:
            if character in line_split[1]:
                total += list(string.ascii_letters).index(character) + 1
                break
    print(f"Total count for part 1 is {total}.")
    
def part2(data):
    data = data.splitlines()
    total = 0
    groups = [data[x * 3:(x * 3) + 3] for x in range(len(data) // 3)]
    for group in groups:
        for character in group[0]:
            if character in group[1] and character in group[2]:
                total += list(string.ascii_letters).index(character) + 1
                break
    print(f"Total count for part 2 is {total}.")


if __name__ == "__main__":
    with open("day3input.txt", "r") as f:
        data = f.read()
    part1(data)
    part2(data)