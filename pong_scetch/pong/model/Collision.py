
from pong.event.ModelEvent import * 
from pong.event.EventBus import *
from .Paddle import PADDLE_WIDTH
from .Paddle import PADDLE_HEIGHT
from .Config import *

from numpy import arange


class Collision:
    __collision_type = None
    __last_paddle_to_hit = None
    @classmethod
    def __publish_collision(cls):
        if not cls.__collision_type == None:
            EventBus.publish(ModelEvent(ModelEvent.EventType(cls.__collision_type)))
        cls.__collision_type = None
         
    @classmethod
    def get_collision_type(cls, paddle1, paddle2, ball):
        

        
        if cls.is_in_range(ball, paddle1) and not cls.__last_paddle_to_hit == "left":
            cls.__collision_type = 0
            
            cls.__last_paddle_to_hit = "left"
            return cls.__collision_type
        
        elif cls.is_in_range(ball, paddle2) and not cls.__last_paddle_to_hit == "right":
            cls.__collision_type = 0
            
            cls.__last_paddle_to_hit = "right"
            return cls.__collision_type
        
        elif ball.get_y() + ball.get_height() > GAME_HEIGHT or ball.get_y() < 0: #wall collision
            
            cls.__collision_type = 1
            return cls.__collision_type
            
        
        elif ball.get_x()+ball.get_width() < 0 : # ball out right

            cls.__collision_type = 2
            
            cls.__last_paddle_to_hit = None
            return cls.__collision_type
        
            
        elif ball.get_x() > GAME_WIDTH: #ball out left
            
            cls.__collision_type = 3
            
            cls.__last_paddle_to_hit = None
            return cls.__collision_type
          
        cls.__publish_collision()

        

            
           
        
            
    #------HELPER------
    @staticmethod
    def is_in_range(ball, paddle):
        above = ball.get_max_y() < paddle.get_y()
        below = ball.get_y() > paddle.get_max_y()
        left_of = ball.get_max_x() < paddle.get_x()
        right_of = ball.get_x() > paddle.get_max_x()
        
        return not (above or below or left_of or right_of)
    
    