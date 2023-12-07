from itertools import groupby
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split each into a list of [hand, value] lists and return that list
    data_list = [line.split() for line in data.splitlines()]  
    return data_list

def determine_hand(hand, part2=False):
    # Take the hand, and group all letters together and sort them based on number of cards.  
    # Return the position they should be in based on length of the letter with the most in the hand
    # If it's part 2, count the number of jokers, remove all jokes before grouping, and then add that many to the highest value card
    if part2:
        j = hand.count('J')
        hand = hand.replace('J', '')
    grouped = sorted([list(g) for _, g in groupby(''.join(sorted(hand)))], key=len, reverse=True)  # Reverse makes sure it's sorted from most cards to least cards
    if part2:
        for _ in range(j):
            grouped[0].append(grouped[0][0])  # Just append the same value to the first entry in grouped j number of times
    if len(set(hand)) == 2:  # Only checks full four of a kind or full house
        return 5 if len(grouped[0]) == 4 else 4  # If the length of the highest in grouped is 4, it's a four of a kind, if it's 3, it's a full house
    else:  # Only checks three of a kind or two pair
        return 3 if len(grouped[0]) == 3 else 2  # If the length of the highest in grouped is 3, it's a three of a kind, if it's 2, it's a two pair
    
def sort_hands(data, part2=False):
    # Sort the hands by the length of the hand in a set.  If the len(set(hand)) is between 2 and 3, it needs to determined separately, and return the sorted hands
    # If it's part2, remove all Js before determining the length of the set
    types = [[] for _ in range(7)]  # List of lists for all the possible hands
    for hand in data:
        hand_length = len(set(hand[0])) if not part2 else len(set(hand[0].replace('J', '')))
        if hand_length <= 1:  # If there's only one, it's a five of a kind and it would come out to 0 if it were all jokers for part2
            types[6].append(hand)
        elif hand_length in range(2 , 4):
            types[determine_hand(hand[0], part2)].append(hand)
        else:  # If the set length is 4 or 5, it's a one pair or high card respectively, so append to the beginning
            types[5 - hand_length].append(hand)
    return types

def print_range(combined_list):
    # This could be done with a shorter command, but I like to have some sort of an output
    for idx, hand in enumerate(combined_list):
        print(f"{hand[0]} was rank {idx + 1}")
        yield int(hand[1]) * (idx + 1)

def sort_power_and_combine(sorted_hands, order):
    # This takes the expected order and returns a combined list of all hands sorted by the order provided
    sorted_power = [[] for _ in range(7)]
    for idx, hand_list in enumerate(sorted_hands):
        sorted_power[idx] = sorted(hand_list, key=lambda x: [order.index(c) for c in x[0] if c in order]) # Sort each hand type by provided order list
    combined_list = [[x, y] for nested_list in sorted_power for x, y in nested_list]  # Combine them all into a single list that will mean index + 1 is their rank
    return combined_list

def part1(parsed_data):
    # Sort the hands, combine them into a single list, and add the power level of each hand together
    sorted_hands = sort_hands(parsed_data)

    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    combined_list = sort_power_and_combine(sorted_hands, order)

    return sum(print_range(combined_list))

def part2(parsed_data):
    # Sort the hands using the part2 trigger, combine them into a single list with the J change, and add the power level of each hand together
    sorted_hands = sort_hands(parsed_data, True)

    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    combined_list = sort_power_and_combine(sorted_hands, order)
    
    return sum(print_range(combined_list))

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total winnings are {answer1}")
    print(f"PART2 - The total winnings are {answer2}")