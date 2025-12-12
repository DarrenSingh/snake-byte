import random
from pygame import Vector2, draw

import settings
from food import Food
from gold import Gold
from item import Item
from poison import Poison
from settings import *


class ItemManager:
    """
    Responsible for spawning and managing all the items on the screen
    """

    def __init__(self, game, snake):
        self.items = list()
        self.game = game
        self.snake = snake
        self.screen_start_x = settings.PLAYABLE_GRID_START_X
        self.screen_bound_x = settings.PLAYABLE_GRID_WIDTH_COUNT
        self.screen_start_y = settings.PLAYABLE_GRID_START_Y
        self.screen_bound_y = settings.PLAYABLE_GRID_HEIGHT_COUNT

    def spawn_item(self, item_type: Item = None):
        """
        creates a new item object at a random valid position
        """
        items = [Food, Gold, Poison]
        weight = [75, 10, 15]
        random_item_class = random.choices(items, weight, k=1)[0]
        coordinates: Vector2 = self._get_random_coordinates()
        new_item = random_item_class(coordinates)

        if isinstance(new_item, Poison) and not self.snake.can_shrink():
            self.items.append(Food(self._get_random_coordinates()))
        else:
            self.items.append(new_item)

    def _get_random_coordinates(self):
        existing_item_positions = [item.position for item in self.items]

        while True:
            x = random.randint(0, self.screen_bound_x - 1)
            y = random.randint(self.screen_start_y, self.screen_bound_y - 1)
            coordinates = Vector2(x, y)

            # check if coordinates clashes with snake or existing items
            if coordinates not in self.snake.body and coordinates not in existing_item_positions:
                return coordinates

    def update(self):
        """
        checks if the snakes head has collided with any item.
        if so, applies items affects and removes the item
        """
        if not self.snake.is_healthy or self.snake.check_collision():
            self.game.game_over = True

        positions = [item.position for item in self.items]

        if self.snake.body[0] in positions[:len(positions)]:
            i = positions.index(self.snake.body[0])
            gathered_item = self.items[i]
            gathered_item.apply_effect(self.game, self.snake)

            if hasattr(gathered_item, 'score'):
                self.game.add_score(gathered_item.score)

            self.items.pop(i)
            self.spawn_item()

    def draw(self, screen):
        for item in self.items:
            x, y = item.position
            rect = [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE]
            draw.rect(screen, item.color, rect)
