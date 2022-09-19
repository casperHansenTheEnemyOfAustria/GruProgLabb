from typing import List
from enum import Enum, auto
from random import *
from math import sqrt

import pygame as pg


#  Program to simulate segregation.
#  See : http:#nifty.stanford.edu/2014/mccown-schelling-model-segregation/
#

# Enumeration type for the Actors
class Actor(Enum):
    BLUE = auto()
    RED = auto()
    NONE = auto()  # NONE used for empty locations


# Enumeration type for the state of an Actor
class State(Enum):
    UNSATISFIED = auto()
    SATISFIED = auto()
    NA = auto()  # Not applicable (NA), used for NONEs

class Person:
    """Object for storing all cell data and counters"""
    def __init__(self, state: State, color:Actor) -> None:
        self.state = state
        self.color = color
        self.threshold = NeighborsModel.THRESHOLD

        self.friend_count = 0
        self.foe_count = 0

    def  check_neighbour_percentage(self) -> None:
        """checks the neighbour percentage and updates the state accordingly
            Args:
                self
        """
        if self.friend_count/(self.friend_count+self.foe_count) < self.threshold and has_neighbours(self) and is_person(self):
            set_unsatisfied(self)
            self.friend_count = 0
            self.foe_count = 0
        

    def poke(self, external_color:Actor) -> None:
        """When cell is poked. Compares color of poking cell and itself
            Args: 
                color of poing cell 
        """
        if external_color == self.color:    
            self.friend_count += 1
        else:
            self.foe_count += 1
        self.check_neighbour_percentage()

        pass
World = List[List[Actor]]  # Type alias


SIZE = 400


def neighbours():
    pg.init()
    model = NeighborsModel(SIZE)
    _view = NeighboursView(model)
    model.run()


class NeighborsModel:

    # Tune these numbers to test different distributions or update speeds
    FRAME_RATE = 1000000   # Increase number to speed simulation up
    DIST = [0.25, 0.25, 0.50]  # % of RED, BLUE, and NONE
    THRESHOLD = 0.8   # % of surrounding neighbours that should be like me for satisfaction

    # ########### These following two methods are what you're supposed to implement  ###########
    # In this method you should generate a new world
    # using randomization according to the given arguments.
    @staticmethod
    def __create_world(self, size:int) -> World:
        
        n_locations = size**2
        seed = generate_seed_2(n_locations, self.DIST)

        brave_new_world = make_matrix(seed, size)
        return brave_new_world

    #updates world
    def __update_world(self):
        poke_cells_around(self.world)
        self.world = move_cells(self.world)
        
        pass

    # ########### the rest of this class is already defined, to handle the simulation clock  ###########
    def __init__(self, size:int):
        self.world: World = self.__create_world(self, size)
        # self.world: World = test()
        self.observers = []  # for enabling discoupled updating of the view, ignore

    def run(self):
        clock = pg.time.Clock()
        running = True
        while running:
            running = self.__on_clock_tick(clock)
        # stop running
        print("Goodbye!")
        pg.quit()

    def __on_clock_tick(self, clock):
        clock.tick(self.FRAME_RATE)  # update no faster than FRAME_RATE times per second
        self.__update_and_notify()
        return self.__check_for_exit()

    # What to do each frame
    def __update_and_notify(self):
        self.__update_world()
        self.__notify_all()

    @staticmethod
    def __check_for_exit() -> bool:
        keep_going = True
        for event in pg.event.get():
            # Did the user click the window close button?
            if event.type == pg.QUIT:
                keep_going = False
        return keep_going

    # Use an Observer pattern for views
    def add_observer(self, observer):
        self.observers.append(observer)

    def __notify_all(self):
        for observer in self.observers:
            observer.on_world_update()


# ---------------- Helper methods ---------------------



#---------------World building methods----------------
def create_person(color: Actor):
    """creates person from given arguments
        Args:
            Color of the person
        Returns:
            the created person
    """
    if color == "red":
        person = Person(State.SATISFIED, Actor.RED)
    elif color == "blue":
        person = Person(State.SATISFIED, Actor.BLUE)
    else:
        person = Person(State.NA, Actor.NONE)
    return person

