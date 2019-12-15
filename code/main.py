import pygame
from config import *
from bird import *
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()

    bird_group.draw(screen)

    pygame.display.update()
