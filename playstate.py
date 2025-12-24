import pygame

from settings import *
from state import State
from snake import Snake
from item_manager import ItemManager
from ui import HUD

class PlayState(State):

    def __init__(self, game):
        super().__init__(game)

        self.snake = Snake()
        self.item_manager = ItemManager(self, self.snake)
        self.hud = HUD(game.screen)
        self.move_interval = 1.0 / START_SNAKE_SPEED
        self.move_timer = 0.0
        self.game_timer = 0  # total time elapsed
        self.score = 0
        self.effect_timers = {
            'ghost': 0,
            'speed': 0,
            'turtle': 0,
            'multiplier': 0,
        }

    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.trigger_game_pause(previous_state=self)

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
        self.move_timer += self.game.dt
        self.game_timer += self.game.dt

        if self.move_timer >= self.move_interval:
            self.snake.move()
            if self.snake.check_collision():
                self.game.trigger_game_over(self.score)
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
        self.game.screen.fill(pygame.Color(COLOR_BACKGROUND))
        self.hud.draw(self.score, self.game_timer)
        self.snake.draw(self.game.screen)
        self.item_manager.draw(self.game.screen)

    def add_score(self, score):
        self.score += score