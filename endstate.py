import pygame

from settings import *
from state import State

class EndState(State):
    def __init__(self, game, final_score):
        super().__init__(game)
        self.final_score = final_score

    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            # keydown triggers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.trigger_game_start()
                elif event.key == pygame.K_m:
                    self.game.trigger_menu()

    def update(self):
        """
        Updates all game logic
        """
        return

    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        self.game.screen.fill(COLOR_DARK_GREY)

        font_title = pygame.font.Font('resources/fonts/PressStart2P-Regular.ttf', UI_FONT_SIZE_TITLE)
        font_instructions = pygame.font.Font('resources/fonts/PressStart2P-Regular.ttf', UI_FONT_SIZE_INSTRUCTIONS)

        text_game_over = font_title.render("GAME OVER", False, COLOR_ERROR)
        text_score = font_instructions.render(f"Final Score: {int(self.final_score)}", True, COLOR_WHITE)
        text_instructions = font_instructions.render("SPACE to Restart", False, COLOR_LIGHT_GREY)

        rect_game_over = text_game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        rect_score = text_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        rect_instruct = text_instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        self.game.screen.blit(text_game_over, rect_game_over)
        self.game.screen.blit(text_score, rect_score)
        self.game.screen.blit(text_instructions, rect_instruct)