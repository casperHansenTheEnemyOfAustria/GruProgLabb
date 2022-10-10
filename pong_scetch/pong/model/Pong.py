# package pong.model

import pong.event.ModelEvent
import pong.event.EventBus


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

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    @classmethod
    def update(cls, now):
        pass
        # TODO Game logic here

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

    @classmethod
    def set_speed_right_paddle(cls, dy):
        # TODO
        pass

    @classmethod
    def set_speed_left_paddle(cls, dy):
        # TODO
        pass
