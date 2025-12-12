from item import Item


class Gold(Item):

    def __init__(self, position):
        super().__init__(position)
        self.color = (226, 133, 46)
        self.score = 50

    def apply_effect(self, game, snake):
        snake.grow()
