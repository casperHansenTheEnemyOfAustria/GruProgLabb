from asyncio.windows_events import NULL
from multiprocessing import current_process
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

    def __init__(self, state, color) -> None:
        self.state = state
        self.color = color
        
        self.friend_count = 0
        self.foe_count = 0

        
    def poke(self, external_color):
        if external_color == self.color:    
            self.friend_count += 1
        else:
            self.foe_count += 1
        

            
        
        pass
World = List[List[Actor]]  # Type alias


SIZE = 30


def neighbours():
    pg.init()
    model = NeighborsModel(SIZE)
    _view = NeighboursView(model)
    model.run()


class NeighborsModel:

    # Tune these numbers to test different distributions or update speeds
    FRAME_RATE = 20        # Increase number to speed simulation up
    DIST = [0.20, 0.20, 0.60]  # % of RED, BLUE, and NONE
    THRESHOLD = 0.8   # % of surrounding neighbours that should be like me for satisfaction

    # ########### These following two methods are what you're supposed to implement  ###########
    # In this method you should generate a new world
    # using randomization according to the given arguments.
    @staticmethod
    def __create_world(self, size) -> World:
        # TODO Create and populate world according to self.DIST distribution parameters
        n_locations = size**2
        prob_map = create_probability_map(self.DIST)
        seed = generate_seed(n_locations, prob_map)

        brave_new_world = generate_matrix_from_seed(seed, size)
        return brave_new_world

    # This is the method called by the timer to update the world
    # (i.e move unsatisfied) each "frame".
    def __update_world(self):
        poke_cells_around(self.world)
        update_cells(self)
        self.world = move_cells(self.world)
        # TODO Update logical state of world based on self.THRESHOLD satisfaction parameter
        pass

    # ########### the rest of this class is already defined, to handle the simulation clock  ###########
    def __init__(self, size):
        self.world: World = self.__create_world(self, size)
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

def create_probability_map(chances):
    output = []
    for prob in range(len(chances)):
        for i in range(int(100*chances[prob])):
            output.append(prob)   
    return output

def generate_seed(n_locations, odds):
    seed =[]
    for i in range(n_locations):
        random_state = randint(0, len(odds)-1)
        color = assign_seed_colors(odds[random_state])
        seed.append(color)
    return  seed

def assign_seed_colors(number):
    if number == 0:
        return "red"
    elif number == 1:
        return "blue"
    else:
        return "empty"
   
def generate_matrix_from_seed(seed, size):
        height = size
        empty_matrix = generate_matrix_height(height)
        width = size
        print(f"width: {width}")
        print(f"height: {height}")
        empty_matrix = insert_people_into_matrix(width, empty_matrix, seed)
                
        return empty_matrix

def calculate_height(size):
    root = sqrt(size)
    height = int(size/root)
    return height

def generate_matrix_height(height):
    output: List[List[any]] = []
    for i in range(height):
        output.append([])
    return output

def insert_people_into_matrix(width, matrix, seed):
    start = 0
    row_indexer = width
    for row_index, row in enumerate(matrix, start=0):
        for i in range(start, row_indexer):
            row.append(create_person(seed[i]))   
        start+=width
        row_indexer += width
    return matrix

def poke_cells_around(world):
    size = len(world)
    for y, row in enumerate(world, start=0):
        for x, column in enumerate(row, start=0):
            current = world[y][x]
            if not current.color == Actor.NONE: #checks so thats the index actually has an actor
                check_indexes= set_poke_indexes(x, y)

                for index in check_indexes: #checks if indexes are valid and pokes the valid ones
                    if is_valid_location(size, index[1], index[0]): #checks if location is valid
                        world[index[1]][index[0]].poke(current.color)
                  

def update_cells(self):
    for row in self.world:
        for item in row:
            #cxatches zero div error
            if not item.friend_count+item.foe_count == 0:
                # TODO escape to different function
                # checks for item threshold and updates state of items
                if item.friend_count / (item.friend_count+item.foe_count) >= self.THRESHOLD:
                    item.state = State.SATISFIED
                elif not item.color == Actor.NONE:
                    item.state = State.UNSATISFIED
            item.friend_count = 0
            item.foe_count = 0

def move_cells(world):
    for i, row in enumerate(world, start = 0):
        for j, item in enumerate(row, start = 0):
            if item.state == State.UNSATISFIED:
                    color = item.color
                    random_empty_place = find_random_empty_place(find_empty_indexes(world))
                    #creates new object at emplty index
                    world = create_new_object_at_empty_index(random_empty_place, world, color)
                    #add an empty object at the old index
                    world[i][j] = clear()
                    #updates the list of empty indexes
                    empty_indexes = find_empty_indexes(world)
    return world
                    
def find_random_empty_place(empty_indexes):
    random_empty_place = empty_indexes[randint(0, len(empty_indexes)-1)]
    return random_empty_place

def create_new_object_at_empty_index(empty_place, world, color):
     world[empty_place[0]][empty_place[1]] = Person(State.SATISFIED, color)
     return world

def clear():
    return Person(State.NA, Actor.NONE)

def find_empty_indexes(world):
    output = []
    for i, row in enumerate(world, start = 0):
        for j, item in enumerate(row, start = 0):
            if item.color == Actor.NONE:
                output.append([i,j])
    return output

def set_poke_indexes(current_x: int, current_y: int):
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

def create_person(color: Actor):
    if color == "red":
        person = Person(State.SATISFIED, Actor.RED)
    elif color == "blue":
        person = Person(State.SATISFIED, Actor.BLUE)
    else:
        person = Person(State.NA, Actor.NONE)
    return person

    # Check if inside world
def is_valid_location(size: int, row: int, col: int):
    return 0 <= row < size and 0 <= col < size


# ------- Testing -------------------------------------

# Here you run your tests i.e. call your logic methods
# to see that they really work
def test():
    # A small hard coded world for testing
    test_world = [
        [Actor.RED, Actor.RED, Actor.NONE],
        [Actor.NONE, Actor.BLUE, Actor.NONE],
        [Actor.RED, Actor.NONE, Actor.BLUE]
    ]

    th = 0.5  # Simpler threshold used for testing

    size = len(test_world)
    print(is_valid_location(size, 0, 0))
    print(not is_valid_location(size, -1, 0))
    print(not is_valid_location(size, 0, 3))
    print(is_valid_location(size, 2, 2))

    # TODO More tests

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
    WIDTH = 400   # Size for window
    HEIGHT = 400
    MARGIN = 50

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
