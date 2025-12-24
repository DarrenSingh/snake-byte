import pygame

from settings import *
from state import State

class MenuState(State):
    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.trigger_game_start()

    def update(self):
        """
        Updates all game logic
        """
        return

    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        # clear screen
        self.game.screen.fill(pygame.Color(COLOR_BACKGROUND))

        # draw a static snake
        body = [(6, 10),(5, 10),(4, 10), (3, 10)]
        for i, section in enumerate(body):
            x, y = section
            if i == 0:
                color = COLOR_HEAD
            else:
                color = COLOR_BODY
            rect = [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE]
            pygame.draw.rect(self.game.screen, color, rect)

        # draw text
        font_title = pygame.font.Font('resources/fonts/PressStart2P-Regular.ttf', UI_FONT_SIZE_TITLE)
        font_instructions = pygame.font.Font('resources/fonts/PressStart2P-Regular.ttf', UI_FONT_SIZE_INSTRUCTIONS)

        text_title = font_title.render("SNAKE BYTE", False, COLOR_WHITE)
        text_instructions = font_instructions.render("Press SPACE to Start", False, COLOR_GREY)

        rect_title = text_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        rect_instructions = text_instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        self.game.screen.blit(text_title, rect_title)
        self.game.screen.blit(text_instructions, rect_instructions)