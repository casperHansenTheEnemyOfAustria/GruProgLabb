# package pong.model

from mimetypes import init
from pong.model.Config import GAME_HEIGHT

from .HasPosition import HasPosition

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5


# A Paddle for the Pong game
class Paddle(HasPosition):
    WIDTH = PADDLE_WIDTH
    HEIGHT = PADDLE_HEIGHT
    def __init__(self, x, dx = 0, dy = 0):
        y = (GAME_HEIGHT  - PADDLE_HEIGHT)/2
        super().__init__(x, y)
        self.__y = y
    

    def get_start_pos(self):
        return self.__y
    
    def get_end_pos(self):
        return self.__y + PADDLE_HEIGHT

    # def is_at_max(self):
        
        

            
    #     elif self.__y > GAME_HEIGHT-PADDLE_HEIGHT:
    #         print(self.__y)
    #         self.__y = GAME_HEIGHT-PADDLE_HEIGHT
    #         return True
    #     return False