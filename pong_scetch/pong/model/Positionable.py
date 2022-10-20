from abc import ABC
from .HasPosition import HasPosition


class Positionable(HasPosition, ABC):
    """Base class for anything that can be positioned in the GUI"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def get_x(self) -> int:
        """Return value of x. () -> int"""
        return self.x


    def get_y(self) -> int:
        """Return value of y. () -> int"""
        return self.y

    
    def set_y(self, y) -> None:
        """Set value of y. (y: int) -> None"""
        self.y = y
        

    def set_x(self, x) -> None:
        """Set value of x. (x: int) -> None"""
        self.x = x


    @classmethod
    def get_width(cls) -> int:
        """Not used - Returns width. () -> int"""
        return cls.WIDTH        


    @classmethod
    def get_height(cls) -> int:
        """Not used - Returns height. () -> int"""
        return cls.HEIGHT

    
    def get_max_x(self) -> int:
        """Returns max_x value. () -> int"""
        return self.x + self.get_width()


    def get_max_y(self) -> int:
        """Returns max_y value. () -> int"""
        return self.y + self.get_height()


    def get_center_x(self) -> float:
        """Returns center x value. () -> float"""
        return self.x + self.get_width()/ 2


    def get_center_y(self) -> float:
        """Returns center y value. () -> float"""
        return self.y + self.get_height() / 2