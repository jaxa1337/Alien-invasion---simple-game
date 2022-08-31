import os

class GameStats():
    """In-game statistics monitoring"""

    def __init__(self, ai_settings) -> None:
        """Initialization of statistical data"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.ship_left = self.ai_settings.ship_limit
        self.game_active = False
        
        if os.path.isfile("data/max_score.txt"):
            with open("data/max_score.txt") as file:
                self.high_score = int(file.readline())
        else:
            self.high_score = 0

    def reset_stats(self):
        """
        Initialization of statistical data that may change during the game
        """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1