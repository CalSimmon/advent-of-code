from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")

# Function to get the chart into a dictionary
def get_chart(data):
    # Grab only the chart
    start_chart = data[:8]
    # Remove all the fluff and add the blank spaces and the letters in order per layer of the chart
    layers = [[line[(x * 4) + 1] for x in range(9)] for line in start_chart]
    # Create a dictionary that is based on the stack and add only the letters with the top at position 0
    chart_dict = {}
    for i in range(9):
        chart_dict[i + 1] = []
    for layer in layers:
        for iditem, item in enumerate(layer):
            if item != ' ':
                chart_dict[iditem + 1].append(item)
    return chart_dict

def part1(data):
    data = data.splitlines()
    chart_dict = get_chart(data)
    # Grab only the section that is instructions
    instructions = data[10:]
    for line in instructions:
        # Parse the instructions to grab the necessary numbers
        list_instr = line.split()
        # Run the command the number of times in the "move" section
        for i in range(int(list_instr[1])):
            # Pop the top of the stack in the "from" section and insert into the "to" section
            chart_dict[int(list_instr[5])].insert(0, chart_dict[int(list_instr[3])].pop(0))
    str_final = ""
    # Run through the dictionary in order and concat the message string.
    for key in chart_dict.keys():
        str_final += chart_dict[key][0]    
    print(f"The part 1 message is {str_final}.")
    
def part2(data):
    data = data.splitlines()
    chart_dict = get_chart(data)
    # Grab only the section that is instructions
    instructions = data[10:]
    for line in instructions:
        # Parse the instructions to grab the necessary numbers
        list_instr = line.split()
        # Add the chunk of letters defined by the "move" number from the "from" stack to the "to" stack
        chart_dict[int(list_instr[5])] = chart_dict[int(list_instr[3])][:int(list_instr[1])] + chart_dict[int(list_instr[5])]
        # Remove the chunk of letters removed from the "from" stack defined by the "move" number
        chart_dict[int(list_instr[3])] = chart_dict[int(list_instr[3])][int(list_instr[1]):]
    str_final = ""
    # Run through the dictionary in order and concat the message string.
    for key in chart_dict.keys():
        str_final += chart_dict[key][0]
    print(f"The part 2 message is {str_final}.")


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        data = f.read()
    part1(data)
    part2(data)