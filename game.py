import sys
import pygame
from settings import *
from snake import Snake
from item_manager import ItemManager
from ui import HUD


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
        self.snake = Snake()
        self.item_manager = ItemManager(self, self.snake)
        self.hud = HUD(self.screen)

        self.clock = pygame.time.Clock()
        self.move_interval = 1.0 / START_SNAKE_SPEED
        self.move_timer = 0.0
        self.dt = 0  # delta time in seconds
        self.game_timer = 0  # total time elapsed

        self.game_over = False
        self.score = 0
        self.effect_timers = {
            'ghost': 0,
            'speed': 0,
            'turtle': 0,
            'multiplier': 0,
        }

    def run(self):
        """
        Main game loop, runs until exited
        """
        while not self.game_over:
            self.handle_events()
            self.draw()
            self.update()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.snake.change_direction("UP")
        elif keys[pygame.K_s]:
            self.snake.change_direction("DOWN")
        elif keys[pygame.K_a]:
            self.snake.change_direction("LEFT")
        elif keys[pygame.K_d]:
            self.snake.change_direction("RIGHT")

    def update(self):
        """
        Updates all game logic
        """
        self.move_timer += self.dt
        self.game_timer += self.dt
        self.score += self.dt * 1.5

        if self.move_timer >= self.move_interval:
            self.snake.move()
            self.game_over = self.snake.check_collision()
            self.move_timer -= self.move_interval

        # handle item collision
        if len(self.item_manager.items) == 0:
            self.item_manager.spawn_item()
        else:
            self.item_manager.update()

        pygame.display.update()

    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        self.screen.fill(pygame.Color(COLOR_BACKGROUND))
        self.hud.draw(self.score, self.game_timer)
        self.snake.draw(self.screen)
        self.item_manager.draw(self.screen)

        pygame.display.flip()
        self.dt = self.clock.tick(FPS) / 1000

    def add_score(self, score):
        self.score += score
