import pygame
import os


class ship:
    """manage ship"""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Construct path to image relative to this file
        # current_path = os.path.dirname(__file__)
        # image_path = os.path.join(current_path, "..", "images", "rocket.png")
        self.image = pygame.image.load("images\\rocket.png")
        self.rect = self.image.get_rect()
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.rect.midbottom = self.screen_rect.midbottom

    def move(self):
        """update ship movement base on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 0.5
        if self.moving_down:
            self.rect.y += 0.5

    def rocket(self):
        """drawing ship"""
        self.screen.blit(self.image, self.rect)
