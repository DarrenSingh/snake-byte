import sys
import pygame
from settings import *
from snake import Snake
from item_manager import ItemManager


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
        self.item_manager = ItemManager([SCREEN_WIDTH, SCREEN_HEIGHT])

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

        # handle collision
        #   check if snake has collided with item through item_manager
        if len(self.item_manager.items) == 0:
            self.item_manager.spawn_item()
        else:
            self.item_manager.update(self.snake)

        if self.snake.check_collision():
            self.game_over = True

        pygame.display.update()

    def draw(self):
        """
        Handles drawing game assets to the screen
        """
        self.screen.fill(pygame.Color(COLOR_BACKGROUND))

        # draw snake
        for i, section in enumerate(self.snake.body):
            x, y = section
            if i == 0:
                color = COLOR_HEAD
            else:
                color = COLOR_BODY
            pygame.draw.rect(self.screen, color, [x, y, GRID_SIZE, GRID_SIZE])

        # draw items
        #   get items from item_manager and draw to screen
        for item in self.item_manager.items:
            x, y = item.position
            pygame.draw.rect(self.screen, item.color, [x, y, GRID_SIZE, GRID_SIZE])

        pygame.display.flip()
        self.dt = self.clock.tick(FPS) / 1000
