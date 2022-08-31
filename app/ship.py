import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        """Ship initialization and initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Display ship in its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the option that indicates its movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center #5
    
    def center_ship(self):
        """Place the ship in the center of the screen"""
        self.center = self.screen_rect.centerx