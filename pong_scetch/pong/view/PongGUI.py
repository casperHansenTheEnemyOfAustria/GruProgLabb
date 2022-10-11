# package pong.view
from turtle import right
import pygame

from pong.model.Pong import Pong
from pong.model.Ball import Ball
from pong.model.Paddle import Paddle

from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler

from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie

from pong.model.Paddle import PADDLE_SPEED
from pong.model.Config import *

from .Assets import Assets

pygame.init()

class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """
    running = False    # Is game running?

    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
            print("hi")
            if event.key == pygame.K_UP:
                Pong.set_speed_left_paddle(-Paddle.PADDLE_SPEED)
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_left_paddle(Paddle.PADDLE_SPEED)
                # TODO
                pass
            elif event.key == pygame.K_q:
                Pong.set_speed_right_paddle(Paddle.PADDLE_SPEED)
                # TODO
                pass
            elif event.key == pygame.K_a:
                Pong.set_speed_right_paddle(-Paddle.PADDLE_SPEED)
                # TODO
                pass

    @classmethod
    def key_released(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Pong.set_speed_left_paddle(0)
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_left_paddle(0)
                # TODO
                pass
            elif event.key == pygame.K_q:
                Pong.set_speed_right_paddle(0)
                # TODO
                pass
            elif event.key == pygame.K_a:
                Pong.set_speed_right_paddle(0)
                # TODO
                pass

    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    @classmethod
    def new_game(cls):
        # TODO rebuild OO model as needed
        pass

    @classmethod
    def kill_game(cls):
        cls.running = False
        # TODO kill all aspects of game

    # -------- Event handling (events sent from model to GUI) ------------

    class ModelEventHandler(EventHandler):
        def on_model_event(self, evt: ModelEvent):
            if evt.event_type == ModelEvent.EventType.NEW_BALL:
                # TODO Optional
                pass
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_PADDLE:
                PongGUI.assets.ball_hit_paddle_sound.play()
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_WALL_CEILING:
                # TODO Optional
                pass

    # ################## Nothing to do below ############################

    # ---------- Theme handling ------------------------------

    assets = Cool()

    @classmethod
    def handle_theme(cls, menu_event):
        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
        last_theme = cls.assets
        try:
            if s == "Cool":
                cls.assets = Cool()
            elif s == "Duckie":
                cls.assets = Duckie()
            else:
                raise ValueError("No such assets " + s)
        except IOError as ioe:
            cls.assets = last_theme

    # ---------- Rendering -----------------
    
    @classmethod
    def render(cls, list_of_movables):
        cls.__load_movable_images(list_of_movables)

        for object in Assets.object_image_map.keys():
            image = Assets.object_image_map[object]
            x= object.get_x()
            y= object.get_y()
            width = object.get_width()
            height = object.get_height()
            cls.__blit_image_at_pos(image, x, y, width, height)
        pygame.display.flip()
        
    @classmethod  
    def __add_background(cls):
        image = cls.assets.get_background()
        cls.__screen.blit(image, (0, 0))
    
    @classmethod 
    def __load_movable_images(cls, list_of_objects):
        ball = list_of_objects["ball"]
        left_paddle = list_of_objects["paddle1"]
        right_paddle = list_of_objects["paddle2"]
        
        cls.bind_ball(ball, cls.assets)
        cls.bind_paddles(left_paddle, right_paddle)

    def bind_paddles(left, right):
        Assets.bind(left,"coolbluepaddle.png")
        Assets.bind(right,"coolredpaddle.png")
        
    def bind_ball(ball, assets):
        if assets == None:
            Cool().get_ball(ball)
        else:
            assets.get_ball(ball)
        
        
    @classmethod   
    def __blit_image_at_pos(cls, image, x, y, width, height):
        image = pygame.transform.scale(image, (width, height))
        cls.__screen.blit(image, (x, y))
     
        
    # ---------- Game loop ----------------

    @classmethod
    def run(cls):
        cls.__screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        cls.__add_background()
        playing = True
        game = Pong()
        list_of_movables = game.get_all_items_with_position()
        while playing:
            
            cls.render(list_of_movables)
           

        # TODO
        pass

    @classmethod
    def update(cls):
        # TODO
        pass

    @classmethod
    def handle_events(cls):
        # TODO
        pass


if __name__ == "__main__":
    PongGUI.run()
