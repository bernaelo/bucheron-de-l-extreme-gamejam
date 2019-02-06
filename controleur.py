import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import tour as tour
import typecase as tc
import mechants as m
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1000, 700))

clock = pygame.time.Clock()

terrain = t.Terrain()
terrain.initcases()
collide=terrain.getCollide()
arbres=terrain.getArbres()
posArbres=terrain.getPosArbres()

arbrescoupes=[]
posArbrescoupes=[]

ressorts=terrain.getRessorts()
collide = terrain.getCollide()

vue = vj.Vue()

bucheron = b.Bucheron()
son = pygame.mixer.Sound("Theme.wav")
saut = pygame.mixer.Sound("saut.wav")
attB = pygame.mixer.Sound("attaque_hache.wav")

bucheron.bougergauche(collide)

son.play()
son.set_volume(0.5)
vue.Update(terrain, bucheron, fenetre,arbres)
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
        if keys[pygame.K_SPACE] or pygame.Rect(bucheron.gethitbox()).collidelist(ressorts) != -1:
            if pygame.Rect(bucheron.gethitbox()).collidelist(ressorts) != -1:
                bucheron.setJumpCount(13.7)
            saut.set_volume(0.2)
            saut.play()
            bucheron.setisJump(True)
    else:
            bucheron.sauter(collide)

    if keys[pygame.K_d]:
        attB.set_volume(0.2)
        attB.play()
        bucheron.attack()
    elif keys[pygame.K_LEFT]:
        bucheron.bougergauche(collide)
    elif keys[pygame.K_RIGHT]:
        bucheron.bougerdroite(collide)
    else:
        bucheron.pasbouger()


    if bucheron.getCoupHache():
        i=-1
        if bucheron.getoldleft():
            if not pygame.Rect(bucheron.gethitboxAttG()).collidelist(arbres) == -1:
                for j in range(0,len(arbres)):
                    if pygame.Rect(bucheron.gethitboxAttG()).colliderect(arbres[j]):
                        i=j

        else:
            if not pygame.Rect(bucheron.gethitboxAttD()).collidelist(arbres) == -1:
                for j in range(0,len(arbres)):
                    if pygame.Rect(bucheron.gethitboxAttD()).colliderect(arbres[j]):
                        i=j
        if i!=-1:
            terrain.getCases()[posArbres[i][1]][posArbres[i][0]].setType(tc.typecase.ARBRECOUPE)
            arbrescoupes.append(arbres[i])
            posArbrescoupes.append((posArbres[i]))
            del arbres[i]
            del posArbres[i]
            if bucheron.getbucheportee()<2:
                bucheron.ajoutbuche()

        if len(arbres)<1:
            arbres=arbrescoupes
            posArbres=posArbrescoupes
            arbrescoupes=[]
            posArbrescoupes=[]
            for i in range(0,len(posArbres)):
                terrain.getCases()[posArbres[i][1]][posArbres[i][0]].setType(tc.typecase.ARBRE)

    vue.Update(terrain, bucheron, fenetre,arbres)



pygame.quit()