def generate_seed_2(n_locations:int, odds:list[int]) -> list[int]:
    """Generates seed from probability map
        Args:
            size of the map and the probability map
        Returns:
            flat list of where everythings going to be
    """
    red_amount = int(odds[0]*n_locations)
    blue_amount = int(odds[1]*n_locations)
    empty_amount = int(odds[2]*n_locations)

    flat_list = create_flat_list(red_amount, blue_amount, empty_amount)
    shuffle(flat_list)
    seed = flat_list

    return  seed
def create_flat_list(red_amount:int, blue_amount:int, empty_amount:int)  -> list[Person]:
    """creates a random flat list with all the abject in it according to the percentages given
        Args:
            amount of red, blue and empy cells
        Returns:
            a list of Person objects with all the amounts above
    """
    reds = [create_person("red")] * red_amount
    blues = [create_person("blue")] * blue_amount
    empties = [create_person("none")] * empty_amount

    return reds+blues+empties

def make_matrix(flat_list:list[Person], width:int) -> list[list[Person]]:
    """Makes a matrix with a precific width from a flat list
        Args:
            the flat list, the width of the matrix
        Returns:
            The newly created matrix
    """
    output_matrix = [flat_list[height*width: (height+1)*width] for height in range(width)]
    return output_matrix

#--------------Changing methods -------------------

def poke_cells_around(world:list[list[Person]]):
    """Pokes all cells aroud all cells
        Args:
            A matrix of the world
    """
    size = len(world)
    for y, row in enumerate(world, start=0):
        #checks row index for lenghth incase canvas is not square
        for x in range(len(row)):
            current = world[y][x]
            if is_person(current): #checks so thats the index actually has an actor
                indexes_to_be_poked = set_poke_indexes(x, y)

                for index in indexes_to_be_poked: #checks if indexes are valid and pokes the valid ones
                    if is_valid_location(size, index[1], index[0]): #checks if location is valid
                        world[index[1]][index[0]].poke(current.color)
                  
def is_person(person:Person) -> bool:
    """checks if input item is empty square or person
        Args:
            person object
        Returns:
            Bool for if it is empty or person
    """
    if person.color == Actor.NONE:
        return False
    return  True
    

def set_satisfied(person:Person):
    """sets person state to satisfied
        Args:
            person object
    """
    person.state = State.SATISFIED

def set_unsatisfied(person):
    """sets person state to unsatisfied
        Args:
            person object
    """
    person.state = State.UNSATISFIED


def has_neighbours(item:Person) -> bool:
    """Checks if there are any neighbours around the given item
        Args:
            a Person object to be checked
        Returns:
            A bool of wther the object has neighbours or not
    """
    if item.friend_count+item.foe_count == 0: 
        return False
    else:
        return True

def move_cells(world:list[list[Person]]) -> list[list[Person]]:
    """Moves cells that are unsatisfied to new empty spaces
        Args:
            The world matrix
        Returns:
            The new updated world matrix
    """
    empty_indexes = find_empty_indexes(world)
    for i, row in enumerate(world, start = 0):
        for j, item in enumerate(row, start = 0):
            if item.state == State.UNSATISFIED:
                    color = item.color
                    random_empty_place = find_random_empty_place(empty_indexes)
                    #creates new object at emplty index
                    world = create_new_object_at_empty_index(random_empty_place, world, color)
                    #add an empty object at the old index
                    world[i][j] = clear()
                    # adds the newly cleared index to the empty list
                    empty_indexes.append([i,j])
    return world
                    
def find_random_empty_place(empty_indexes:list[list[int]]):
    """checks throug hempty indexes and finds a random one
        Args:
            List of empty indexes
        Returns:
            a random one in the list
    """
    i = randint(0, len(empty_indexes)-1)
    random_empty_place = empty_indexes[i]
    del empty_indexes[i] # removes the used index from the empty indexes list
    return random_empty_place

def create_new_object_at_empty_index(empty_place:list[int], world:list[list[Person]], color:Actor) -> list[list[Person]]:
    """Creates new object at an index
        Args:
            Empty index[x and y, the world matrix, color of the actor to be created
    """
    world[empty_place[0]][empty_place[1]] = Person(State.SATISFIED, color)
    return world

def clear() -> Person:
    """Creates an empty player
        Returns: empty player
    """
    return Person(State.NA, Actor.NONE)

