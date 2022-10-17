# package pong.model

from abc import abstractmethod, ABC


class HasPosition(ABC):
    """
        Contract for anything that can be positioned in the world.

        NOTE: This must be fulfilled by any object the GUI shall render
        
    """
    def __init__(self, x, y):
        self.__x = x      # 0, 0 is upper left corner
        self.__y = y
        self.__dx = 0
        self.__dy = 0


    def set_dx(self, dx):
        self.__dx = dx


    def set_dy(self, dy):
        self.__dy = dy

    def set_x(self, x):
        self.__x = x

    
    def set_y(self, y):
        self.__y = y


    def stop(self):
        self.__dx = self.__dy = 0

    def move(self):
        self.__x += self.__dx
        self.__y += self.__dy
    
    def get_x(self):      
        return self.__x# Min x and y is upper left corner (y-axis pointing down)


    def get_y(self):
        return self.__y

    
    def get_dy(self):
        return self.__dy
    
    def get_dx(self):
        return self.__dx

    @classmethod
    def get_width(cls):
        return cls.WIDTH        


    @classmethod
    def get_height(cls):
        return cls.HEIGHT
