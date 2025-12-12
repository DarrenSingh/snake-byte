from abc import ABC, abstractmethod
from pygame import Vector2


class Item(ABC):

    def __init__(self, position: Vector2):
        self.effect_duration = 15
        self.color = (147, 191, 199)
        self.position = position
        self.score = 10

    @abstractmethod
    def apply_effect(self, game, snake):
        snake.grow()
