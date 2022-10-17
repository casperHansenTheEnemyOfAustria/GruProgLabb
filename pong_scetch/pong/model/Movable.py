from .Positionable import Positionable
from abc import ABC


class Movable(Positionable, ABC):
    def __init__(self, x, y,  dx, dy):
        super().__init__(x, y)
        self.__dx = dx
        self.__dy = dy

    def move(self):
        self.x += self.__dx
        self.y += self.__dy
    
    
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy
