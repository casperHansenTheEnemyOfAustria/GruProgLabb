# package pong.model

from mimetypes import init
from .Movable import Movable
from pong.model.Config import GAME_HEIGHT

from .HasPosition import HasPosition

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 8


# A Paddle for the Pong game
class Paddle(Movable):
    """Paddle for the Pong game"""
    WIDTH = PADDLE_WIDTH
    HEIGHT = PADDLE_HEIGHT
    def __init__(self, x, dx = 0, dy = 0):
        y = (GAME_HEIGHT  - PADDLE_HEIGHT)/2
        super().__init__(x, y, dx, dy)
        self.y = y
    

    def get_start_pos(self):
        """Gets start coord for the paddle"""
        return self.y
    
    def get_end_pos(self):
        """Gets end coord for the paddle"""
        return self.y + PADDLE_HEIGHT
