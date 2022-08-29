import random as r

def single_game(player_name):
    user_input = input()
    total_score = 0 
    dice = 0
    while user_input == "yes" or user_input == "y" and dice != 1 :
        print("rolling")
        dice = r.randrange(1,7)
        if dice == 1:
            total_score = 0 
            break
        else:
            total_score += dice
        print("total score is {}".format(total_score))

        print("Keep going? y, n")
        user_input = input()
    