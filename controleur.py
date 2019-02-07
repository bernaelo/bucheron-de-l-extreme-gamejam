import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import tour as to
import typecase as tc
import mechants as m
import RecupText as rete
import projectile as proj

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
    arrowCount = 0
    dCount = 0
    fCount = 0
    spaceCount = 0
    arrowkeys = [pygame.image.load('arrows1.png'), pygame.image.load('arrows2.png'), pygame.image.load('arrows1.png'), pygame.image.load('arrows3.png')]
    dkey = [pygame.image.load('dkey1.png'), pygame.image.load('dkey2.png')]
    fkey = [pygame.image.load('fkey1.png'), pygame.image.load('fkey2.png')]
    spacekey = [pygame.image.load('space1.png'), pygame.image.load('space2.png')]
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

        TextSurf, TextRect = text_objects("Se Déplacer", pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (140, 280)
        fenetre.blit(TextSurf, TextRect)
        fenetre.blit(arrowkeys[arrowCount // 4], (60, 350))
        arrowCount += 1
        if arrowCount > 15:
            arrowCount = 0

        TextSurf, TextRect = text_objects("Sauter", pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (340, 280)
        fenetre.blit(TextSurf, TextRect)
        fenetre.blit(spacekey[spaceCount // 4], (260, 405))
        spaceCount += 1
        if spaceCount > 7:
            spaceCount = 0

        TextSurf, TextRect = text_objects("Attaquer / Couper", pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (580, 280)
        fenetre.blit(TextSurf, TextRect)
        fenetre.blit(dkey[dCount // 4], (555, 405))
        dCount += 1
        if dCount > 7:
            dCount = 0

        TextSurf, TextRect = text_objects("Super Attaque", pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (840, 280)
        fenetre.blit(TextSurf, TextRect)
        fenetre.blit(fkey[fCount // 4], (815, 405))
        fCount += 1
        if fCount > 7:
            fCount = 0

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 800 + 100 > mouse[0] > 800 and 530 + 50 > mouse[1] > 530:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 530, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 430))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 430))
                    attCount += 1
                    pygame.display.flip()
                controles = False
                introloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 530, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Menu", smallText)
        textRect.center = ((800 + (100 / 2)), (530 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)

def créditsloop():
    controles = True
    stopCount = 0
    while controles:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                controles=False
                pygame.quit()
                quit()

        fenetre.fill((255, 255, 255))
        TextSurf, TextRect = text_objects("Crédits", pygame.font.Font('freesansbold.ttf', 70))
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        TextRect.center = ((1000 / 2), 100)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Arrière plan : edermunizz', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (500, 240)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Musique : OrangeHead', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (500, 340)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Sons : findsond, Nintendo', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (500, 440)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Graphismes : Timber Corp', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (500, 540)
        fenetre.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 800 + 100 > mouse[0] > 800 and 530 + 50 > mouse[1] > 530:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 530, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (700, 430))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (705, 430))
                    attCount += 1
                    pygame.display.flip()
                controles = False
                introloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (800, 530, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Menu", smallText)
        textRect.center = ((800 + (100 / 2)), (530 + (50 / 2)))
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
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        fenetre.blit(pygame.image.load('titrejeu.png'), (250, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 100 + 100 > mouse[0] > 100 and 230 + 50 > mouse[1] > 230:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 230, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 130))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 130))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                gameloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 230, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Démarrer", smallText)
        textRect.center = ((100 + (100 / 2)), (230 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton2
        if 100 + 100 > mouse[0] > 100 and 330 + 50 > mouse[1] > 330:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 330, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 230))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 230))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                controlesloop()


        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 330, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Controles", smallText)
        textRect.center = ((100 + (100 / 2)), (330 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton3 Crédits
        if 100 + 100 > mouse[0] > 100 and 430 + 50 > mouse[1] > 430:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 430, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 330))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 330))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                créditsloop()
        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 430, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Crédits", smallText)
        textRect.center = ((100 + (100 / 2)), (430 + (50 / 2)))
        fenetre.blit(textSurf, textRect)

        # bouton4
        if 100 + 100 > mouse[0] > 100 and 530 + 50 > mouse[1] > 530:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 530, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (0, 430))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (5, 430))
                    attCount += 1
                    pygame.display.flip()
                intro = False
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 530, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Quitter", smallText)
        textRect.center = ((100 + (100 / 2)), (530 + (50 / 2)))
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
    missilGravite = proj.projectile(bucheron.getx(), bucheron.gety())
    missilActive = False
    missilDirection = ""
    mechant = m.Mechant("G")
    mechant2 = m.Mechant("D")
    mechant.respawn()
    mechant2.respawn()

    bucheron.bougergauche(collide)


    son.play()
    son.set_volume(0.2)
    vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres, missilGravite)
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
            attB.set_volume(0.1)
            attB.play()
            bucheron.attack()
        elif keys[pygame.K_r]:
            print("BRRRE! BRRRE! PETER LES CHEVILLES !");
            bucheron.attackSpe()
        elif keys[pygame.K_LEFT]:
            bucheron.bougergauche(collide)
        elif keys[pygame.K_RIGHT]:
            bucheron.bougerdroite(collide)
        else:
            bucheron.pasbouger()

        #Exécution de l'attaque Speciale Jutsu
        if bucheron.isAttackingSpe():
            missilActive = True
            missilGravite = proj.projectile(bucheron.getx(), bucheron.gety())
            missilGravite.ajouterhitbox()
            if bucheron.getoldleft():
                missilDirection = "G"
            else:
                missilDirection = "D"

        if missilGravite.getx() < -100 or missilGravite.getx() > 1000:
            missilActive = False
            missilGravite = proj.projectile(bucheron.getx(), bucheron.gety())

        if missilActive:
            if missilDirection == "G":
                missilGravite.shoot("G")
            else:
                missilGravite.shoot("D")
        else:
            missilGravite.retirerhitbox()

        if bucheron.getCoupHache():
            i = -1
            if bucheron.getoldleft():
                if not pygame.Rect(bucheron.gethitboxAttG()).collidelist(arbres) == -1:
                    for j in range(0, len(arbres)):
                        if pygame.Rect(bucheron.gethitboxAttG()).colliderect(arbres[j]):
                            i = j
                if pygame.Rect(bucheron.gethitboxAttG()).colliderect(mechant.gethitbox()):
                    mechant.tuer()
                    mechant.respawn()
                if pygame.Rect(bucheron.gethitboxAttG()).colliderect(mechant2.gethitbox()):
                    mechant2.tuer()
                    mechant2.respawn()

            else:
                if not pygame.Rect(bucheron.gethitboxAttD()).collidelist(arbres) == -1:
                    for j in range(0, len(arbres)):
                        if pygame.Rect(bucheron.gethitboxAttD()).colliderect(arbres[j]):
                            i = j

                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant.gethitbox()):
                    mechant.tuer()
                    mechant.respawn()
                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant2.gethitbox()):
                    mechant2.tuer()
                    mechant2.respawn()
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

        if pygame.Rect(bucheron.gethitbox()).colliderect(terrain.getTour().gethitbox()) and bucheron.getbucheportee() > 0:
            terrain.getTour().augnbbuche(bucheron.getbucheportee())
            bucheron.rstbuche()

        def majmechant(ennemi):
            if pygame.Rect(ennemi.gethitbox()).colliderect(bucheron.gethitbox()):
                if bucheron.getbucheportee() > 0:
                    bucheron.setbucheportee(bucheron.getbucheportee() - 1)
                    # enlever une buche au bucheron

            if pygame.Rect(ennemi.gethitbox()).colliderect(terrain.getTour().gethitbox()):
                ennemi.tuer()
                ennemi.respawn()
                if terrain.getTour().getnbbuche() > 0:
                    terrain.getTour().setnbbuche(terrain.getTour().getnbbuche() - 1)
            else:
                ennemi.deplacer()

        majmechant(mechant)
        majmechant(mechant2)
        print("SAmere la pute : " + str(mechant2.getx()))

        vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres, missilGravite)

        if pygame.time.get_ticks() // 1000 == 180:
            finloop()


introloop()
pygame.quit()
