# package pong.model

from mimetypes import init
from pong.model.Config import GAME_HEIGHT

from .HasPosition import HasPosition

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5


# A Paddle for the Pong game
class Paddle(HasPosition):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
    pass
