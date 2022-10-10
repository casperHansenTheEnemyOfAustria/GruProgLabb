# package pong.model

from pong.model.Config import GAME_WIDTH
import pong.event.ModelEvent
import pong.event.EventBus
from .Paddle import Paddle
from .Paddle import PADDLE_WIDTH
from .Ball import Ball


class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """

    
    # TODO More attributes
    points_left  = 0
    points_right = 0

    # TODO Initialization
    def __init__(self):
        self.paddle1  = Paddle(0)
        self.paddle2 = Paddle(GAME_WIDTH - PADDLE_WIDTH)
        self.ball = Ball(0)

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    @classmethod
    def update(cls, now):
        pass
        # TODO Game logic here

    # --- Used by GUI  ------------------------
    def get_all_items_with_position(cls):
        drawables = [cls.paddle1, cls.paddle2, cls.ball]
        return drawables

    @classmethod
    def get_points_left(cls):
        return cls.points_left

    @classmethod
    def get_points_right(cls):
        return cls.points_right

    @classmethod
    def set_speed_right_paddle(cls, dy):
        # TODO
        pass

    @classmethod
    def set_speed_left_paddle(cls, dy):
        # TODO
        pass
