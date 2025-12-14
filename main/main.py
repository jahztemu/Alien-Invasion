import pygame
import sys
import pygame
from settings import settings
from ship import ship
from bullet import bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = settings()
        self._screen()

        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()

    def _screen(self):
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.move()
            self._update_bullet()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_f:
            self._fullscreen()

        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False

    def _fullscreen(self):
        # Toggle fullscreen
        self.settings.fullscreen = not self.settings.fullscreen
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )
        self.ship.resize(self)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.rocket()
        for bullet_sprite in self.bullets.sprites():
            bullet_sprite.draw_bullet()
        pygame.display.flip()

    def _update_bullet(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
