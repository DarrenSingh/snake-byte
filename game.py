import sys
import pygame

from playstate import PlayState
from pausestate import PauseState
from endstate import EndState
from menustate import MenuState

from settings import *

class Game:
    """
    Manages the main game loop, game state, and game objects
    """

    def __init__(self):
        """
        Initialize the game, screen, clock and game variables
        """
        pygame.init()
        pygame.display.set_caption('Snake Byte')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0  # delta time in seconds

        self.state = MenuState(self)

    def change_state(self, new_state):
        self.state = new_state

    def trigger_menu(self):
        self.change_state(MenuState(self))

    def trigger_game_start(self):
        self.change_state(PlayState(self))

    def trigger_game_pause(self, previous_state):
        self.change_state(PauseState(self, previous_state))

    def trigger_game_over(self, score):
        self.change_state(EndState(self,score))

    def run(self):
        """
        Main game loop, runs until exited
        """
        while self.running:
            self.state.handle_events()
            self.state.update()
            self.state.draw()
            self.dt = self.clock.tick(FPS) / 1000
            pygame.display.flip()

        pygame.quit()
        sys.exit()
