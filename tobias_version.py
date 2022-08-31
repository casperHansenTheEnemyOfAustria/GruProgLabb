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
                while player_playing:
                    print()
                    print(current.name + ", do you want to roll or hold? (type r or n)")
                    player_choice = str(input())
                    if player_choice == "r":
                        print(current.name + " rolled")
                        result = roll_result()
                        if result != 1:
                            print(f"You rolled {result}")
                            current.roundPts += result
                        else:
                            print(f"You rolled {result} and all your points are lost")
                            current.roundPts = 0
                            current.totalPts = 0
                            player_playing = False

                    elif player_choice == "n":
                        current.totalPts = players[i].roundPts
                        player_playing = False

                    else:
                        aborted = True
                        player_playing = False

                    print(f"{current.name} got a total of {current.roundPts} points this round")

            if current.totalPts >= win_points and not aborted:
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
        print("Aborted")
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
