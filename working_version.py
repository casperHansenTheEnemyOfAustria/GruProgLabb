# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
import random as r

# Function
# Input: None
# Method: Runs program
# Output: None
def run():
    win_points = 5  # Points to win (decrease if testing)
    aborted = False # Variable for checking state of game anf ending if aborted
    players = get_players()    # ... this (method to read in all players)

    welcome_msg(win_points) # Sends welcoming message :)
    status_msg(players) # Sends status of how many players
    current = players[r.randint(0, len(players)-1)]  # TODO Set random player to start
    index = get_index(players, current) # Checks index for current player

    while current.totalPts < win_points and not aborted: # Checks if players has not won nor aborted
        for i in [((a + index) % len(players)) for a in range(len(players))]: #list comprehension, creating a new list that we are stepping through
            current = players[i]
            player_playing = True 
            aborted = single_round(current, player_playing, win_points, players) # If functions returns true game is aborted
            if aborted:
                break
    game_over_msg(current, aborted, players)

# Initializing player class
class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


# ---- Game logic methods --------------

# Function
# Input: None
# Method: Selects random integer from 1 to 6
# Output: Random integer from 1 to 6
def roll_result():
    dice_number = r.randint(1, 6)
    return dice_number

# Function
# Input: Array of players, Object of current player
# Method: Finds index in array for the current player
# Output: Index of input player in input array 
def get_index(players, current):
    for i in range(len(players)):
        if players[i] == current:
            return i

# Function
# Input: Player Object, Integer
# Method: Adds Integer to Player Objects rounts points
# Output: None
def regular_roll(current_player, dice_result): 
    current_player.roundPts += dice_result
    round_msg(dice_result, current_player)
    
# Function
# Input: Player Object
# Method: Sends out special message for rolling a 1 and resets Player Objects roiund points
# Output: None
def roll_one(current_player):
    round_msg(1, current_player)
    current_player.roundPts = 0

# Function
# Input: Player Object
# Method: Rolls and checks score ends round if roll is 1
# Output: Bool, to continue or not
def game_logic_instance(current_player):
    print(current_player.name + " rolled")
    result = roll_result() #rolls dice
    if result != 1:
        regular_roll(current_player, result) #method for rolling anothing other than a 1
        continue_playing = True
    else:
        roll_one(current_player) #method for rolling a 1
        continue_playing = False
    return continue_playing

# Function
# Input: Player Object
# Method: Adds up round points in to Players total points
# Output: Since rounds has ended function returns Bool, set False
def round_ender(player_to_be_added_points_to):
    player_to_be_added_points_to.totalPts += player_to_be_added_points_to.roundPts # adds up total points TODO: escape to other function
    player_to_be_added_points_to.roundPts = 0
    return False # returns false to set player playing

# Function
# Input: Player Object, Playing Bool, Points to win Integer, Array of players
# Method: Starts and runs a single round of the game aslso checks if players has won
# Output: Bool if player has won
def single_round(current_player, player_playing, winning_points, player_lst):
    while player_playing:
        player_choice = game_start_choice(current_player.name)
        # TODO move if sats to different function
        game_output = run_game(current_player, player_choice)
        game_end = game_output["game_ended"]
        player_playing = game_output["player_playing"]

        if current_player.totalPts >= winning_points or current_player.roundPts >= winning_points: # checks if current player has won. Double checks for current round to see if its a singel round win
            round_ender(current_player)
            game_end = game_over_msg(current_player, game_end, player_lst) # runs winning message and sets game to end
            break

    return game_end

# ---- IO Methods --------------

# Function
# Input: Player Object, Player choice String
# Method: Checks player choice and either runs game, aborts session or ends round 
# Output: Dict of two Bools to end a game or round
def run_game(player, player_choice):
    game_end = False
    if player_choice == "r":
        player_playing = game_logic_instance(player) # runs game logic
    elif player_choice == "n":
        player_playing = round_ender(player)
    elif player_choice == 'q':
        game_end = True
        player_playing = False
        abort_message(player)
    return {
        "game_ended": game_end,
        "player_playing": player_playing
    }

# Function
# Input: Player name String
# Method: Gets choice inout from player
# Output: Players choice String
def game_start_choice(player_name):
    print(player_name + ", do you want to roll or hold? (type r or n)")
    player_choice = str(input())
    while player_choice != "n" and player_choice != "r" and player_choice != "q":
        print("Wrong input, try again")
        player_choice = str(input())
    return player_choice

# Function
# Input: Player Object 
# Method: Prints message
# Output: None
def abort_message(player):
    print("aww, sad to see you go! :(" + str(player.name))

# Function
# Input: Amount of winning points Integer
# Method: Prints message containint winning amount of points
# Output: None
def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

# Function
# Input: Players Array
# Method: Prints out total points for each player
# Output: None
def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

# Function
# Input: Result Integer, Player Object
# Method: Checks if result is over 1 and prints different messages for the two
# Output: None
def round_msg(result, current_player):
    if result > 1:
        print("Got " + str(result) + " running total is " + str(current_player.roundPts) + " this round")
    else:
        print("Got 1 lost it all!")

# Function
# Input: Player Object, Abortion status Bool, Array of players
# Method: Checks if game is aborted or not and sends out different messages for each
# Output: Bool set to true for game over checks
def game_over_msg(player, is_aborted, player_lst):
    if is_aborted:
        print("Goodbye")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")
        print(player_lst[0].totalPts)
        score_board(player_lst)
    return True

# Function
# Input: Player Object
# Method: Gets input
# Output: None
def get_player_choice(player):
    input("Player is " + player.name + " > ")

# Function
# Input: None
# Method: Creates an array of newly created player objects
# Output: Array of players
def get_players():
    players = []
    while 1:
        try:
            n_players = int(input("How many players are there?"))
            for i in range(n_players):
                player = str(input(f"Player {i + 1} is >"))
                players.append(Player(name=player))
            break
        except ValueError:
            print("Type in an integer.")
            continue
    return players

# Function
# Input: Array of players
# Method: Prints out score board with total points of Player Objects
# Output: None 
def score_board(player_lst): # Dynamic score board. To look good, max characters in name 13, 
    print()
    print("*-------- SCORE BOARD --------*")
    print("*---  NAME  ------  SCORE  ---*")
    for i in range(len(player_lst)):
        mid_spacer = "--------------"
        for a in player_lst[i].name:
            mid_spacer = mid_spacer.replace('-', '', 1)
        for a in str(player_lst[i].totalPts):
            mid_spacer = mid_spacer.replace('-', '', 1)
        print("*---  " + player_lst[i].name + "  " + mid_spacer + "  " + str(player_lst[i].totalPts) + "   ---*")
    print("*-----------------------------*")
    print()

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
