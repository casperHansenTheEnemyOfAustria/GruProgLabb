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


class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """
    
    # Class attributes for the moveable objects
    paddle1 = Paddle(10)
    paddle2 = Paddle(GAME_WIDTH - PADDLE_WIDTH-10)
    ball = Ball(0)

    
    def __init__(self):
        self.__points_left  = 0
        self.__points_right = 0
        self.__points_to_win = 2
        self.__winner = None

    # --------  Game Logic -------------

    
    def update(self) -> None:
        """Update movable objects, points and check for winner. () -> None"""
        self.move_paddle(self.paddle1)
        self.move_paddle(self.paddle2)
        self.ball.move()
        # Cheaty AI
        # AI(self.paddle1, self.ball).run()
        # AI(self.paddle2, self.ball).run()
        
        points_to = self.collision_detector()
        self.add_points_to_player(points_to)
        self.__check_winner()

    def __check_winner(self) -> None:
        """Check for a winner. () -> None"""
        if self.__points_left == self.__points_to_win:
            self.__winner = " left"

        elif self.__points_right == self.__points_to_win:
            self.__winner = " right"
    

    def add_points_to_player(self, side:str) -> None:
        """Add points to correct player. (side: str) -> None"""
        if side =="left":
            self.__points_left += 1

        elif side == "right":
            self.__points_right += 1

        else:
            pass
          
    
    def collision_detector(self) -> str:
        """Check collision tyype and return which side should get points. () -> str"""
        ball = self.ball
        paddle1 = self.paddle1
        paddle2 = self.paddle2
        
        if Collision.get_collision_type(paddle1, paddle2, ball) == 0: #If the ball collides with paddle
            self.__ball_collide_with_paddle()
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 1: #If the ball collides with wall
            self.__ball_ceil_floor_collision()  
                
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 3: #If the ball goes outside on the right side
            self.new_ball(True) #spawn a new ball in the middle
            return "left" #Points to the left player
            
        elif Collision.get_collision_type(paddle1, paddle2, ball) == 2: #If the ball goes outside on the left side
            self.new_ball(True) #spawn a new ball in the middle
            return "right" #Points to the right player


    # --- Used by GUI  ------------------------
    
    @classmethod
    def get_all_items_with_position(cls) -> dict:
        """Returns a dictionary with all positionable objects. () -> dict"""
        drawables = {"paddle1": cls.paddle1, "paddle2": cls.paddle2, "ball": cls.ball}
        return drawables
    
    
    def get_winner(self) -> str:
        """Return string with the game winner. () -> str"""
        return self.__winner
    

    @classmethod
    def new_ball(cls, in_match: bool) -> None:
        """Place ball in the middle of the screen but on random height. Set speed of ball to a randon dx and dy. (in_match: bool) -> None"""
        if in_match:
            cls.set_pos_ball(GAME_WIDTH/2, randint(0, GAME_HEIGHT-Ball.get_height()))
        cls.set_speed_ball(cls.get_random_number(), cls.get_random_number()) #Shoot the ball in a random direction with a random speed
        
        
    @staticmethod
    def get_random_number() -> float:
        """Return a random float between -4 and 4. () -> float"""
        return (3-uniform(-1,1))*choice([-1, 1])

            
    def get_points_left(self) -> int:
        """Return points for left player. () ->  int"""
        return self.__points_left


    def get_points_right(self) -> int:
        """Return points for right player. () -> int"""
        return self.__points_right


    @classmethod
    def set_speed_right_paddle(cls, dy:float) -> None:
        """Set speed of right paddle. (delta y) -> None"""
        cls.paddle2.set_dy(dy)
    

    @classmethod
    def set_speed_left_paddle(cls, dy:float) -> None:
        """Set speed of left paddle. (delta y)  -> None"""
        cls.paddle1.set_dy(dy)


    @classmethod
    def set_speed_ball(cls, dx:float, dy:float) -> None:
        """Set speed of ball. (delta x, delta y) -> None"""
        cls.ball.set_dx(dx)
        cls.ball.set_dy(dy)
        

    @classmethod
    def set_pos_ball(cls, x:float, y:float) -> None:
        """set position of ball. (x, y) -> None"""
        cls.ball.set_x(x)
        cls.ball.set_y(y)
    
        
    @classmethod
    def __ball_collide_with_paddle(cls) -> None:
        """When ball hits paddle increase the speed slightly. () -> None"""
        speed_mod = 1.05
        cls.set_speed_ball(-(cls.ball.get_dx()*speed_mod), cls.ball.get_dy()*speed_mod)


    @classmethod
    def __ball_ceil_floor_collision(cls) -> None:
        """Ball hit the ceiling or floor. ()  -> None"""
        cls.ball.set_dy(-cls.ball.get_dy())
        
        
        
# _____HELPERS___
    @staticmethod  
    def move_paddle(paddle: Paddle) -> None:
        """Make sure the paddles can't move of the screen. (paddle: Paddle) -> None"""
        if paddle.get_y()+paddle.get_dy() < 0: #The paddle should not go above the top wall
            paddle.set_y(0)
        elif paddle.get_max_y() + paddle.get_dy() > GAME_HEIGHT: #The paddle should not go below the bottom wall
            paddle.set_y(GAME_HEIGHT - PADDLE_HEIGHT)
        else:
            paddle.move() #If the ball is inbetween the walls, let it move
            

            
                