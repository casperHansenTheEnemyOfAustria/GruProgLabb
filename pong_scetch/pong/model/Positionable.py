from abc import ABC
from .HasPosition import HasPosition


class Positionable(HasPosition, ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self. y = y
        
    def set_x(self, x):
        self. x = x

    @classmethod
    def get_width(cls):
        return cls.WIDTH        


    @classmethod
    def get_height(cls):
        return cls.HEIGHT
    
    def get_max_x(self):
        return self.x + self.__width

    def get_max_y(self):
        return self.y + self.__height

    def get_center_x(self):
        return self.x + self.__width / 2

    def get_center_y(self):
        return self.y + self.__height / 2
