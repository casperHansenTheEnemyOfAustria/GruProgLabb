# package pong.model
from pong.model.Config import *
from pong.model.Movable import Movable

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5


# A Paddle for the Pong game
class Paddle(Movable):
    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height, dx, dy)

    def move_paddle(self):
        self.y += self.dy
