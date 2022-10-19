# package pong.model

from .Movable import Movable
from pong.model.Config import GAME_HEIGHT


PADDLE_WIDTH: int = 10
PADDLE_HEIGHT: int = 60
PADDLE_SPEED: int = 8

class Paddle(Movable):
    """Paddle for the Pong game"""
    WIDTH: int = PADDLE_WIDTH
    HEIGHT: int = PADDLE_HEIGHT
    def __init__(self, x: int, dx: int = 0, dy: int = 0):
        y: float = (GAME_HEIGHT - PADDLE_HEIGHT)/2
        super().__init__(x, y, dx, dy)
        self.y = y