# package pong.model

from pong.event.ModelEvent import * 
from pong.event.EventBus import *
from .Paddle import Paddle
from .Paddle import PADDLE_WIDTH
from .Paddle import PADDLE_HEIGHT
from .Ball import Ball
from .Collision import Collision

from .Config import *
from random import randint
from numpy import arange

from .ai import AI

class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """

    
    # TODO More attributes
   
    paddle1  = Paddle(0)
    paddle2 = Paddle(GAME_WIDTH - PADDLE_WIDTH)
    ball = Ball(0)  
    # TODO Initialization
    
    def __init__(self) -> None:
        print("Initialization")
        self.__points_left  = 0
        self.__points_right = 0
        pass



    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    
    def update(self):
        paddle_boundaries(self.paddle1)
        paddle_boundaries(self.paddle2)
        
        self.ball.move()
        # AI(self.paddle1, self.ball).run()
        # AI(self.paddle2, self.ball).run()
        
        points_to = self.collision_detector()
        
        self.add_points_to_player(points_to)
        # TODO Game logic here
        
    
    def add_points_to_player(self, side):
        if side =="left":
            self.__points_left += 1
            print("player left +1")
        elif side == "right":
            self.__points_right += 1
            print("player right +1")
        else:
            pass
            
            


    # --- Used by GUI  ------------------------
    
    @classmethod
    def get_all_items_with_position(cls):
        drawables = {"paddle1":cls.paddle1, "paddle2":cls.paddle2, "ball":cls.ball}
        return drawables
    
    
    def collision_detector(self):
        ball = self.ball
        paddle1 = self.paddle1
        paddle2 = self.paddle2
        
        if Collision.get_collision_type(paddle1, paddle2, ball) == 0:
            self.__ball_collide_with_paddle()
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 1:
            self.__ball_wall_collision()  
                
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 3:
            self.__new_ball()
            return "left"
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 2:
            self.__new_ball()
            return "right"
        
        
    @classmethod
    def __new_ball(cls):
        cls.set_speed_ball(Ball.random_ball_speed(), Ball.random_ball_speed())
        cls.set_pos_ball(GAME_WIDTH/2, randint(0, GAME_HEIGHT-Ball.get_height()))

            
            
    
    
    def get_points_left(self):
        return self.__points_left


    def get_points_right(self):
        return self.__points_right

    @classmethod
    def set_speed_right_paddle(cls, dy):
        cls.paddle2.set_dy(dy)
        
        
        # TODO
        pass

    @classmethod
    def set_speed_left_paddle(cls, dy):
        cls.paddle1.set_dy(dy)
        
        
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
    def __ball_collide_with_paddle(cls):
        cls.set_speed_ball(-cls.ball.get_dx()*1.4, cls.ball.get_dy()*1.4)
        
    @classmethod
    def __ball_wall_collision(cls):
        cls.ball.set_dy(-cls.ball.get_dy())
        
        
        
# _____HELPERS___

        
def paddle_boundaries(paddle: Paddle):
    if paddle.get_y()+paddle.get_dy() < 0:
        paddle.set_y(0)
    elif paddle.get_y()+paddle.get_dy() > GAME_HEIGHT - PADDLE_HEIGHT:
        paddle.set_y(GAME_HEIGHT  - PADDLE_HEIGHT)
    else:
        paddle.move()
        

            
                