import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import tour as to
import typecase as tc
import mechants as m
import RecupText as rete
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1000, 700))

pygame.display.set_caption('Menu')
clock = pygame.time.Clock()
immobileDroite = [pygame.image.load('Bucheron-Stop-Right0.png'), pygame.image.load('Bucheron-Stop-Right1.png')]
attaqueDroite = [pygame.image.load('att D1.png'), pygame.image.load('att D3.png')]
terrain = t.Terrain()

def finloop():
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        nomJoueurCourant = rete.name(fenetre)
        print("nom : ", nomJoueurCourant)
        print("score : ", terrain.getTour().getnbbuche())
        introloop()


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def controlesloop():
    controles = True
    stopCount = 0
    while controles:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                controles = False
                pygame.quit()
                quit()

        fenetre.fill((255, 255, 255))
        TextSurf, TextRect = text_objects("Instructions", pygame.font.Font('freesansbold.ttf', 70))
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        TextRect.center = ((1000 / 2), 100)
        fenetre.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Déplacement : ", pygame.font.Font('freesansbold.ttf', 20))
        TextRect.center = (80, 200)
        fenetre.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 800 + 100 > mouse[0] > 800 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 500, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 400))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 400))
                    attCount += 1
                    pygame.display.flip()
                controles = False
                introloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 500, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Menu", smallText)
        textRect.center = ((800 + (100 / 2)), (500 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton2
        if 800 + 100 > mouse[0] > 800 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 400, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 300))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 300))
                    attCount += 1
                    pygame.display.flip()
                controles = False
                instructionsloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 400, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ((800 + (100 / 2)), (400 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def instructionsloop():
    highscore = True
    stopCount = 0
    while highscore:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                highscore = False
                pygame.quit()
                quit()

        fenetre.fill((255, 255, 255))
        TextSurf, TextRect = text_objects("Instructions", pygame.font.Font('freesansbold.ttf', 70))
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        TextRect.center = ((1000 / 2), 100)
        TextSurf, TextRect = text_objects('aaaaaa \n bbbbbbb', pygame.font.Font('freesansbold.ttf', 20))
        TextRect.center = (80, 200)
        fenetre.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 800 + 100 > mouse[0] > 800 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 500, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 400))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 400))
                    attCount += 1
                    pygame.display.flip()
                highscore = False
                introloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 500, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Menu", smallText)
        textRect.center = ((800 + (100 / 2)), (500 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton2
        if 800 + 100 > mouse[0] > 800 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 400, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 300))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 300))
                    attCount += 1
                    pygame.display.flip()
                highscore = False
                controlesloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 400, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Controles", smallText)
        textRect.center = ((800 + (100 / 2)), (400 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def introloop():
    intro = True
    stopCount = 0

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()

        fenetre.fill((255, 255, 255))
        largeText = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects("Bucheron De L'Extreme", largeText)
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        TextRect.center = ((1000 / 2), 100)
        fenetre.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 100 + 100 > mouse[0] > 100 and 300 + 50 > mouse[1] > 300:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 300, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 200))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 200))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                gameloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 300, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Démarrer", smallText)
        textRect.center = ((100 + (100 / 2)), (300 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton2
        if 100 + 100 > mouse[0] > 100 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 400, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 300))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 300))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                instructionsloop()


        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 400, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ((100 + (100 / 2)), (400 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton3
        if 100 + 100 > mouse[0] > 100 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 500, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 400))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 400))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 500, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Quitter", smallText)
        textRect.center = ((100 + (100 / 2)), (500 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def gameloop():

    terrain.initcases()
    collide = terrain.getCollide()
    arbres = terrain.getArbres()
    posArbres = terrain.getPosArbres()

    arbrescoupes = []
    posArbrescoupes = []

    ressorts = terrain.getRessorts()
    collide = terrain.getCollide()

    vue = vj.Vue()

    bucheron = b.Bucheron()
    son = pygame.mixer.Sound("Theme.wav")
    saut = pygame.mixer.Sound("saut.wav")
    attB = pygame.mixer.Sound("attaque_hache.wav")

    bucheron.bougergauche(collide)
    mechant = m.Mechant()
    mechant2 = m.Mechant()

    mechant2.recréerGauche()

    son.play()
    son.set_volume(0.5)
    vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres)
    jumpCount = 10

    # mainloop
    gameexit = False
    while not (gameexit):
        clock.tick(60)

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:
                gameexit = True
                pygame.quit()
                quit()

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
            i = -1
            if bucheron.getoldleft():
                if not pygame.Rect(bucheron.gethitboxAttG()).collidelist(arbres) == -1:
                    for j in range(0, len(arbres)):
                        if pygame.Rect(bucheron.gethitboxAttG()).colliderect(arbres[j]):
                            i = j
                if pygame.Rect(bucheron.gethitboxAttG()).colliderect(mechant.gethitbox()):
                    mechant.suprimer()
                    mechant.recréerDroite()
                if pygame.Rect(bucheron.gethitboxAttG()).colliderect(mechant2.gethitbox()):
                    mechant2.suprimer()
                    mechant2.recréerGauche()

            else:
                if not pygame.Rect(bucheron.gethitboxAttD()).collidelist(arbres) == -1:
                    for j in range(0, len(arbres)):
                        if pygame.Rect(bucheron.gethitboxAttD()).colliderect(arbres[j]):
                            i = j

                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant.gethitbox()):
                    mechant.suprimer()
                    mechant.recréerDroite()
                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant2.gethitbox()):
                    mechant2.suprimer()
                    mechant2.recréerGauche()
            if i != -1:
                terrain.getCases()[posArbres[i][1]][posArbres[i][0]].setType(tc.typecase.ARBRECOUPE)
                arbrescoupes.append(arbres[i])
                posArbrescoupes.append((posArbres[i]))
                del arbres[i]
                del posArbres[i]
                if bucheron.getbucheportee() < 2:
                    bucheron.ajoutbuche()

            if len(arbres) < 1:
                arbres = arbrescoupes
                posArbres = posArbrescoupes
                arbrescoupes = []
                posArbrescoupes = []
                for i in range(0, len(posArbres)):
                    terrain.getCases()[posArbres[i][1]][posArbres[i][0]].setType(tc.typecase.ARBRE)

        if pygame.Rect(bucheron.gethitbox()).colliderect(
                terrain.getTour().gethitbox()) and bucheron.getbucheportee() > 0:
            terrain.getTour().augnbbuche(bucheron.getbucheportee())
            bucheron.rstbuche()

        vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres)

        if pygame.time.get_ticks() // 1000 == 5:
            finloop()
            print("FIN DU JEU TA MERE LA PUTE")


introloop()
pygame.quit()
