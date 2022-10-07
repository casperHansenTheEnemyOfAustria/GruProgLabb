# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from HasPosition import HasPosition

"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(HasPosition):
    WIDTH = 40
    HEIGHT = 40
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
        
    
