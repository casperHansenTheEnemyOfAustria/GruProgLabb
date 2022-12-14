# package pong.view.theme

from pong.model.Ball import Ball
from pong.view.Assets import Assets

"""
   Specific theme

   *** Nothing to do here ***
"""


class Duckie(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("duckieBg.jpg")
    
    @classmethod
    def get_ball(cls, obj):
        Assets.bind(obj, "duckieBall.png")
    

    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------
    ball_hit_paddle_sound = Assets.get_sound("ballhitpaddle.wav")