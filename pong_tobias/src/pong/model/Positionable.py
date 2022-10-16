from abc import ABC
from .HasPosition import HasPosition


class Positionable(HasPosition, ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_max_x(self):
        return self.x + self.width

    def get_max_y(self):
        return self.y + self.height

    def get_center_x(self):
        return self.x + self.width / 2

    def get_center_y(self):
        return self.y + self.height / 2

    def get_image(self):
        return self.image
