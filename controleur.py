import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import mechants as m
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

clock = pygame.time.Clock()

terrain = t.Terrain()
vue = vj.Vue()
bucheron = b.Bucheron()
mechant = m.Mechant()

vue.Update(terrain, bucheron, fenetre)
jumpCount = 10
# mainloop
run = True
while run:
    clock.tick(18)
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bucheron.bougergauche()
    elif keys[pygame.K_RIGHT]:
        bucheron.bougerdroite()
    else:
        bucheron.pasbouger()

    if not (bucheron.getisJump()):
        if keys[pygame.K_SPACE]:
            bucheron.setisJump(True)
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:

            bucheron.sety(bucheron.gety() - (jumpCount * abs(jumpCount)) * 0.5)
            jumpCount -= 1
        else:
            bucheron.setisJump(False)
            jumpCount = 10

    vue.Update(terrain, bucheron,fenetre)
    mechant.Creer(100, 300, fenetre)
pygame.quit()s
