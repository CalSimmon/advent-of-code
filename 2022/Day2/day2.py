def part1(data):
    opponent = ["A", "B", "C"]
    you = ["X", "Y", "Z"]
    total_score = 0
    for line in data.splitlines():
        game = line.split()
        game_score = 0
        opp_ind = opponent.index(game[0])
        you_ind = you.index(game[1])
        game_result = opp_ind - you_ind
        game_score += you_ind + 1
        if game_result == 0:
            game_score += 3
        if game_result == -1 or game_result == 2:
            game_score += 6
        total_score += game_score
    print(f"Your total score is {total_score}.")
    
def part2(data):
    opponent = ["A", "B", "C"]
    wl = ["X", "Y", "Z"]
    total_score = 0
    for line in data.splitlines():
        game = line.split()
        game_score = 0
        opp_ind = opponent.index(game[0])
        indicator = wl.index(game[1])
        you = 0
        game_score += indicator * 3
        if indicator == 0:
            you = opp_ind - 1
        if indicator == 1:
            you = opp_ind
        if indicator == 2:
            you = opp_ind + 1
        if you == -1:
            you = 2
        if you == 3:
            you = 0
        game_score += you + 1
        total_score += game_score
    print(f"Your total score is {total_score}.")


if __name__ == "__main__":
    with open("day2input.txt", "r") as f:
        data = f.read()
    part1(data)
    part2(data)