import pygame

from settings import *
from state import State

class PauseState(State):

    def __init__(self, game, previous_state):
        super().__init__(game)
        self.previous_state = previous_state

    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.change_state(self.previous_state)


    def update(self):
        """
        Updates all game logic
        """
        return


    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        self.previous_state.draw()
        font_instructions = pygame.font.Font('resources/fonts/PressStart2P-Regular.ttf', UI_FONT_SIZE_INSTRUCTIONS)
        text_instructions = font_instructions.render("Press SPACE to Resume", True, COLOR_LIGHT_GREY)
        rect_instructions = text_instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.game.screen.blit(text_instructions, rect_instructions)

