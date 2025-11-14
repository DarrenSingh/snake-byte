from collections import deque
from pygame import Vector2


class Snake:
    """
    Manages the snake's body, movement and collision logic
    """

    def __init__(self):
        self.body = deque([Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)])
        self.direction = Vector2(1, 0)
        self.is_growing = False
        self.speed = 15

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

    def change_direction(self, new_direction: Vector2):
        """
        Updates the snakes direction, while preventing 180-degree turns
        :param new_direction: The new direction to move
        :type new_direction: Vector2
        """
        if new_direction != self.direction * -1:
            self.direction = new_direction

    def check_collision(self):
        """
        Checks if head Vector2 coordinate exists in the rest of the body deque collection
        :return: if the snakes head collided with its body
        :rtype: bool
        """
        if self.body.count(self.body[0]) > 1:
            return True

    def adjust_speed(self, speed_adjustment: int):
        """
        Adjust the speed at which the snake moves, relative to the previous speed
        :param speed_adjustment:
        :type speed_adjustment: int
        """
        self.speed += speed_adjustment
