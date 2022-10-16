from .Positionable import Positionable
from abc import ABC


class Movable(Positionable, ABC):
    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height)
        self.dx = dx
        self.dy = dy

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def stop(self):
        self.dx = self.dy = 0

    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy
