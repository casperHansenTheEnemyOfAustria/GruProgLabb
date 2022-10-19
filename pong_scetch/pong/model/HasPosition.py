# package pong.model

from abc import abstractmethod, ABC


class HasPosition(ABC):
    """
        Contract for anything that can be positioned in the world.
        NOTE: This must be fulfilled by any object the GUI shall render
        Methods to implement: get_x(), get_y(), get_width(), get_height().
    """
    @abstractmethod
    def get_x(self):
        raise NotImplementedError

    @abstractmethod
    def get_y(self):
        raise NotImplementedError

    @abstractmethod
    def get_width(self):
        raise NotImplementedError

    @abstractmethod
    def get_height(self):
        raise NotImplementedError
