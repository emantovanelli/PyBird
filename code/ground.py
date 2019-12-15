import pygame
from pygame.locals import *

from config import *


class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('../assets/sprites/base.png')
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect[0] -= GAME_SPEED
