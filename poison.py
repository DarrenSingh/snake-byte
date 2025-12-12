from item import Item


class Poison(Item):

    def __init__(self, position):
        super().__init__(position)
        self.color = (255, 46, 99)
        self.score = -10

    def apply_effect(self, game, snake):
        snake.shrink()
