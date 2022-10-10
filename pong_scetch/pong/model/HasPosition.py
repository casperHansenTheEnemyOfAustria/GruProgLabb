# package pong.model

from abc import abstractmethod, ABC


class HasPosition(ABC):
    """
        Contract for anything that can be positioned in the world.

        NOTE: This must be fulfilled by any object the GUI shall render
        
    """
    def __init__(self, x, y, dx, dy):
        self.__x = x      # 0, 0 is upper left corner
        self.__y = y
        self.__dx = dx
        self.__dy = dy

    @abstractmethod
    def set_dx(self, dx):
        self.__dx = dx

    @abstractmethod
    def set_dy(self, dy):
        self.__dy = dy

    @abstractmethod
    def set_x(self, x):
        self.__x = x
        
    @abstractmethod
    def set_y(self, y):
        self.__y = y
        
    @abstractmethod    
    def stop(self):
        self.__dx = self.__dy = 0

    @abstractmethod       
    def move(self):
        self.__x += self.__dx
        self.__y += self.__dy
    
    @abstractmethod
    def get_x(self):      
        return self.__x# Min x and y is upper left corner (y-axis pointing down)
        raise NotImplementedError

    @abstractmethod
    def get_y(self):
        return self.__y
        raise NotImplementedError

    @abstractmethod
    def get_width(self):
        return self.WIDTH        
        raise NotImplementedError

    @abstractmethod
    def get_height(self):
        return self.HEIGHT
        raise NotImplementedError
