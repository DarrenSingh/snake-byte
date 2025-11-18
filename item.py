from abc import ABC, abstractmethod
from pygame import Vector2


class Item(ABC):

    def __init__(self, position: Vector2):
        self.position = position
        self.color = (147, 191, 199)

    @abstractmethod
    def apply_effect(self, snake):
        snake.grow()
