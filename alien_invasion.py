import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen, update_bullets, create_fleet, update_aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    play_button = Button(ai_settings, screen, "Nowa gra")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(screen, ai_settings)
 
    bullets = Group()
    aliens = Group()
    
    create_fleet(ai_settings, screen, ship, aliens)
 
    while True:

        check_events(ai_settings, screen, sb, stats, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, stats, sb, bullets, ship, aliens)
            update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        update_screen(screen, ai_settings, stats, sb, ship, aliens, bullets, play_button)


run_game()
