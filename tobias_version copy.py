# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
import random as r

def run():
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    # Hard coded players, replace *last* of all with ... (see below)
    players = [Player(name='Olle'), Player(name='Fia')]
    # players = getPlayers()    # ... this (method to read in all players)

    welcome_msg(win_points)
    status_msg(players)
    current = players[r.randint(0, len(players)-1)]  # TODO Set random player to start
    index = get_index(players, current)
    # TODO Game logic, using small step, functional decomposition

    while current.totalPts < win_points and not aborted:
            for i in [((a + index) % len(players)) for a in range(len(players))]:
                current = players[i]
                player_playing = True
                aborted = single_round(current, player_playing, win_points)
                if aborted:
                    break
    game_over_msg(current, aborted)


class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


# ---- Game logic methods --------------
# TODO
def roll_result():
    dice_number = r.randint(1, 6)
    return dice_number


def get_index(players, current):
    for i in range(len(players)):
        if players[i] == current:
            return i

def regular_roll(current_player, dice_result):
    print(f"You rolled {dice_result}")
    current_player.roundPts += dice_result

def roll_one(current_player):
    print(f"You rolled 1 and all your points are lost :(")
    current_player.roundPts = 0
    current_player.totalPts = 0
    
def game_logic_instance(current_player):
    print(current_player.name + " rolled")
    result = roll_result()
    if result != 1:
        regular_roll(current_player, result)
        continue_playing = True
    else:
        roll_one(current_player)
        continue_playing = False
    return continue_playing

def single_round(current_player, player_playing, winning_points):
    while player_playing:
        aborted = False
        print()
        print(current_player.name + ", do you want to roll or hold? (type r or n)")
        player_choice = str(input())
        if player_choice == "r":
            player_playing = game_logic_instance(current_player)
        elif player_choice == "n":
            current_player.totalPts += current_player.roundPts
            player_playing = False
        else:
            aborted = True
            player_playing = False
            print("aww, sad to see you go! :(")
        if current_player.totalPts >= winning_points or current_player.roundPts >= winning_points:
            aborted = True
            print("woaaa epic win!!")
            break
            
        print(f"{current_player.name} got a total of {current_player.roundPts} points this round")  
    return aborted
# ---- IO Methods --------------

def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")


def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")


def round_msg(result, current_player):
    if result > 1:
        print("Got " + result + " running total are " + current_player.roundPts)
    else:
        print("Got 1 lost it all!")


def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Goodbye")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")


def get_player_choice(player):
    input("Player is " + player.name + " > ")


def get_players():
    # TODO
    pass


# ----- Testing -----------------
# Here you run your tests i.e. call your game logic methods
# to see that they really work (IO methods not tested here)
def test():
    # This is hard coded test data
    # An array of (no name) Players (probably don't need any name to test)
    test_players = [Player(), Player(), Player()]
    # TODO Use for testing of logical methods (i.e. non-IO methods)


if __name__ == "__main__":
    run()
