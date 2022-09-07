import random as r

def game_logic():
    dice = r.randrange(1,7)
    message = "Fail" if dice == 0 else "Sucess"
    score = dice if dice != 0 else 0
    output = {
        "message": message,
        "score": score
    }
    return output  

def single_game(player_name):
    print("Hello! "+player_name+" do you want to start your round?")
    user_input = input()
    round_score = 0 
    while user_input == "yes" or user_input == "y" and dice != 1:
        print("rolling")
        if game_logic()["message"]:
            round_score = 0
            print("oops, next player")
            break
        else:
            round_score += game_logic()["score"]
        print(f"total score is {round_score}")

        print("Keep going? y, n")
        user_input = input()
    return round_score
# single_game("Casper")

# player.total_score += single_game(player.name)




