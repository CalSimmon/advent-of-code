import re
import operator
from copy import deepcopy
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Parse the output to separate the instructions and the parts and then return each of those parsed in custom ways 
    instructions, parts = [item.splitlines() for item in data.split('\n\n')]
    return (parse_instructions(instructions), parse_parts(parts))

def parse_parts(parts):
    # Remove the brackets, split by commas, and then return a list of dictionaries for each part
    return [{pair.split('=')[0]: int(pair.split('=')[1]) for pair in part.strip('{}').split(',')} for part in parts]

def parse_instructions(instructions):
    # Parse each instruction set, and return a dictionary where the keys are the instruction key, and then value is the list of instructions
    new_instr = {}
    for instr in instructions:
        curr_instr = instr.strip('}').split('{')
        key = curr_instr[0]
        value = []
        for item in curr_instr[1].split(','):
            value.append(item.split(':'))
        new_instr[key] = value
    return new_instr

def check(part, curr_instr, instructions):
    # For part 1, simply follow the instructions, and return the next possible instruction set
    for item in instructions[curr_instr]:
        if len(item) > 1:
            match = re.search(r'[<>]', item[0])  # Figure out the operator from the string, and calculate
            match match.group():
                case '<': op = operator.lt
                case '>': op = operator.gt
            if op(part[item[0][0]], int(item[0][2:])):
                return item[1]
        else:
            return item[0]
        
def recursive_check(curr_in, curr_path, accepted, instructions):
    # Use recursion to find the values that allow for each successful path and return the list of accepted paths 
    for instr in instructions[curr_in]:
        if len(instr) > 1:
            first = deepcopy(curr_path)  # If going recursive, ensure you are making a copy of the current path
            first[instr[0][0]].append(instr[0][1:])  # Add the current path to the copy
            if instr[1] == 'R':  # For these, make sure to only pass so you don't skip the opposite path for the set
                pass
            elif instr[1] == 'A':
                accepted.append(first)
                pass
            else:  # If we haven't found an end, recurse
                accepted = recursive_check(instr[1], first, accepted, instructions)
            val = int(instr[0][2:])  # Don't forget to add the difference if you have to swap operators
            match instr[0][1]:
                case '>':
                    val += 1
                case '<': 
                    val -= 1
            sym = '<>'.replace(instr[0][1], '')  # Add the opposite operator to the number when swapping
            curr_path[instr[0][0]].append(''.join([sym, str(val)]))  # Add the path to the curr_path before performing the next instruction
        elif instr[0] == 'A':  # If you've hit the end of your instruction set, determine the next step
            accepted.append(curr_path)
            return accepted
        elif instr[0] == 'R':
            return accepted
        else:
            accepted = recursive_check(instr[0], curr_path, accepted, instructions)
    return accepted

def part1(parsed_data):
    # Use a while loop to determine when you've hit the end for each part and return the sum of all accepted parts
    accepted = []
    for part in parsed_data[1]:
        curr_instr = 'in'
        while curr_instr not in ['R', 'A']:
            curr_instr = check(part, curr_instr, parsed_data[0])
        if curr_instr == 'A':
            accepted.append(part)
            print(f"The part with values {part} is accepted")
    return sum([sum(part.values()) for part in accepted])

def part2(parsed_data):
    # Recursively find all possible accepted paths and their respective switches that are required
    # Run through the accepted paths and find their boundaries for each letter and multiply the possible ranges
    # Return the sum of all possible values per accepted path
    path = {'x': [], 'm': [], 'a': [], 's': []}
    accepted = recursive_check('in', deepcopy(path), [], parsed_data[0])
    total = 0
    count = 1
    for line in accepted:
        curr_values = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]  # Start with the full possible value for each path
        for idx, char in enumerate(line):
            for item in line[char]:
                match item[0]:
                    case '<':  # If the operator is less than, and the upper end of the range is greater, set the new upper limit
                        if int(item[1:]) < curr_values[idx][1]:
                            curr_values[idx][1] = int(item[1:]) - 1
                    case '>': # If the operator is greater than, and the lower end of the range is lesser, set the new lower limit
                        if int(item[1:]) > curr_values[idx][0]:
                            curr_values[idx][0] = int(item[1:]) + 1
        t = 1  # Add the full possible values to the total
        for lo, hi in curr_values:
            t *= hi - lo + 1
        print(f"Accepted part {count} has {t} possible combinations")
        count += 1
        total += t
    return total

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total ratings for all accepted parts is {answer1}")
    print(f"PART2 - The number of distinct combinations of accepted ratings is {answer2}")