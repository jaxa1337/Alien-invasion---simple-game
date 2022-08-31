from re import L
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class designed to manage missiles launched by a ship."""
    
    def __init__(self, ai_settings, screen, ship) -> None:
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving the missile on the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Display of the missile on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
