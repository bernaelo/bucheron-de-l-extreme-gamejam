import pygame
import pygame as pygame

import terrain as t
import vueJouer as vj
import bucheron as b
import tour as tour
import mechants as m
import mechants as m2
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1000, 700))

clock = pygame.time.Clock()

terrain = t.Terrain()
terrain.initcases()
collide=terrain.getCollide()
ressorts=terrain.getRessorts()
collide = terrain.getCollide()
vue = vj.Vue()
bucheron = b.Bucheron()
mechant = m.Mechant()
mechant2 = m2.Mechant()
mechant2.recréerGauche()
son = pygame.mixer.Sound("Theme.wav")
saut = pygame.mixer.Sound("saut.wav")
attB = pygame.mixer.Sound("attaque_hache.wav")


son.set_volume(0.5)
son.play()
vue.Update(terrain, bucheron, fenetre, mechant, mechant2)
jumpCount = 10
# mainloop
run = True
while run:
    clock.tick(40)

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()



    if not (bucheron.getisJump()):
        if keys[pygame.K_SPACE]:
            saut.set_volume(0.2)
            saut.play()
            bucheron.setisJump(True)
    else:
        bucheron.sauter(collide)
        #bucheron.sauter(ressorts)

    if keys[pygame.K_d]:
        attB.set_volume(0.2)
        attB.play()
        bucheron.attack()
    elif keys[pygame.K_LEFT]:
        bucheron.bougergauche(collide)
        #bucheron.bougergauche(ressorts)
    elif keys[pygame.K_RIGHT]:
        bucheron.bougerdroite(collide)
        #bucheron.bougerdroite(ressorts)
    else:
        bucheron.pasbouger()

    vue.Update(terrain, bucheron, fenetre, mechant, mechant2)

pygame.quit()
