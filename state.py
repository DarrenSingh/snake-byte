from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_events(self):
        """
        Handles user inputs from peripherals (mouse, keyboard, etc.)
        """
        pass

    @abstractmethod
    def update(self):
        """
          Updates all game logic
        """
        pass

    @abstractmethod
    def draw(self):
        """
          Handles drawing game assets to the screen
        """
        pass