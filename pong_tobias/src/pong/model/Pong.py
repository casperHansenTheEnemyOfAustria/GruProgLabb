# package pong.model

import pong.event.ModelEvent
import pong.event.EventBus
from pong.model.Config import *
from pong.model.Paddle import Paddle
from src.pong.view.Assets import *
from .Ball import Ball

from img import *
class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """
    # TODO More attributes
    points_left = 0
    points_right = 0

    # TODO Initialization
    def __init__(self, ball, left_paddle, right_paddle):
        self.__ball = ball
        self.__left_paddle = left_paddle
        self.__right_paddle = right_paddle

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    def update(self, now):
        # TODO Game logic here
        self.__left_paddle.move_paddle()
        self.__right_paddle.move_paddle()
    # --- Used by GUI  ------------------------
    @classmethod
    def get_all_items_with_position(cls):
        drawables = []
        # TODO
        return drawables

    @classmethod
    def get_points_left(cls):
        return cls.points_left

    @classmethod
    def get_points_right(cls):
        return cls.points_right

    def set_speed_right_paddle(self, dy):
        # TODO
        self.__right_paddle.set_dy(dy)

    def set_speed_left_paddle(self, dy):
        # TODO
        self.__left_paddle.set_dy(dy)

    def get_left_paddle(self):
        return self.__left_paddle

    def get_right_paddle(self):
        return self.__right_paddle

    def get_ball(self):
        return self.__ball
