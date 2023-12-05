from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example2.txt")

def parse_input(data):
    # Split each section of the almanac into a dictionary which each heading of the secion as the key
    # Then split all lines below each heading into a list as the value of the heading
    # Return almanac dictionary
    almanac = {}
    data_list = [section.split(':') for section in data.split('\n\n')]
    for section in data_list:
        almanac[section[0].replace(' map', '')] = [line.split(' ') for line in section[1].strip().split('\n')]
    return almanac

def check_conversion_map(seed, conversion_map):
    # This checks the input conversion map and returns the altered value based on the difference between the seed value and source value
    # If not in the range, return itself
    for line in conversion_map:
        if int(seed) >= int(line[1]) and int(seed) < (int(line[1]) + int(line[2])):
            return (int(line[0]) + (int(seed) - int(line[1])))
    return int(seed)

def conversion_map_to_range(conversion_map):
    # Convert the input conversion map into a nested list where each item is a list of start, end, and amount to offset if matched, return sorted nested list
    # For instance, [50, 98, 2] becomes [98, 99, -48]
    conversion_list = []
    for line in conversion_map:
        conversion_list.append([int(line[1]), (int(line[1]) + int(line[2]) - 1), (int(line[0]) - int(line[1]))])
    return sorted(conversion_list, key=lambda x: x[0])

def convert_seed_range_list(seed_range, conversion_range):
    # For part 2, take the seed_range and convert it to a list of ranges based on the conversion_range and return sorted nested list
    seed_range_list = []
    curr_value = seed_range[0]
    for i in range(len(conversion_range)):
        if curr_value < conversion_range[i][0]:  # If the first entry in conversion_range is higher than lowest seed, add range until that point
            seed_range_list.append([int(curr_value), (int(conversion_range[i][0] - 1))])
            curr_value = int(conversion_range[i][0])
        if curr_value >= int(conversion_range[i][0]) and curr_value <= int(conversion_range[i][1]):  # If between the current conversion range, add the range, unless we are at the end of the seed range
            max_value = int(conversion_range[i][1]) if not int(seed_range[1]) <= int(conversion_range[i][1]) else int(seed_range[1])  # Set max value to seed range end if conversion range is higher than seed range
            seed_range_list.append([(curr_value + conversion_range[i][2]), (max_value + conversion_range[i][2])])
            curr_value = max_value + 1
        if curr_value - 1 == int(seed_range[1]):  # If we've hit the end of the seed range, break
            break
    if curr_value < seed_range[1]:  # If we did not hit the end of the seed range, add the rest of the range
        seed_range_list.append([curr_value, seed_range[1]])
    
    return sorted(seed_range_list, key=lambda x: x[0])

def part1(parsed_data):
    # Run through the seeds and find the location then return the lowest location number
    lowest = None
    for seed in parsed_data['seeds'][0]:
        curr_soil = seed
        for cm in parsed_data.keys():
            if cm != 'seeds':
                curr_soil = check_conversion_map(curr_soil, parsed_data[cm])
        print(f"Seed {seed} has a location number of {curr_soil}")
        if lowest is None or int(curr_soil) < lowest:
            lowest = int(curr_soil)

    return lowest

def part2(parsed_data):
    # Get all seed pairs and conversion maps, and run through each seed pair to find the lowest location number within the range
    # Return the lowest location number of all seed ranges
    seeds = parsed_data['seeds'][0]
    lowest = None
    seed_pairs = [[int(seeds[i]), (int(seeds[i]) + int(seeds[i + 1]) - 1)] for i in range(0, len(seeds), 2)]  # Convert the pairs to a range of seed values
    conversion_maps = [cm for cm in parsed_data.keys() if cm != 'seeds']
    conversion_range_dict = {}
    for cm in conversion_maps:  # Convert the conversion maps into a dict of conversion ranges based on the map
        conversion_range_dict[cm] = conversion_map_to_range(parsed_data[cm])
    for seed_range in seed_pairs:
        curr_seed_range = [seed_range.copy()]  # Convert the first seed pair into a nested list so the future loops will function properly
        for curr_conv_map in conversion_range_dict.keys():
            curr_output_list = []
            for entry in curr_seed_range:
                output_list = convert_seed_range_list(entry, conversion_range_dict[curr_conv_map])  # Output the new range for each seed range supplied
                curr_output_list.append(output_list)  
            curr_output_list = [item for sublist in curr_output_list for item in sublist]  # Make sure output is only a single nested list sorted
            curr_output_list = sorted(curr_output_list, key=lambda x: x[0])
            curr_seed_range = curr_output_list.copy()  # Set the curr seed range to the output list and run through the next conversion map
        print(f"The lowest of seed range {seed_range} is {curr_seed_range[0][0]}")

        if lowest is None or curr_seed_range[0][0] < lowest:
            lowest = curr_seed_range[0][0]
        
    return lowest

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The lowest location number is {answer1}")
    print(f"PART2 - The lowest location number of seed ranges is {answer2}")