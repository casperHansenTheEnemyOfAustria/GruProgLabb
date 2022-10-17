
from pong.event.ModelEvent import * 
from pong.event.EventBus import *
from .Paddle import PADDLE_WIDTH
from .Paddle import PADDLE_HEIGHT
from .Config import *

class Collision:
    __collision_type = None
    @classmethod
    def __publish_collision(cls):
        if not cls.__collision_type == None:
            EventBus.publish(ModelEvent(ModelEvent.EventType(cls.__collision_type)))
         
    @classmethod
    def get_collision_type(cls, paddle1, paddle2, ball):
        
        last_paddle_to_hit = ""
        if ball.get_y() + ball.get_height() >= GAME_HEIGHT or ball.get_y() <= 0: #wall collision
            
            cls.__collision_type = 1
            return cls.__collision_type
            
        
        elif (ball.get_x() <= 0+PADDLE_WIDTH and ball_in_range(ball, paddle1)) and not last_paddle_to_hit == "left" : #left paddle hit
            
            cls.__collision_type = 0
            
            last_paddle_to_hit = "left"
            return cls.__collision_type
        
        elif (ball.get_x() + ball.get_width() >= GAME_WIDTH - PADDLE_WIDTH and ball_in_range(ball, paddle2)) and not last_paddle_to_hit == "right": #right paddle hit
            
            cls.__collision_type = 0
            
            last_paddle_to_hit = "right"
            return cls.__collision_type
        
        elif ball.get_x()+ball.get_width() < 0 : # ball out right

            cls.__collision_type = 2
            
            last_paddle_to_hit = ""
            return cls.__collision_type
        
            
        elif ball.get_x() > GAME_WIDTH: #ball out left
            
            cls.__collision_type = 3
            
            last_paddle_to_hit = ""
            return cls.__collision_type
        
        cls.__publish_collision()

            
           
        
            
#------HELPER------
            
def ball_in_range(ball, paddle)  -> bool:
        #mult by 1000 to get accuarcy
        if int((ball.get_y()+ball.get_height()/2)*1000) in range( int((paddle.get_y()-ball.get_height()/2)*1000), int(paddle.get_y()+PADDLE_HEIGHT + ball.get_height()/2)*1000):
            return True
        return False
        