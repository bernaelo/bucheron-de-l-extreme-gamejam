import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import mechants as m
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1000, 700))

clock = pygame.time.Clock()

terrain = t.Terrain()
collide=terrain.initcases()
vue = vj.Vue()
bucheron = b.Bucheron()
#mechant = m.Mechant()
son = pygame.mixer.Sound("Theme.wav")
saut = pygame.mixer.Sound("saut.wav")

son.play()
son.set_volume(0.5)
vue.Update(terrain, bucheron, fenetre)
jumpCount = 10
# mainloop
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type==pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bucheron.bougergauche(collide)
    elif keys[pygame.K_RIGHT]:
        bucheron.bougerdroite(collide)
    else:
        bucheron.pasbouger()

    if not (bucheron.getisJump()):
        if keys[pygame.K_SPACE]:
            saut.play()
            saut.set_volume(0.3)
            bucheron.setisJump(True)


    else:
        bucheron.sauter(collide)

    vue.Update(terrain, bucheron,fenetre)
#    mechant.Creer(100, 300, fenetre)
pygame.quit()
