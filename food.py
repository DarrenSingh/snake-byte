from item import Item


class Food(Item):

    def __init__(self, position):
        super().__init__(position)
        self.color = (203, 243, 187)

    def apply_effect(self, snake):
        snake.grow()
