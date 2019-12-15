import pygame
from pygame.locals import *

from config import *


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load(
                '../assets/sprites/bluebird-upflap.png').convert_alpha(),
            pygame.image.load(
                '../assets/sprites/bluebird-midflap.png').convert_alpha(),
            pygame.image.load(
                '../assets/sprites/bluebird-downflap.png').convert_alpha()
        ]

        self.current_image = 0
        self.image = pygame.image.load(
            '../assets/sprites/bluebird-midflap.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
