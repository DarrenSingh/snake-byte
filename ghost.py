from item import Item


class Ghost(Item):

    def __init__(self, position):
        super().__init__(position)
        self.color = (226, 133, 46)

    def apply_effect(self, game, snake):
        return
