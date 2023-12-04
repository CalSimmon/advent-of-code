import re
from math import pow
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "inputs/input.txt")
# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(data):
    # Split the input into lines, remove the card identifier, split by number types, and then separate each individual number
    cards = [[re.split(r'\s+', part.strip()) for part in row.split(': ')[1].split(' | ')] for row in data.splitlines()]
    return cards

def part1(parsed_data):
    # Compare the numbers in the first section to the numbers in the second and return 2 to the power of the number of cards won minus one
    total_value = 0
    for card_number, card in enumerate(parsed_data):
        won = 0
        print(f"Card {card_number + 1} had the following winning numbers:")
        for number in card[0]:
            if number in card[1]:
                won += 1
                print(number)
        card_value = pow(2, (won - 1)) if won > 0 else 0  # Ensures that you aren't getting a negative exponent
        total_value += card_value
        print("Card {} had a value of {:.0f}".format((card_number + 1), card_value))
    return total_value

def part2(parsed_data):
    # Track how many cards are added at which position, and then return total number of cards
    number_of_cards = [1 for _ in range(len(parsed_data))]  # All cards start with one
    for card_number, card in enumerate(parsed_data):
        won = 0
        for number in card[0]:
            if number in card[1]:
                won += 1 
        for i in range(won):
            number_of_cards[card_number + (i + 1)] += (1 * number_of_cards[card_number])  # Multiply 1 by the number of times the card would add
        print(f"Card {card_number + 1} won {won * number_of_cards[card_number]} extra cards.")
    return sum(number_of_cards)

if __name__ == "__main__":
    with open(INPUT_PATH , "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)
    
    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print("PART1 - The total point value of the cards is {:.0f}".format(answer1))
    print(f"PART2 - The total cards at the end is {answer2}")