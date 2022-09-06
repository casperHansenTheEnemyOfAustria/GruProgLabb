# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
from random import randint



def run():
    """
        Runs program
    """
    win_points = 5  # Points to win (decrease if testing)
    aborted = False # Variable for checking state of game anf ending if aborted
    players = get_players()    # ... this (method to read in all players)

    welcome_msg(win_points) # Sends welcoming message :)
    status_msg(players) # Sends status of how many players
    current = players[randint(0, len(players)-1)]  # TODO Set random player to start
    index = players.index(current) # Checks index for current player

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


def roll_result(max:int = 6):
    """This function generates a random number between 1 and the input with a default max of 6

    Args:
        max (Integer, optional): range of roll,  defaults to 6.

    Returns:
        (Integer) randomly generated integer
    """
    return randint(1, max)

#-----------Unused-----------
# def get_index(players, current):
#     """Finds index in array for the current player

#     Args:
#         (Array) players, (Object) current player

#     Returns
#         (Integer) index of player

#     """

#     for i in range(len(players)):
#         if players[i] == current:
#             return i


def regular_roll(current_player, dice_result): 
    """Adds Integer to Player Objects rounts points

    Args:
        (Object) player, (Integer) dice result

    """
    current_player.roundPts += dice_result
    round_msg(dice_result, current_player)
    

def roll_one(current_player):
    """Sends out special message for rolling a 1 and resets Player Object's round points

    Args: 
        (Object) player

    """
    round_msg(1, current_player)
    current_player.roundPts = 0


def game_logic_instance(current_player):
    """Rolls and checks score ends round if roll is 1

    Args:
        (Object) player

    Retruns:
        (Bool) to continue or not
    """
    print(current_player.name + " rolled")
    result = roll_result() #rolls dice
    if result != 1:
        regular_roll(current_player, result) #method for rolling anothing other than a 1
        continue_playing = True
    else:
        roll_one(current_player) #method for rolling a 1
        continue_playing = False
    return continue_playing

def round_ender(player_to_be_added_points_to):
    """Adds up round points in to Players total points

    Args: 
        (Object) player

    Returns:
        (Bool) Set to false
        
    """
    player_to_be_added_points_to.totalPts += player_to_be_added_points_to.roundPts # adds up total points TODO: escape to other function
    player_to_be_added_points_to.roundPts = 0
    return False # returns false to set player playing

def single_round(current_player, player_playing, winning_points, player_lst):
    """Starts and runs a single round of the game aslso checks if players has won
    
    Args: 
        (Object) player, (Bool) playing?, (Integer) points to win, (Array) players
    
    Returns:
        (Bool) if player has won
    
    """
    while player_playing:
        player_choice = game_start_choice(current_player.name)
        # TODO move if sats to different function
        game_end, player_playing = run_game(current_player, player_choice)

        if current_player.totalPts >= winning_points or current_player.roundPts >= winning_points: # checks if current player has won. Double checks for current round to see if its a singel round win
            round_ender(current_player)
            game_end = game_over_msg(current_player, game_end, player_lst) # runs winning message and sets game to end
            break

    return game_end

# ---- IO Methods --------------

def run_game(player, player_choice):
    """Checks player choice and either runs game, aborts session or ends round 
    
    Args:
        (Object ) player, (String) player choice
    
    Returns: 
        (Bool) Eng game?, (Bool) End round?
        
    """
    game_end = False
    if player_choice == "r":
        player_playing = game_logic_instance(player) # runs game logic
    elif player_choice == "n":
        player_playing = round_ender(player)
    elif player_choice == 'q':
        game_end = True
        player_playing = False
        abort_message(player)
    return game_end, player_playing

def game_start_choice(player_name):
    """Gets choice inout from player

    Args: 
        (String) player name

    Returns:
        (String) player choice

    """
    print(player_name + ", do you want to roll or hold? (type r or n)")
    player_choice = str(input())
    while player_choice != "n" and player_choice != "r" and player_choice != "q":
        print("Wrong input, try again")
        player_choice = str(input())
    return player_choice

def abort_message(player):
    """Prints message for ending session
    """
    print("aww, sad to see you go! :(" + str(player.name))

def welcome_msg(win_pts):
    """Prints message containint winning amount of points

    Args:
        (Integer) Amound of winning points

    """
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

def status_msg(the_players):
    """Prints out total poitns for each player

    Args:
        (Array) players

    """
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

def round_msg(result, current_player):
    """Checks if result is over 1 and prints different messages for the two

    Args:
        (Integer) result, (Object) player

    """
    if result > 1:
        print("Got " + str(result) + " running total is " + str(current_player.roundPts) + " this round")
    else:
        print("Got 1 lost it all!")

def game_over_msg(player, is_aborted, player_lst):
    """Checks if game is aborted or not
    
    Args:
        (Object) player, (Bool) aborted?, (Array) players

    Returns:
        (Bool) True

    """
    if is_aborted:
        print("Goodbye")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")
        score_board(player_lst)
    return True

def get_player_choice(player):
    """Prints player name
    
    Args: (Object) player

    """
    input("Player is " + player.name + " > ")

def get_players():
    """Creates an array of players of the desired length
        
    Returns: (Array) players'

    """
    players = []
    while 1:
        try:
            n_players = int(input("How many players are there?"))
            for i in range(n_players):
                players = create_player(players, i)
            break
        except ValueError:
            print("Type in an integer.")
            continue
    return players

def create_player(player_array, index):
    """Creates players

    Args: 
        (Array) for players, (Integer) The index of the player to be created

    Returns: 
        (Array) all the newly created players

    """
    name = str(input(f"Player {index + 1} is >"))
    player = Player(name)
    player_array.append(player)
    return player_array

def score_board(player_lst): 
    """Prints out a dynamic score board

    Args: 
        (Array) list of players MAXIMUM LENGTH 13
    
    """
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
