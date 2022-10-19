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
from random import uniform
from random import choice

from .ai import AI

class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """

    
       
    paddle1 = Paddle(0+10)
    paddle2 = Paddle(GAME_WIDTH - PADDLE_WIDTH-10)
    ball = Ball(0)  

    
    def __init__(self):
        print("Initialization")
        self.__points_left  = 0
        self.__points_right = 0
        self.__winner = None




    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    
    def update(self):
        self.move_paddle(self.paddle1)
        self.move_paddle(self.paddle2)
        
        self.ball.move()
        # AI(self.paddle1, self.ball).run()
        # AI(self.paddle2, self.ball).run()
        
        points_to = self.collision_detector()
        
        self.add_points_to_player(points_to)
        self.__check_winner()
        
    
    def __check_winner(self):
        if self.__points_left == 2:
            self.__winner = " left"
        elif self.__points_right == 2:
            self.__winner = " right"
    
    def add_points_to_player(self, side:str):
        if side =="left":
            self.__points_left += 1
            print("player left +1")
        elif side == "right":
            self.__points_right += 1
            print("player right +1")
        else:
            pass
            
          
          
          
        
    def collision_detector(self) -> str:
        ball = self.ball
        paddle1 = self.paddle1
        paddle2 = self.paddle2
        
        if Collision.get_collision_type(paddle1, paddle2, ball) == 0:
            self.__ball_collide_with_paddle()
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 1:
            self.__ball_wall_collision()  
                
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 3:
            self.new_ball(True)
            return "left"
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 2:
            self.new_ball(True)
            return "right"  


    # --- Used by GUI  ------------------------
    
    @classmethod
    def get_all_items_with_position(cls) -> dict:
        drawables = {"paddle1":cls.paddle1, "paddle2":cls.paddle2, "ball":cls.ball}
        return drawables
    
    
    def get_winner(self):
        return self.__winner
    

        
        
    @classmethod
    def new_ball(cls, in_match: bool) -> None:
        if in_match:
            cls.set_pos_ball(GAME_WIDTH/2, randint(0, GAME_HEIGHT-Ball.get_height()))
        cls.set_speed_ball(cls.get_random_number(), cls.get_random_number())
        
        
    @staticmethod
    def get_random_number() -> float:
    
        return (3-uniform(-1,1))*choice([-1, 1])

            
            
    
    
    def get_points_left(self) -> int:
        return self.__points_left


    def get_points_right(self) -> int:
        return self.__points_right

    @classmethod
    def set_speed_right_paddle(cls, dy:float) -> None:
        cls.paddle2.set_dy(dy)
    

    @classmethod
    def set_speed_left_paddle(cls, dy:float):
        cls.paddle1.set_dy(dy)

    @classmethod
    def set_speed_ball(cls, dx:float, dy:float) -> None:
        cls.ball.set_dy(dy)
        cls.ball.set_dx(dx)
        
    @classmethod
    def set_pos_ball(cls, x:float, y:float) -> None:
        cls.ball.set_x(x)
        cls.ball.set_y(y)
        
    
        
    @classmethod
    def __ball_collide_with_paddle(cls) -> None:
        speed_mod = 0.2
        
        
        cls.set_speed_ball(-(cls.ball.get_dx()+ speed_mod*cls.ball.get_dx()), cls.ball.get_dy()+speed_mod*cls.ball.get_dy())
        
    @classmethod
    def __ball_wall_collision(cls) -> None:
        cls.ball.set_dy(-cls.ball.get_dy())
        
        
        
# _____HELPERS___

    @staticmethod  
    def move_paddle(paddle: Paddle) -> None:
        if paddle.get_y()+paddle.get_dy() < 0:
            paddle.set_y(0)
        elif paddle.get_y()+paddle.get_dy() > GAME_HEIGHT - PADDLE_HEIGHT:
            paddle.set_y(GAME_HEIGHT  - PADDLE_HEIGHT)
        else:
            paddle.move()
            

            
                