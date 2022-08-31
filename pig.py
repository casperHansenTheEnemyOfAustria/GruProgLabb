import random as r

    

def single_game(player_name):
    print("Hello! "+player_name+" do you want to start your round?")
    user_input = input()
    round_score = 0 
    dice = 0
    while user_input == "yes" or user_input == "y" and dice != 1:
        print("rolling")
        dice = r.randrange(1,7)
        if dice == 1:
            round_score = 0
            print("oops, next player")
            break
        else:
            round_score += dice
        print(f"total score is {round_score}")

        print("Keep going? y, n")
        user_input = input()
    return round_score
# single_game("Casper")

# player.total_score += single_game(player.name)