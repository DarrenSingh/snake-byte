import sys
import pygame
from settings import *
from snake import Snake


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

        self.clock = pygame.time.Clock()
        self.move_interval = 1.0 / START_SNAKE_SPEED
        self.move_timer = 0.0
        self.dt = 0  # delta time in seconds
        self.game_over = False

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

        if self.move_timer >= self.move_interval:
            self.snake.move()
            self.move_timer -= self.move_interval

        pygame.display.update()

    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        self.screen.fill(pygame.Color(COLOR_BACKGROUND))

        for i, section in enumerate(self.snake.body):
            x, y = section
            if i == 0:
                color = COLOR_HEAD
            else:
                color = COLOR_BODY
            pygame.draw.rect(self.screen, color, [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE])

        pygame.display.flip()
        self.dt = self.clock.tick(FPS) / 1000
