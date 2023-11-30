# Make a list of unique folder paths based on the cwd passed
def make_folder_path(folder_list):
    return [''.join(folder_list[:x+1]) for x in range(len(folder_list))]

# Parse the terminal line and remove the $ from commands
def parse_line(line):
    parsed = line.split()
    if parsed[0] == "$":
        return parsed[1:]
    else:
        return parsed

# Return a dictionary of all nested folders and their total size
def get_folder_size_dict(data):
    folder_sizes = dict()
    curr_dir = list()
    terminal = data.splitlines()
    for line in terminal:
        command = parse_line(line)
        # If the command is cd, use a list to define the nested structure of cwd
        if command[0] == "cd":
            if command[1] == "..":
                curr_dir.pop()
            else:
                curr_dir.append(command[1])
        # If the line is a folder, add the size of the folder to all folders in cwd
        elif command[0].isnumeric():
            long_paths = make_folder_path(curr_dir)
            for folder in long_paths:
                # If the folder doesn't already exist in folder_sizes, define it and set it to 0
                if folder not in folder_sizes:
                    folder_sizes[folder] = 0
                folder_sizes[folder] += int(command[0])
    return folder_sizes

def part1(data):
    folder_sizes = get_folder_size_dict(data)
    sum = 0
    # Run through all keys in folder_sizes dict and only sum the ones that are under 100000
    for key in folder_sizes.keys():
        if folder_sizes[key] <= 100000:
            sum += folder_sizes[key]
    print(f"The sum of folders under 100000 is {sum}")
    
def part2(data):
    folder_sizes = get_folder_size_dict(data)
    # Find the amount of space needed to install program
    free_space = 70000000 - folder_sizes['/']
    needed_space = 30000000 - free_space
    smallest_to_fill = 0
    # Run through all keys in folder_sizes dict and check if they can free enough space if deleted
    for key in folder_sizes.keys():
        if folder_sizes[key] > needed_space:
            # If it's large enough, check if it's the smaller than smallest_to_fill
            if smallest_to_fill == 0:
                smallest_to_fill = folder_sizes[key]
            elif folder_sizes[key] < smallest_to_fill:
                smallest_to_fill = folder_sizes[key]
    print(f"The smallest folder that can free up the space is {smallest_to_fill}")


if __name__ == "__main__":
    with open("day7input.txt", "r") as f:
        data = f.read()
    part1(data)
    part2(data)