import pygame
import terrain as t
import vueJouer as vj
import bucheron as b
import tour as to
import typecase as tc
import mechants as m
import RecupText as rete
import projectile as proj
import pickle as pk

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

        nom = rete.name(fenetre)
        new_score = str(terrain.getTour().getnbbuche())

        ##Permet de reset tout le fichier des scores (supprime les high scores donc WOLAH FAUT PAS Y TOUCHER)
        # scores = []
        # fichier = open("scores.txt","wb")
        # pickled = pk.Pickler(fichier)
        # pickled.dump(scores)
        # fichier.close()

        ## Récupération des scores
        with open("scores.txt", "rb") as fichier:  # Ouverture en binaire
            unpickled = pk.Unpickler(fichier)
            scores = unpickled.load()  # On récupère la variable
            fichier.close()
            print(scores)

        ##Verification des scores existants ou inexistants selon les noms
        try:
            nom_list = [score[0] for score in scores]  # création de la liste des noms
            index = nom_list.index(nom)  # recherche du joueur
            # Si le joueur a un score:
            print("Le joueur {} a déjà un score. il est à l'index n°{} de la liste".format(nom, index))
            if new_score > scores[index][1]:  # et que son nouveau score est mieux
                scores[index][1] = new_score
        except ValueError:  # Si le joueur n'a pas de score précédent / index(nom) renvoie une ValueError si il trouve pas nom
            print("Le joueur n'a pas de scores précédents")
            scores.append([nom, new_score])  # Ajout du score
        print(scores)

        ## Sauvegarde des scores
        with open("scores.txt", "wb") as fichier:
            pickled = pk.Pickler(fichier)
            pickled.dump(scores)
            fichier.close()

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
    arrowkeys = [pygame.image.load('arrows1.png'), pygame.image.load('arrows2.png'), pygame.image.load('arrows1.png'),
                 pygame.image.load('arrows3.png')]
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
            fenetre.blit(immobileDroite[stopCount // 4], (725, 485))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (730, 485))
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
                controles = False
                pygame.quit()
                quit()

        fenetre.fill((255, 255, 255))
        TextSurf, TextRect = text_objects("Crédits", pygame.font.Font('freesansbold.ttf', 70))
        fenetre.blit(pygame.image.load('background.png'), (0, 0))
        TextRect.center = ((1000 / 2), 100)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Arrière plan : edermunizz', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (200, 240)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Musique : OrangeHead', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (200, 340)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Sons : findsond, Nintendo', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (200, 440)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Graphismes : Timber Corp', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (200, 540)
        fenetre.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Membre de Timber Corp :', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 240)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Damien Brill', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 300)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Eloi Bernard', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 360)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Mathieu Milliez', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 420)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Simon Loraux', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 480)
        fenetre.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects('Yamine El Mir', pygame.font.Font('freesansbold.ttf', 25))
        TextRect.center = (600, 540)
        fenetre.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 850 + 100 > mouse[0] > 850 and 580 + 50 > mouse[1] > 580:
            pygame.draw.rect(fenetre, (100, 100, 100), (850, 580, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (775, 535))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (775, 535))
                    attCount += 1
                    pygame.display.flip()
                controles = False
                introloop()

        else:
            pygame.draw.rect(fenetre, (100, 100, 100), (850, 580, 100, 50))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Menu", smallText)
        textRect.center = ((850 + (100 / 2)), (580 + (50 / 2)))
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

        with open("scores.txt", "rb") as fichier:  # Ouverture en binaire
            unpickled = pk.Unpickler(fichier)
            scores = unpickled.load()  # On récupère la variable
            i=0
            j=250
            while i <= 1:
                TextSurf, TextRect = text_objects(str(scores[i][0]), pygame.font.Font('freesansbold.ttf', 25))
                TextRect.center = (650, j)
                fenetre.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects(str(scores[i][1]), pygame.font.Font('freesansbold.ttf', 25))
                TextRect.center = (750, j)
                fenetre.blit(TextSurf, TextRect)
                i += 1
                j += 100
            fichier.close()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # bouton1
        if 100 + 100 > mouse[0] > 100 and 230 + 50 > mouse[1] > 230:
            pygame.draw.rect(fenetre, (100, 100, 100), (100, 230, 100, 50))
            fenetre.blit(immobileDroite[stopCount // 4], (25, 185))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (30, 185))
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
            fenetre.blit(immobileDroite[stopCount // 4], (25, 285))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (30, 285))
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
            fenetre.blit(immobileDroite[stopCount // 4], (25, 385))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (30, 385))
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
            fenetre.blit(immobileDroite[stopCount // 4], (25, 485))
            stopCount += 1
            if stopCount > 7:
                stopCount = 0
            if click[0] == 1:
                attCount = 0
                while attCount < 1:
                    fenetre.blit(attaqueDroite[attCount], (30, 485))
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
    lesmechants = []

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

    debutjeu = pygame.time.get_ticks() // 1000
    son.play()
    son.set_volume(0.2)
    vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres, missilGravite, debutjeu)
    jumpCount = 10

    # mainloop
    gameexit = False

    timer=180

    while ((not (gameexit)) and (timer >=0)):
        clock.tick(60)

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:
                gameexit = True
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if bucheron.getchargeUltim() > 7:
            bucheron.setchargeUltim(8)

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
        elif keys[pygame.K_r] and bucheron.getchargeUltim() > 7:
            print("FUCK FUCK FUCK FUCK!");
            bucheron.attackSpe()
            bucheron.resetchargeUltim()
        elif keys[pygame.K_LEFT]:
            bucheron.bougergauche(collide)
        elif keys[pygame.K_RIGHT]:
            bucheron.bougerdroite(collide)
        else:
            bucheron.pasbouger()

        # Exécution de l'attaque Speciale Jutsu
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
                    bucheron.addchargeultim()
                if pygame.Rect(bucheron.gethitboxAttG()).colliderect(mechant2.gethitbox()):
                    mechant2.tuer()
                    mechant2.respawn()
                    bucheron.addchargeultim()

            else:
                if not pygame.Rect(bucheron.gethitboxAttD()).collidelist(arbres) == -1:
                    for j in range(0, len(arbres)):
                        if pygame.Rect(bucheron.gethitboxAttD()).colliderect(arbres[j]):
                            i = j

                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant.gethitbox()):
                    mechant.tuer()
                    mechant.respawn()
                    bucheron.addchargeultim()
                if pygame.Rect(bucheron.gethitboxAttD()).colliderect(mechant2.gethitbox()):
                    mechant2.tuer()
                    mechant2.respawn()
                    bucheron.addchargeultim()
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

            if pygame.Rect(ennemi.gethitbox()).colliderect(missilGravite.gethitbox()):
                ennemi.setemplevitation(200)
                ennemi.setenlevitation(True)

            if ennemi.getenlevitation():
                if ennemi.gety() < -20:
                    ennemi.respawn()
                    ennemi.setenlevitation(False)
                else:
                    ennemi.leviter()
            else:
                ennemi.setvitesse(2)
                ennemi.deplacer()

        majmechant(mechant)
        majmechant(mechant2)

        vue.Update(terrain, bucheron, fenetre, mechant, mechant2, arbres, missilGravite, debutjeu)

        if (pygame.time.get_ticks() // 1000 - debutjeu) == 180:
            finloop()


introloop()
pygame.quit()
