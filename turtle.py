from item import Item


class Turtle(Item):

    def __init__(self, position):
        super().__init__(position)
        self.color = (98, 129, 65)

    def apply_effect(self, game, snake):
        return