from functools import reduce
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Run a bunch of splits to get a nice dictionary split by game id, dice pulls, and then color values for each pull
    data_dict = {}
    for line in data.splitlines():
        id_split = line.split(': ')  # Split by ': ' to get game id
        id_number = id_split[0].split(' ')[1]
        data_dict[id_number] = []
        for game in id_split[1].split('; '):  # Split by '; ' to separate each pull
            game_dict = {}
            for cubes in game.split(', '):  # Split by ', ' to separate each color value
                cube_value = cubes.split(' ')  # Split by ' ' to separate color from number and add to the individual game dict
                game_dict[cube_value[1]] = cube_value[0]
            data_dict[id_number].append(game_dict)

    return data_dict

def part1(parsed_data):
    # Run through all games and compare the values to the game_contains dict, return the sum of all possible game id
    total_value = 0
    bag_contains = {'red': '12', 'green': '13', 'blue': '14'}
    for game in parsed_data.keys():
        possible = True
        for pulls in parsed_data[game]:
            for color in pulls.keys():
                if int(pulls[color]) > int(bag_contains[color]):  # An impossible game claims to have more of a color than the bag contains
                    possible = False
                    print(f"Game {game} is not possible, there are {pulls[color]} {color}")
                    break
        if possible:
            print(f"Game {game} is possible!")
            total_value += int(game)  # Add the game id to the total_value

    return total_value

def part2(parsed_data):
    # Run through each game and find the highest pull for each color, return the product of all color values added together
    total_value = 0
    for game in parsed_data.keys():
        highest_value = {'red': '0', 'green': '0', 'blue': '0'}
        for pulls in parsed_data[game]:
            for color in pulls.keys():
                if int(highest_value[color]) < int(pulls[color]):  # If there is more of a certain color required, update the highest_value dict
                    highest_value[color] = pulls[color]
        product = reduce(lambda x, y: x*y, [int(highest_value[color]) for color in highest_value.keys()])  # Use the reduce function to multiply the values of all colors in the highest_value dict
        print(f"Game {game} has a minimum power of {product}")
        total_value += product

    return total_value

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total value of possible games is {answer1}")
    print(f"PART2 - The total power of the minimum set of cubes is {answer2}")