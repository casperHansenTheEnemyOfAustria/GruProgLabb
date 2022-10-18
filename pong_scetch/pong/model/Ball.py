# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from .HasPosition import HasPosition
from .Config import *
from random import uniform, randint
from numpy import arange
from .Movable import Movable

"""
 * A Ball for the Pong game
 * A model class
"""




class Ball(Movable):
    WIDTH = 40
    HEIGHT = 40
    def __init__(self, x, dx=0, dy=0, ):
        y= (GAME_HEIGHT - self.HEIGHT)/2
        x = (GAME_WIDTH - self.WIDTH)/2
        super().__init__(x, y, dx, dy)
  
    @classmethod
    def random_ball_speed(cls):
        output = uniform(-1,1)
        while abs(output) < 0.6:
           output = uniform(-1,1) 
        return output*BALL_SPEED_FACTOR
        # return uniform(-1,1)*BALL_SPEED_FACTOR
    
   
    
