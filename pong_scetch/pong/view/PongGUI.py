# package pong.view

#from random import randint
import pygame

from pong.model.Pong import Pong
from pong.model.Ball import Ball
from pong.model.Paddle import Paddle
from pong.model.Paddle import PADDLE_SPEED
from pong.model.Config import *

from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler

from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie

from time import sleep

from .Assets import Assets

pygame.init()


class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """
    
    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event: pygame.event) -> None:
        """Handle keypresses, left paddle is controlled with 'q' and 'a' 
        and the right paddle is controlled with 'up-arrow' and 'down-arrow. 
        (event: pygame.event) -> None"""
        if not cls.__running:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Pong.set_speed_right_paddle(-PADDLE_SPEED)
                
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_right_paddle(PADDLE_SPEED)

            elif event.key == pygame.K_q:
                Pong.set_speed_left_paddle(-PADDLE_SPEED)

            elif event.key == pygame.K_a:
                Pong.set_speed_left_paddle(PADDLE_SPEED)


    @classmethod
    def key_released(cls, event: pygame.event) -> None:
        """Handle key releases, When a key is released the corresponding paddles should stop moving. 
        (event: pygame.event) -> None"""
        if not cls.__running:
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Pong.set_speed_right_paddle(0)
     
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_right_paddle(0)
              
            elif event.key == pygame.K_q:
                Pong.set_speed_left_paddle(0)
             
            elif event.key == pygame.K_a:
                Pong.set_speed_left_paddle(0)
         

    # ---- Menu handling (except themes) -----------------

    @classmethod
    def new_game(cls) -> None:
        """Create an instance of the game model. () -> None"""
        cls.game = Pong()


    @classmethod
    def kill_game(cls) -> None:
        """Terminate the game. () -> None"""
        cls.__running = False


    # -------- Event handling (events sent from model to GUI) ------------

    class ModelEventHandler(EventHandler):
        """If ball hit a paddle play the appropriate sound. (EventHandler)"""
        def on_model_event(evt: ModelEvent) -> None:
            if evt.event_type == ModelEvent.EventType.NEW_BALL_RIGHT or evt.event_type == ModelEvent.EventType.NEW_BALL_LEFT:
                pass
            
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_PADDLE:
                if not PongGUI.assets is None:
                    PongGUI.assets.ball_hit_paddle_sound.play()
                
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_WALL_CEILING:
                pass


    # ################## Nothing to do below ############################

    # ---------- Theme handling ------------------------------

    assets = Duckie()


    @classmethod
    def handle_theme(cls, menu_event):
        """Not implemented"""
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
    def render(cls) -> None:
        """Fill the screen with black then apply the background image, render all movable objects and then render the scoreboard. () -> None"""
        cls.__screen.fill((0,0,10)) #Black screen
        cls.__add_background() #Blit the background image to the screen
        cls.__render_moveables() #Step through the image_map and blit the image for the object with the right x, y, width and height
        cls.__render_scores(cls.game) #Scoreboard, shows the points
        
        pygame.display.flip() #Flip the display to show what we have drawn on the display


    @classmethod 
    def __render_moveables(cls) -> None:
        """Blit all objects in the object image map to screen, one at a time. () -> None"""
        for object in Assets.object_image_map.keys():
            image = Assets.object_image_map[object]
            x = object.get_x()
            y = object.get_y()
            width = object.get_width()
            height = object.get_height()
            cls.__blit_image_at_pos(image, x, y, width, height)

            
    @classmethod  
    def __add_background(cls) -> bool:
        """Blit the backgound image to screen. () -> bool"""
        try:
            image = cls.assets.get_background()
            image = pygame.transform.scale(image, (GAME_WIDTH, GAME_HEIGHT))
            cls.__screen.blit(image, (0, 0))
            return False

        except AttributeError:
            return True
        
        
    @classmethod 
    def __load_movable_images(cls, dict_of_objects: dict) -> None:
        """Binds the movable objects to the images representing the objects. (dict of objects) -> None"""
        ball = dict_of_objects["ball"]
        left_paddle = dict_of_objects["paddle1"]
        right_paddle = dict_of_objects["paddle2"]
        #clears the image map before making it new 
        Assets.object_image_map = {}
        cls.bind_ball(ball, cls.assets) 
        cls.bind_paddles(left_paddle, right_paddle)


    def bind_paddles(left: Paddle, right: Paddle) -> None:
        """Bind paddle objects to papddle images. (left: Paddle(), right: Paddle()) -> None"""
        Assets.bind(left,"coolbluepaddle.png")
        Assets.bind(right,"coolredpaddle.png")
        

    def bind_ball(ball: Ball, assets: Duckie) -> None:
        """Bind ball object to ball image. (ball: Ball(), assets: Duckie()) -> None"""
        if assets == None:
            Cool().get_ball(ball)

        else:
            assets.get_ball(ball)
        
        
    @classmethod   
    def __blit_image_at_pos(cls, image: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Blit image to the screen. (image: pygame.Surface, x: int, y: int, width: int, height: int) -> None"""
        image = pygame.transform.scale(image, (width, height))
        cls.__screen.blit(image, (x, y))

        
    # ---------- Score representation---
    
    @classmethod
    def __render_scores(cls, game: Pong) -> None:
        """Blit score board the screen. (game: Pong) -> None"""
        width = 100
        height = 55
        string = cls.__create_score_string(game.get_points_left(), game.get_points_right())
        img = cls.__font.render(string, False, (100, 255, 0))
        cls.__blit_image_at_pos(img, (GAME_WIDTH)/2 - width, 10, width, height)
    
     
    def __create_score_string(left: int, right: int) -> str:
        """Create score board. (left score: int, right score: int) -> str"""
        return f"{left}|{right}"
    

    @classmethod
    def __display_winner(cls) -> None:
        """Blit winner message. () -> None"""
        #Add background to clear the screen
        cls.__add_background()
        width = GAME_WIDTH - 50
        height = GAME_HEIGHT - 120
        string = "winner: " + cls.game.get_winner()
        img = cls.__font.render(string, False, (100,100,100))
        cls.__blit_image_at_pos(img, (GAME_WIDTH-width)/2, 10, width, height)
        
        pygame.display.flip() 

        
    # ---------- Game loop ----------------

    @classmethod
    def setup(cls) -> None:
        """Setup the game before beginning to play. () -> None"""
        cls.__screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) #Initialize a window with size GAME_WIDTH * GAME_HEIGHT
        cls.__clock = pygame.time.Clock() #Clock to track time
        cls.__font = pygame.font.SysFont(None, 24) #System font with size 24
        cls.__add_background() #Blit the imagine on the display window
        cls.__running = True #Running should be set on true for the run loop
        cls.game = Pong() #Initialize the pong model
        list_of_movables = cls.game.get_all_items_with_position() #a dictionary with all positionable objects
        cls.__load_movable_images(list_of_movables) #Binds the images to the moving objects
        
    @classmethod
    def run(cls) -> None:
        """Game startup and loop. () -> None"""
        cls.setup() #Call the setup method
        cls.game.new_ball(False)

        while cls.__running: #The game loop, do this until someone wins or quits
            cls.__clock.tick(60) #Capping the frames per second
            cls.render() #For every loop, we should do a new rendering
            cls.update()


    @classmethod
    def update(cls) -> None:
        """Run the model update, handle events and check for a winner, done every frame in run(). () -> None"""
        cls.game.update()
        cls.__handle_events()
        cls.__check_for_winner()


    @classmethod
    def __check_for_winner(cls) -> None:
        """Check if there is a winner. If winner is found wait 5 sec before terminating game. () -> None"""
        if not cls.game.get_winner() == None:
            cls.__display_winner()
            sleep(5)
            pygame.quit()
            cls.kill_game()


    @classmethod
    def  __handle_events(cls) -> None:
        """Handles incoming events to either quit game or move paddles. () -> None"""
        EventBus.register(cls.ModelEventHandler)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                cls.kill_game()
            # cls.handle_theme(event)
            cls.key_pressed(event)
            cls.key_released(event)


if __name__ == "__main__":
    PongGUI.run()