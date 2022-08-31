class Settings():

    def __init__(self) -> None:
        """Initializing game settings."""
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,100,150)

        self.ship_limit = 3
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6

        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing settings that change during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 0.5

        self.fleet_direction = 1

        self.alien_points = 20

    def increase_speed(self):
        """Change the settings for the speed of entertainment"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


    