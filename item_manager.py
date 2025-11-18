import random
from pygame import Vector2

from food import Food
from settings import *


class ItemManager:
    """
    Responsible for spawning and managing all the items on the screen
    """

    def __init__(self, screen_bounds):
        self.items = list()
        self.screen_bound_x, self.screen_bound_y = screen_bounds

    def spawn_item(self):
        """
        creates a new item object at a random valid position
        """
        x = random.randrange(GRID_SIZE, self.screen_bound_x - GRID_SIZE, GRID_SIZE)
        y = random.randrange(GRID_SIZE, self.screen_bound_y - GRID_SIZE, GRID_SIZE)

        new_item = Food(Vector2(x, y))
        self.items.append(new_item)

    def update(self, snake):
        """
        checks if the snakes head has collided with any item.
        if so, applies items affects and removes the item
        :param snake: snake object
        :type snake: Snake
        """
        positions = [item.position for item in self.items]

        if snake.body[0] in positions[:len(positions)]:
            self.items[0].apply_effect(snake)
            self.items.pop()
            self.spawn_item()
