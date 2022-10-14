# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from .HasPosition import HasPosition
from .Config import *
from random import uniform, randint
from numpy import arange

"""
 * A Ball for the Pong game
 * A model class
"""




class Ball(HasPosition):
    WIDTH = 40
    HEIGHT = 40
    def __init__(self, x, dx=0, dy=0, ):
        y= (GAME_HEIGHT - self.HEIGHT)/2
        x = (GAME_WIDTH - self.WIDTH)/2
        super().__init__(x, y)
  
    @classmethod
    def random_ball_speed(cls):
        output = uniform(-1,1)
        while output in arange(-0.6, 0.6, 0.01):
           output = uniform(-1,1) 
        return output*BALL_SPEED_FACTOR
        # return uniform(-1,1)*BALL_SPEED_FACTOR
    
   
    