def find_empty_indexes(world:list[list[Person]]) -> list[list[int]]:
    """Finds empty indexes in the world
        Args:
            The world matrix
        Returns:
            All empty indexes in world
    """
    output = []
    for i, row in enumerate(world, start = 0):
        for j, item in enumerate(row, start = 0):
            if item.color == Actor.NONE:
                output.append([i,j])
    return output

def set_poke_indexes(current_x: int, current_y: int) -> list[list[int]]:
    """Sets the indexes thats are to be poked
    """
    x1 = current_x + 1
    x2 = current_x - 1
    y1 = current_y + 1
    y2 = current_y - 1
    output = [
        [x1, current_y],
        [x2, current_y],
        [current_x, y1],
        [current_x, y2],
        [x1, y1],
        [x2, y1],
        [x1, y2],
        [x2, y2]    
    ]
    return output


    # Check if inside world
def is_valid_location(size: int, row: int, col: int) -> bool:
    return 0 <= row < size and 0 <= col < size


# ------- Testing -------------------------------------

# Here you run your tests i.e. call your logic methods
# to see that they really work
def test():
    # A small hard coded world for testing
    test_world = [
        [Person(State.SATISFIED, Actor.RED), Person(State.SATISFIED, Actor.RED), Person(State.NA, Actor.NONE)],
        [Person(State.NA, Actor.NONE), Person(State.SATISFIED, Actor.BLUE), Person(State.NA, Actor.NONE)],
        [Person(State.SATISFIED, Actor.RED), Person(State.NA, Actor.NONE), Person(State.SATISFIED, Actor.BLUE)]
    ]
     
    th = 0.5  # Simpler threshold used for testing

    size = len(test_world)
    print(is_valid_location(size, 0, 0))
    print(not is_valid_location(size, -1, 0))
    print(not is_valid_location(size, 0, 3))
    print(is_valid_location(size, 2, 2))

    # TODO More tests
    return test_world
    exit(0)


# Helper method for testing
def count(a_list, to_find):
    the_count = 0
    for a in a_list:
        if a == to_find:
            the_count += 1
    return the_count


# ###########  NOTHING to do below this row, it's pygame display stuff  ###########
# ... but by all means have a look at it, it's fun!
class NeighboursView:
    # static class variables
    WIDTH = 2000  # Size for window
    HEIGHT = 1000
    MARGIN = 10

    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    BLUE  = (  0,   0, 255)

    # Instance methods

    def __init__(self, model: NeighborsModel):
        pg.init()  # initialize pygame, in case not already done
        self.dot_size = self.__calculate_dot_size(len(model.world))
        self.screen = pg.display.set_mode([self.WIDTH, self.HEIGHT])
        self.model = model
        self.model.add_observer(self)

    def render_world(self):
        # # Render the state of the world to the screen
        self.__draw_background()
        self.__draw_all_actors()
        self.__update_screen()

    # Needed for observer pattern
    # What do we do every time we're told the model had been updated?
    def on_world_update(self):
        self.render_world()

    # private helper methods
    def __calculate_dot_size(self, size):
        return max((self.WIDTH - 2 * self.MARGIN) / size, 2)

    @staticmethod
    def __update_screen():
        pg.display.flip()

    def __draw_background(self):
        self.screen.fill(NeighboursView.WHITE)

    def __draw_all_actors(self):
        for row in range(len(self.model.world)):
            for col in range(len(self.model.world[row])):
                self.__draw_actor_at(col, row)

    def __draw_actor_at(self, col, row):
        color = self.__get_color(self.model.world[row][col].color)
        xy = self.__calculate_coordinates(col, row)
        pg.draw.circle(self.screen, color, xy, self.dot_size / 2)

    # This method showcases how to nicely emulate 'switch'-statements in python
    @staticmethod
    def __get_color(actor):
        return {
            Actor.RED: NeighboursView.RED,
            Actor.BLUE: NeighboursView.BLUE
        }.get(actor, NeighboursView.WHITE)

    def __calculate_coordinates(self, col, row):
        x = self.__calculate_coordinate(col)
        y = self.__calculate_coordinate(row)
        return x, y

    def __calculate_coordinate(self, offset):
        x: float = self.dot_size * offset + self.MARGIN
        return x


if __name__ == "__main__":
    neighbours()
