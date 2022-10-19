from .Positionable import Positionable
from abc import ABC


class Movable(Positionable, ABC):
    """Base class for objects that can be moved in the GUI"""
    def __init__(self, x, y,  dx, dy):
        super().__init__(x, y)
        self.__dx = dx
        self.__dy = dy

    def move(self):
        """Moves object"""
        self.x += self.__dx
        self.y += self.__dy
    
    
    def get_dx(self):
        """The delta in x"""
        return self.__dx

    def get_dy(self):
        """tThe delta in y"""
        return self.__dy

    def set_dx(self, dx):
        """Sets delta in x"""
        self.__dx = dx

    def set_dy(self, dy):
        """Sets delta in y"""
        self.__dy = dy
