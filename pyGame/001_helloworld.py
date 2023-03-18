import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY_SURF.fill(WHITE)

pygame.draw.polygon(DISPLAY_SURF, GREEN, ((146, 0), (291, 106), (236, 277),
                                          (56, 277), (0, 106)))
pygame.draw.line(DISPLAY_SURF, BLUE, (60, 60), (120, 60), 4)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
