import pygame
from pygame.sprite import Sprite


class Aliens(Sprite):
    """A sprite to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien and set its rect attribute
        self.image = pygame.image.load("Images/futuristic-spaceship.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the aliens to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

