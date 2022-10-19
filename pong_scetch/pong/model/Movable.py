from .Positionable import Positionable
from abc import ABC


class Movable(Positionable, ABC):
    """Base class for objects that can be moved in the GUI"""
    def __init__(self, x: int, y: int,  dx: int, dy: int):
        super().__init__(x, y)
        self.__dx = dx
        self.__dy = dy

    def move(self) -> None:
        """Moves object. ()  -> None"""
        self.x += self.__dx
        self.y += self.__dy
    
    
    def get_dx(self) -> float:
        """The delta x. ()  -> float"""
        return self.__dx


    def get_dy(self) -> float:
        """tThe delta y. () -> float"""
        return self.__dy


    def set_dx(self, dx: float) -> None:
        """Sets delta x. (delta x: float) -> None"""
        self.__dx = dx


    def set_dy(self, dy: float) -> None:
        """Sets delta y. (delta y:  float) -> None"""
        self.__dy = dy
