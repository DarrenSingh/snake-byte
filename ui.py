import pygame
import math
import settings
from settings import *


class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font_hud = pygame.font.Font(None, settings.UI_FONT_SIZE_HUD)
        pass

    def draw(self, score, time_elapsed):
        # HUD Background Bar
        pygame.draw.rect(self.screen, COLOR_HUD_BG, (0, 0, SCREEN_WIDTH, 40))
        pygame.draw.line(self.screen, COLOR_ACCENT, (0, 40), (SCREEN_WIDTH, 40), 2)

        # Score : aligned left
        score_surf = self.font_hud.render(f"SCORE: {int(score)}", True, COLOR_WHITE)
        self.screen.blit(score_surf, (20, 10))

        # Time : aligned center
        time_str = str(math.floor(round(time_elapsed)))
        time_surf = self.font_hud.render(f"TIME: {time_str}", True, COLOR_WHITE)
        # Center the time text horizontally
        time_rect = time_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=10)
        self.screen.blit(time_surf, time_rect)
        pass

