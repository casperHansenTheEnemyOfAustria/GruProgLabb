# package pong.model

from pong.event.ModelEvent import * 
from pong.event.EventBus import *
from .Paddle import Paddle
from .Paddle import PADDLE_WIDTH
from .Paddle import PADDLE_HEIGHT
from .Ball import Ball
from .Config import *


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
    
    def __init__(self) -> None:
        pass

    paddle1  = Paddle(0)
    paddle2 = Paddle(GAME_WIDTH - PADDLE_WIDTH)
    ball = Ball(0)

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    
    def update(self):
        self.paddle1.move()
        self.paddle2.move()
        self.ball.move()
        self.collision_detector()
        
        
        
        pass
        # TODO Game logic here

    # --- Used by GUI  ------------------------
    
    
    def get_all_items_with_position(cls):
        drawables = {"paddle1":cls.paddle1, "paddle2":cls.paddle2, "ball":cls.ball}
        return drawables
    

    def collision_detector(self):
        ball = self.ball
        paddle1 = self.paddle1
        paddle2 = self.paddle2
        if ball.get_y() + ball.get_height() >= GAME_HEIGHT or ball.get_y() <= 0:
            EventBus.publish(ModelEvent(ModelEvent.EventType(1),"Ball hit ceiling" ))
        
        
        elif (ball.get_x() <= 0+PADDLE_WIDTH and ball_in_range(ball, paddle1)) or (ball.get_x() + ball.get_width() >= GAME_WIDTH - PADDLE_WIDTH and ball_in_range(ball, paddle2)):
            EventBus.publish(ModelEvent(ModelEvent.EventType(0), "ball hit paddle"))
        
        elif ball.get_x()+ball.get_width() < 0 or ball.get_x() > GAME_WIDTH: 
            EventBus.publish(ModelEvent(ModelEvent.EventType(2), "ball out"))
            
            
    
    @classmethod
    def get_points_left(cls):
        return cls.points_left

    @classmethod
    def get_points_right(cls):
        return cls.points_right

    @classmethod
    def set_speed_right_paddle(cls, dy):
        cls.paddle2.set_dy(dy)
        
        
        # TODO
        pass

    @classmethod
    def set_speed_left_paddle(cls, dy):
        cls.paddle1.set_dy(dy)
        # TODO
        pass

    @classmethod
    def set_speed_ball(cls, dx, dy):
        cls.ball.set_dy(dy)
        cls.ball.set_dx(dx)
        
    @classmethod
    def set_pos_ball(cls, x, y ):
        cls.ball.set_x(x)
        cls.ball.set_y(y)
        
    
        
    @classmethod
    def ball_collide_with_paddle(cls):
        cls.set_speed_ball(-cls.ball.get_dx(), cls.ball.get_dy())
        
    @classmethod
    def ball_wall_collision(cls):
        cls.ball.set_dy(-cls.ball.get_dy())
        
        
        
# _____HELPERS___
def ball_in_range(ball: Ball, paddle: Paddle)  -> bool:
        #mult by 1000 to get accuarcy
        if int((ball.get_y()+ball.get_height()/2)*1000) in range( int((paddle.get_y()-ball.get_height()/2)*1000), int(paddle.get_y()+PADDLE_HEIGHT + ball.get_height()/2)*1000):
            return True
        return False
        
                