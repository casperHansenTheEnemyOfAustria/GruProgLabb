# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from .Movable import Movable
"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(Movable):

    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height, dx, dy)

    def move_ball(self):
        self.x += self.dx
        self.y += self.dy
