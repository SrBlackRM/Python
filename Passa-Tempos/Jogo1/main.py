
import pygame
import field
from sys import exit

fieldCreate = field.battlefield()
#fieldCreate.showObstacles()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


