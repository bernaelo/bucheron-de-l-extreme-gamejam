import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
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

vue = vj.Vue()

bucheron = b.Bucheron()

#mechant = m.Mechant()

son = pygame.mixer.Sound("Theme.wav")
saut = pygame.mixer.Sound("saut.wav")
attB = pygame.mixer.Sound("attaque_hache.wav")

son.play()
son.set_volume(0.5)
vue.Update(terrain, bucheron, fenetre,arbres)
jumpCount = 10
# mainloop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type==pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()

    if not (bucheron.getisJump()):
        if keys[pygame.K_SPACE]:
            saut.play()
            bucheron.setisJump(True)
    else:
        bucheron.sauter(collide)

    if keys[pygame.K_d]:
        attB.play()
        bucheron.attack()
    elif keys[pygame.K_LEFT]:
        bucheron.bougergauche(collide)
    elif keys[pygame.K_RIGHT]:
        bucheron.bougerdroite(collide)
    else:
        bucheron.pasbouger()

    if bucheron.getCoupHache():
        i=0
        if bucheron.getoldleft():
            if not pygame.Rect(bucheron.gethitboxAttG()).collidelist(arbres) == -1:
                while pygame.Rect(bucheron.gethitboxAttG()).colliderect(arbres[i]) == -1:
                    i+=1
                print(arbres[i][1] /50)
                print("arbre tapé")
                terrain.getCases()[posArbres[i][1]][posArbres[i][0]].setType(tc.typecase.ARBRECOUPE)
                del arbres[i]
                del posArbres[i]
                bucheron.ajoutbuche()
                print("buche : ")
                print(bucheron.getbucheportee())




    vue.Update(terrain, bucheron,fenetre,arbres)
#    mechant.Creer(100, 300, fenetre)
pygame.quit()
