# package pong.view.theme

from pong.model.Ball import Ball
from pong.view.Assets import Assets

"""
   Specific theme

   *** Nothing to do here ***
"""


class Cool(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("coolBg.png")
    
    def get_ball(cls, obj):
        Assets.bind(obj, "coolBall.png")

    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------
    ball_hit_paddle_sound = Assets.get_sound("cool_sound.wav")