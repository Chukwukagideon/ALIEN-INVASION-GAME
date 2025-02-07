import pygame
from pygame.sprite import Sprite


class Aliens(Sprite):
    """A sprite to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien and set its rect attribute
        self.image = pygame.image.load("Images/futuristic-spaceship.bmp")
        self.image_rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.image_rect.x = self.image_rect.width
        self.image_rect.y = self.image_rect.height

        # store the aliens exact horizontal position
        self.x = float(self.image_rect.x)