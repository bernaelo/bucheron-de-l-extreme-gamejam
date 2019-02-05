import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
from pygame.locals import *

pygame.init()


terrain=t.Terrain()
vue = vj.Vue()
fdp = b.Bucheron()
vue.Update(terrain,fdp)

# mainloop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        fdp.bougergauche()
    elif keys[pygame.K_RIGHT]:
        fdp.bougerdroite()
    else:
        fdp.pasbouger()

    if not (fdp.getisJump()):
        if keys[pygame.K_SPACE]:
            fdp.setisJump(True)
            right = False
            left = False
            walkCount = 0
    else:
        fdp.sauter()

    vue.Update(terrain, fdp)

pygame.quit()