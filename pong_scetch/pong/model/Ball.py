# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from .Movable import Movable

"""
 * A Ball for the Pong game
 * A model class
"""

class Ball(Movable):
    WIDTH: int = 40
    HEIGHT: int = 40
    def __init__(self, x: int, dx: float = 0.0, dy: float = 0.0, ):
        y: float = (GAME_HEIGHT - self.HEIGHT)/2
        x: float = (GAME_WIDTH - self.WIDTH)/2
        super().__init__(x, y, dx, dy)

   
    
