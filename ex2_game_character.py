import pygame

class GameCharacter:
    """Class to manage game character"""

    def __init__(self, character):
        self.screen = character.screen
        self.screen_rect = character.screen.get_rect()
        self.settings = character.settings

        # load the character image and get it's rect
        self.image = pygame.image.load("Images/futuristic-spaceship.bmp")
        self.image_rect = self.image.get_rect()

        # start and position the character at the center of the screen
        self.image_rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the game character at its current location"""
        self.screen.blit(self.image, self.image_rect)