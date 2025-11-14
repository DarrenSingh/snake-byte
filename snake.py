from collections import deque
from pygame import Vector2


class Snake:

    # methods
    def __init__(self):
        self.body = deque([Vector2(8, 10), Vector2(7, 10), Vector2(6, 10), Vector2(5, 10), Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)])
        self.direction = Vector2(1, 0)
        self.is_growing = False
        self.speed = 5

    def move(self):
        # add new block to head in current direction, if not is_growing
        # call popleft to remove tail
        head = self.body[0]
        new_head = head + self.direction
        self.body.appendleft(new_head)

        if not self.is_growing:
            self.body.pop()
        self.is_growing = False

    def grow(self):
        self.is_growing = True

    # updates direction only if new direction is not opposite of the current direction
    def change_direction(self, new_direction: Vector2):
        if new_direction != self.direction * -1:
            self.direction = new_direction

    # returns true if the head is in the rest of the body
    def check_collision(self):
        # check if head Vector2 is in the rest of the body deque
        if self.body.count(self.body[0]) > 1:
            return True

    def adjust_speed(self, speed_adjustment: int):
        self.speed += speed_adjustment
