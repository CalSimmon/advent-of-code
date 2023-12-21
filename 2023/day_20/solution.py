from copy import deepcopy
from math import lcm
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Convert the output to a dictionary, add other identifiers, and return the output of determine_con_out to pull conjunction outputs
    data_list = [line.split(' -> ') for line in data.splitlines()]
    data_dict = {}
    for item in data_list:
        if item[0] != 'broadcaster':
            match item[0][0]:
                case '%':  # For flip-flop modules, split into type, output, boolean status
                    data_dict[item[0][1:]] = {'type': item[0][0], 'output': item[1].split(', '), 'status': False}
                case '&':  # For conjunction modules, split into type, output, dictionary status
                    data_dict[item[0][1:]] = {'type': item[0][0], 'output': item[1].split(', '), 'status': {}}
        else:  # Broadcaster module has no type or status
            data_dict[item[0]] = {'type': None, 'output': item[1].split(', '), 'status': None}
    return determine_con_out(data_dict)

def determine_con_out(data_dict):
    # If a module outputs to a conjunction module, list the input module in the output's status and return the updated dictionary
    for key in data_dict.keys():
        for module in data_dict[key]['output']:
            if module in data_dict.keys():
                if data_dict[module]['type'] == '&':
                    data_dict[module]['status'][key] = 'L'
    return data_dict

def process_pulse(modules, origin, strength, targets):
    # For each pulse, follow the rules from the instructions based on the output strength and targets,
    # yield the new outputs generated by each pulse
    for target in targets:
        if target in modules.keys():  # Only process if there is a module for the target
            if target == 'broadcaster':  # Maintain strength for broadcaster
                yield [target, strength, modules[target]['output']], modules
            elif modules[target]['type'] == '%':  # For flip-flop, if turning on send high pulse, and if turning off send low pulse
                if strength == 'L':
                    if not modules[target]['status']:  # Turning on
                        modules[target]['status'] = not modules[target]['status']
                        yield [[target, 'H', modules[target]['output']], modules]
                    else:  # Turning off
                        modules[target]['status'] = not modules[target]['status']
                        yield [[target, 'L', modules[target]['output']], modules]
            else:  # For conjunction modules, update origin's status in target module, and if all match high, send low pulse, else send high pulse
                modules[target]['status'][origin] = strength
                con_status = list(set(modules[target]['status'].values()))
                if len(con_status) == 1 and con_status[0] == 'H':
                    yield [[target, 'L', modules[target]['output']], modules]
                else: 
                    yield [[target, 'H', modules[target]['output']], modules]
        else:
            pass

def part1(parsed_data):
    # Use a queue to run through each output of a button press, until queue empties,
    # repeat 1000 times, and return the production of the number of low pulses and high pulses
    module_dict = deepcopy(parsed_data)
    count = [0, 0]
    for _ in range(1000):
        queue = [['button', 'L', ['broadcaster']]]  # Start with the pulse from the button
        while queue:
            q = queue.pop(0)
            match q[1]:
                case 'L': count[0] += len(q[2])
                case 'H': count[1] += len(q[2])
            for item in process_pulse(module_dict, *q):
                queue.append(item[0])
                module_dict = item[1]  # Update module map each full pulse
    print(f"There were {count[0]} low pulses and {count[1]} high pulses")
    return count[0] *  count[1]

def part2(parsed_data):
    # Since there are a number of conjunction modules that lead into the rx output module, find those modules, and determine what button press they 
    # will turn to a high pulse, indicating a low pulse from the dh module to rx, then return the lowest common multiple of all
    module_dict = deepcopy(parsed_data)
    for key in module_dict.keys():  # Find the conjunction module that outputs to rx
        if 'rx' in module_dict[key]['output']:
            final_con = key
    final_inputs = {}
    for key in module_dict.keys():  # Find the modules that output to the final conjunction module and set those to False
        if module_dict[key]['type'] == '&':
            if final_con in module_dict[key]['output']:
                final_inputs[key] = False
    count = 0
    while not all(final_inputs.values()):  # While all final inputs are still false, loop
        count += 1
        queue = [['button', 'L', ['broadcaster']]]
        while queue:
            q = queue.pop(0)
            for item in process_pulse(module_dict, *q):
                queue.append(item[0])
                module_dict = item[1]
            for key in module_dict[final_con]['status']:  # Check the conjunction modules that lead into final_con and if they have a high pulse, record how many presses it took
                if not final_inputs[key] and module_dict[final_con]['status'][key] == 'H':
                    print(f"Module {key} took {count} number of button presses before it produced a high pulse")
                    final_inputs[key] = count
    return lcm(*final_inputs.values())

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The product of the total pulses for 1000 presses is {answer1}")
    print(f"PART2 - The number of button presses to start the final machine is {answer2}")