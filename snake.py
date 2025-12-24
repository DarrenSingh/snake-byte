from collections import deque
from pygame import Vector2, draw
from settings import *


class Snake:
    """
    Manages the snake's body, movement and collision logic
    """

    def __init__(self):
        self.body = deque([Vector2(6, 10), Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)])
        self.direction = Vector2(1, 0)
        self.is_growing = False

    def draw(self, screen):
        for i, section in enumerate(self.body):
            x, y = section
            if i == 0:
                color = COLOR_HEAD
            else:
                color = COLOR_BODY
            rect = [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE]
            draw.rect(screen, color, rect)

    def move(self):
        """
        Moves the snake one step in its current direction
        Handles growing by not popping the tail if is_growing is True
        """
        head = self.body[0]
        new_head = head + self.direction
        self.body.appendleft(new_head)

        if not self.is_growing:
            self.body.pop()
        self.is_growing = False

    def grow(self):
        """
        Handles setting the state of whether the snake is growing
        """
        self.is_growing = True

    def can_shrink(self):
        return len(self.body) != 2

    def shrink(self):
        """
        Removes tail end from the snake
        """
        self.body.pop()

    def change_direction(self, direction_str: str):
        """
        Updates the snakes direction based on a string command ("UP","DOWN","LEFT","RIGHT"),
        while preventing 180-degree turns
        :param direction_str: The new direction to move
        :type direction_str: str
        """
        new_direction = self.direction

        if direction_str == "UP":
            new_direction = Vector2(0, -1)
        elif direction_str == "DOWN":
            new_direction = Vector2(0, 1)
        elif direction_str == "LEFT":
            new_direction = Vector2(-1, 0)
        elif direction_str == "RIGHT":
            new_direction = Vector2(1, 0)

        if new_direction != -self.direction:
            self.direction = new_direction

    def check_collision(self):
        """
        Checks if head Vector2 coordinate exists in the rest of the body deque collection
        :return: if the snakes head collided with its body
        :rtype: bool
        """
        if self.body.count(self.body[0]) > 1:
            return True

    def is_healthy(self):
        return len(self.body) > 1
