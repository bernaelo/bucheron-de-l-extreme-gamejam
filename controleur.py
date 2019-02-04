import pygame
import terrain as t
import vueJouer as vj
from pygame.locals import *
pygame.init()

terrain=t.Terrain()
vue = vj.Vue()
terre = pygame.image.load('terre.png')
vue.Update(terrain)

run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()




pygame.quit()