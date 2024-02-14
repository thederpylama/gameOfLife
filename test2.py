import pygame
from pygame.locals import *
import time

pygame.init()

window = pygame.display.set_mode((1001, 1001))

window.fill((255, 255, 255))

y = 1

for i in range(100):
    x = 1
    for j in range(100):
        pygame.draw.rect(window, (0, 0, 255), [x, y, 9, 9], )
        x+= 10

    y+=10


pygame.display.update()

time.sleep(5)
pygame.quit()

#while True: