# package pong.view
import random
import time

import pygame

from pong.model import *
from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.model.Ball import Ball
from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie

from pong.model.Paddle import PADDLE_SPEED, Paddle
from pong.model.Config import *
from pong.model.Pong import Pong

pygame.init()


class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """

    BLACK = (0, 0, 0)
    SOME_COLOR = (50, 5, 75)

    def __init__(self):
        left_paddle = self.__create_left_paddle()
        right_paddle = self.__create_right_paddle()
        ball = self.__create_ball()
        self.ctr_model = Pong(ball, left_paddle, right_paddle)

    screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
    points_font = pygame.font.SysFont(None, 36)
    clock = pygame.time.Clock()

    @classmethod
    def __create_points_left_image(cls, points_left):
        text_left = f"Points: {points_left}"
        img = cls.points_font.render(text_left, True, cls.SOME_COLOR)
        rect = img.get_rect()
        return img, rect

    @classmethod
    def __create_points_right_image(cls, points_right):
        text_right = f"Points: {points_right}"
        img = cls.points_font.render(text_right, True, cls.SOME_COLOR)
        rect = img.get_rect()
        return img, rect

    @staticmethod
    def __create_right_paddle():
        return Paddle(GAME_WIDTH-PADDLE_WIDTH, GAME_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT, 0, 0)

    @staticmethod
    def __create_left_paddle():
        return Paddle(0, GAME_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT, 0, 0)

    @staticmethod
    def __create_ball():
        return Ball(GAME_WIDTH / 2, GAME_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT, 1, 1)

    running = False  # Is game running?

    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                # TODO
                pass
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
                # TODO
                pass

    @classmethod
    def key_released(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                # TODO
                pass
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
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

    assets = None

    def handle_theme(self, menu_event):
        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
        last_theme = self.assets
        try:
            if s == "Cool":
                self.assets = Cool()
            elif s == "Duckie":
                self.assets = Duckie()
            else:
                raise ValueError("No such assets " + s)
        except IOError as ioe:
            self.assets = last_theme

    # ------- pygame graphics for rendering --------

    # ---------- Rendering -----------------

    def render(self):
        self.draw_background()
        self.show_points()
        self.draw_left_paddle()
        self.draw_right_paddle()
        #self.__draw_ball()
        self.update_screen()

    @classmethod
    def update_screen(cls):
        pygame.display.flip()

    def draw_background(self):
        self.screen.fill(self.BLACK)

    # ---------- Game loop ----------------
    def run(self):
        # TODO
        keep_running = True
        while keep_running:
            self.clock.tick(GAME_SPEED)
            self.update()
            keep_running = self.handle_events()
        pygame.quit()

    def update(self):
        # TODO
        self.ctr_model.update(time.time_ns())
        self.render()
        print("calling update method")

    def handle_events(self):
        # TODO
        keep_going = True
        events = pygame.event.get()
        for event in events:
            self.__handle_key_events(event)
            keep_going &= self.__check_for_quit(event)
        return keep_going

    def __handle_key_events(self, event):
        self.key_pressed(event)
        self.key_pressed(event)

    @classmethod
    def __check_for_quit(cls, event):
        return event.type != pygame.QUIT

    @classmethod
    def show_points(cls):
        points_left = Pong.get_points_right()
        points_right = Pong.get_points_left()
        img_left, rect_left = cls.__create_points_left_image(points_left)
        img_right, rect_right = cls.__create_points_right_image(points_right)
        cls.draw_points_left(img_left, rect_left)
        cls.draw_points_right(img_right, rect_right)

    @classmethod
    def draw_points_left(cls, img, rect):
        rect.topleft = (20, 20)
        cls.screen.blit(img, rect)

    @classmethod
    def draw_points_right(cls, img, rect):
        rect.topleft = (GAME_WIDTH - 150, 20)
        cls.screen.blit(img, rect)

    def draw_left_paddle(self):
        left_paddle = self.ctr_model.get_left_paddle()
        left_paddle_image = self.SOME_COLOR
        pygame.draw.rect(self.screen, left_paddle_image,
                         (left_paddle.get_x(), left_paddle.get_y(), left_paddle.get_width(), left_paddle.get_height()))

    def draw_right_paddle(self):
        right_paddle = self.ctr_model.get_right_paddle()
        right_paddle_image = self.SOME_COLOR
        pygame.draw.rect(self.screen, right_paddle_image,
                         (right_paddle.get_x(), right_paddle.get_y(), right_paddle.get_width(), right_paddle.get_height()))


if __name__ == "__main__":
    GUI = PongGUI()
    GUI.run()
