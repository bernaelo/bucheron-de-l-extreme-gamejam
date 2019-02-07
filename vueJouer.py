import pygame
import typecase as tc


class Vue(object):

    def __init__(self):
        pygame.display.set_caption("Bucheron Vie")
        self.walkLeft = [pygame.image.load('Bucheron-Run-Left0.png'), pygame.image.load('Bucheron-Run-Left1.png'), pygame.image.load('Bucheron-Run-Left2.png'), pygame.image.load('Bucheron-Run-Left3.png'), pygame.image.load('Bucheron-Run-Left4.png'),pygame.image.load('Bucheron-Run-Left5.png')]
        self.walkRight = [pygame.image.load('Bucheron-Run-Right0.png'), pygame.image.load('Bucheron-Run-Right1.png'), pygame.image.load('Bucheron-Run-Right2.png'), pygame.image.load('Bucheron-Run-Right3.png'), pygame.image.load('Bucheron-Run-Right4.png'),pygame.image.load('Bucheron-Run-Right5.png')]
        self.immobileDroite = [pygame.image.load('Bucheron-Stop-Right0.png'), pygame.image.load('Bucheron-Stop-Right1.png')]
        self.immobileGauche = [pygame.image.load('Bucheron-Stop-Left0.png'), pygame.image.load('Bucheron-Stop-Left1.png')]
        self.attaqueDroite = [pygame.image.load('att D0.png'), pygame.image.load('att D1.png'), pygame.image.load('att D2.png'), pygame.image.load('att D3.png'), pygame.image.load('att D4.png')]
        self.attaqueGauche = [pygame.image.load('att G0.png'), pygame.image.load('att G1.png'), pygame.image.load('att G2.png'), pygame.image.load('att G3.png'), pygame.image.load('att G4.png')]
        self.attaqueSpeDroite = [pygame.image.load('attSpe D0.png'), pygame.image.load('attSpe D1.png'), pygame.image.load('attSpe D2.png'), pygame.image.load('attSpe D3.png'), pygame.image.load('attSpe D4.png')]
        self.attaqueSpeGauche = [pygame.image.load('attSpe G0.png'), pygame.image.load('attSpe G1.png'), pygame.image.load('attSpe G2.png'), pygame.image.load('attSpe G3.png'), pygame.image.load('attSpe G4.png')]
        self.vagueAntigravDroite = [pygame.image.load('vagueAntigrav D.png')]
        self.vagueAntigravGauche = [pygame.image.load('vagueAntigrav G.png')]
        self.nuagefD = [pygame.image.load('NUAGE FIN D.png'), pygame.image.load('NUAGE FIN D2.png')]
        self.nuagefG = [pygame.image.load('NUAGE FIN G.png'), pygame.image.load('NUAGE FIN G2.png')]
        self.nuage = [pygame.image.load('nuage0.png'), pygame.image.load('nuage1.png')]
        self.ninjaDepGauche = [pygame.image.load('Ninja MOUV G0.png'), pygame.image.load('Ninja MOUV G1.png')]
        self.ninjaDepDroite = [pygame.image.load('Ninja MOUV D0.png'), pygame.image.load('Ninja MOUV D1.png')]
        self.ninjaAttGauche = [pygame.image.load('Ninja ATT G0.png'), pygame.image.load('Ninja ATT G1.png')]
        self.ninjaAttDroite = [pygame.image.load('Ninja ATT D0.png'), pygame.image.load('Ninja ATT D1.png')]
        self.ninjaDeces = [pygame.image.load('Ninja MORT.png')]
        self.terre = pygame.image.load('Terre.png')
        self.herbe = pygame.image.load('Terre + Herbe.png')
        self.arbre = pygame.image.load('arbre.png')
        self.arbrecoupe = pygame.image.load('arbre_coupé.png')
        self.ressort = [pygame.image.load('Ressort0.png'), pygame.image.load('Ressort1.png'), pygame.image.load('Ressort2.png')]
        self.levitation = [pygame.image.load('Antigravite0.png'), pygame.image.load('Antigravite1.png'), pygame.image.load('Antigravite2.png'), pygame.image.load('Antigravite3.png'), pygame.image.load('Antigravite4.png'), pygame.image.load('Antigravite5.png')]
        self.stopCount = 0
        self.walkCount = 0
        self.walkNinjaCount = 0
        self.levitCount = 0
        self.ressortCount = 0
        self.nuageCount=0
        self.attCount=0
        self.attSpeCount = 0
        self.vagueAntigravActive = False
        self.vagueAntigravDirect = ""
        self.font = pygame.font.Font(None, 40)
        self.temps = pygame.time.Clock()
        self.demarrer = 0
        self.old_charge = 0

        def getdemarrer(self):
            return self.demarrer

        def setdemarrer(self, demarrer):
            self.demarrer = demarrer


    def Update(self, terrain, bu, fenetre, lesmechants, arbres, missil,temps):

        fenetre.blit(pygame.image.load('background.png'), (0, 0))

        for i in range(0, len(terrain.getCases()) - 1):
            for j in range(0, len(terrain.getCases()[i]) - 1):
                if terrain.getCases()[i][j].getType() == tc.typecase.TOUR:
                    for k in range(0, terrain.getTour().getnbbuche()):
                        fenetre.blit(pygame.image.load('Bûche.png'),(j * 30 + 26 * (k % 5), i * 30 - 20 - 50 * (k // 5)))
                elif terrain.getCases()[i][j].getType() == tc.typecase.ARBRE:
                    fenetre.blit(self.arbre, (j * 30 -20, i * 30 - 48))
                elif terrain.getCases()[i][j].getType() == tc.typecase.ARBRECOUPE:
                    fenetre.blit(self.arbrecoupe, (j * 30 - 10, i * 30 - 28))
                elif terrain.getCases()[i][j].getType() == tc.typecase.RESSORT:
                    fenetre.blit(self.ressort[self.ressortCount // 20], (j * 30, i * 30))
                elif terrain.getCases()[i][j].getType() == tc.typecase.TERRE:
                    fenetre.blit(self.terre, (j * 30, i * 30))
                elif terrain.getCases()[i][j].getType() == tc.typecase.HERBE:
                    fenetre.blit(self.herbe, (j * 30, i * 30))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGE:
                    fenetre.blit(self.nuage[self.nuageCount // 10], (j * 30, i * 30))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGED:
                    fenetre.blit(self.nuagefD[self.nuageCount // 10], (j * 30, i * 30))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGEG:
                    fenetre.blit(self.nuagefG[self.nuageCount // 10], (j * 30, i * 30))

        self.nuageCount += 1
        if self.nuageCount > 19:
            self.nuageCount = 0

        self.ressortCount += 1
        if self.ressortCount > 39:
            self.ressortCount = 0

        if self.walkCount >= 12:
            self.walkCount = 0

        self.walkNinjaCount += 1
        if self.walkNinjaCount > 19:
            self.walkNinjaCount = 0

        self.levitCount += 1
        if self.levitCount > 49:
            self.levitCount = 0

        def runninja(ennemi, runCount, levitCount):
            if ennemi.getspawn() == "G":
                fenetre.blit(self.ninjaDepGauche[runCount // 10], (ennemi.getx(), ennemi.gety()))
            else:
                fenetre.blit(self.ninjaDepDroite[runCount// 10], (ennemi.getx(), ennemi.gety()))

            if ennemi.getenlevitation():
                fenetre.blit(self.levitation[levitCount //10], (ennemi.getx(), ennemi.gety() + 50))

        for m in lesmechants:
            runninja(m, self.walkNinjaCount, self.levitCount)


        if bu.isAttackingSpe():
            if bu.getoldleft():
                fenetre.blit(self.attaqueSpeGauche[self.attSpeCount], (bu.getx(), bu.gety()))
                self.vagueAntigravDirect = "G"
            else:
                fenetre.blit(self.attaqueSpeDroite[self.attSpeCount], (bu.getx(), bu.gety()))
                self.vagueAntigravDirect = "D"

            self.attSpeCount += 1
            if self.attSpeCount == 3:
                bu.attackSpe()
                self.vagueAntigravActive = True
            if self.attSpeCount == 4:
                self.attSpeCount=0
                bu.setAttackSpe(False)

        elif bu.isAttacking():
            if bu.getoldleft():
                fenetre.blit(self.attaqueGauche[self.attCount], (bu.getx(), bu.gety()))
            else:
                fenetre.blit(self.attaqueDroite[self.attCount], (bu.getx(), bu.gety()))

            self.attCount += 1
            if self.attCount == 3:
                bu.setCoupHache(True)
            elif self.attCount == 4:
                bu.setCoupHache(False)
            if self.attCount > 4:
                self.attCount = 0
                bu.setAttack(False)

        elif bu.getleft():
            if bu.getisJump() and not bu.getTraitrise():
                fenetre.blit(self.walkLeft[5], (bu.getx(), bu.gety()))
                self.walkCount = 0
            else:
                fenetre.blit(self.walkLeft[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount += 1
                if self.walkCount >= 12:
                    self.walkCount = 0
        elif bu.getright():
            if bu.getisJump() and not bu.getTraitrise():
                fenetre.blit(self.walkRight[5], (bu.getx(), bu.gety()))
                self.walkCount = 0
            else:
                fenetre.blit(self.walkRight[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount += 1
                if self.walkCount > 11:
                    self.walkCount = 0
        else:
            if bu.getoldleft():
                fenetre.blit(self.immobileGauche[self.stopCount // 10], (bu.getx(), bu.gety()))
            else:
                fenetre.blit(self.immobileDroite[self.stopCount // 10], (bu.getx(), bu.gety()))
            bu.setright(False)
            bu.setleft(False)
            self.stopCount += 1
            if self.stopCount > 19:
                self.stopCount = 0

        if self.vagueAntigravActive:
            if self.vagueAntigravDirect == "G":
                fenetre.blit(self.vagueAntigravGauche[0], (missil.getx(), missil.gety()))
            else:
                fenetre.blit(self.vagueAntigravDroite[0], (missil.getx(), missil.gety()))
            #Distance maximum sur l'axe X de la vague Antigravité
            if missil.getx() < -100 or missil.getx() > 1000:
                self.vagueAntigravActive = False


        pygame.draw.rect(fenetre, (255, 0, 0), bu.gethitbox(), 2)
        pygame.draw.rect(fenetre, (0, 255, 0), bu.gethitboxAttG(), 2)
        pygame.draw.rect(fenetre, (0, 0, 0), bu.gethitboxAttD(), 2)

        pygame.draw.rect(fenetre, (0, 0, 255), terrain.getTour().gethitbox(), 2)

        for m in lesmechants:
            pygame.draw.rect(fenetre, (255, 0, 0), m.gethitbox(), 2)

        pygame.draw.rect(fenetre, (255, 0, 0), missil.gethitbox(), 2)

        if len(arbres) > 0:
            i = 0
            while i < len(arbres):
                pygame.draw.rect(fenetre, (255, 0, 0), arbres[i], 2)
                i += 1

        if bu.getbucheportee() < 2:
            text = self.font.render("Buches : " + str(bu.getbucheportee()), 1, (255, 255, 255))
        else:
            text = self.font.render("Buches : " + str(bu.getbucheportee()), 1, (255, 0, 0))
        fenetre.blit(text, (10, 670))

        #infoUltim = self.font.render("Capacité : " + str(bu.getchargeUltim()) + "/8", 1, (255, 255, 255))
        #fenetre.blit(infoUltim, (550, 640))

        #------ LA BORDEL DE JAUGE !!!! -------
        x_jauge = 730
        y_jauge = 640
        larg_jauge = 200
        bord_jauge = 4
        cran_jauge = larg_jauge / 8
        pygame.draw.rect(fenetre, (174, 166, 183), (x_jauge - (bord_jauge / 2), y_jauge, larg_jauge + bord_jauge, cran_jauge + (bord_jauge / 2)), 0)
        if bu.getchargeUltim() == 8:
            pygame.draw.rect(fenetre, (250, 250, 250), (x_jauge - (bord_jauge / 2), y_jauge, larg_jauge + bord_jauge, cran_jauge + (bord_jauge / 2)), bord_jauge)
            pygame.draw.rect(fenetre, (250, 250, 250), (940, 628, 45, 45), 3)
        else:
            pygame.draw.rect(fenetre, (0, 0, 0), (x_jauge - (bord_jauge/2), y_jauge, larg_jauge + bord_jauge, cran_jauge +(bord_jauge/2)), bord_jauge)
            pygame.draw.rect(fenetre, (0, 0, 0), (940, 628, 45, 45), 3)

        if bu.getchargeUltim() > 0:
            pygame.draw.rect(fenetre, (145, 80 - 10 * (bu.getchargeUltim() - 1), 191),((x_jauge + larg_jauge - (bu.getchargeUltim() * 25)), y_jauge + bord_jauge - 1, (cran_jauge + ((bu.getchargeUltim()-1) * 25)), cran_jauge - bord_jauge + 1), 0)
            #image du spell
        iconUlt = pygame.image.load('icon_ultim.png')
        fenetre.blit(iconUlt, (940, 630))

        #----- ET ELLE FONCTIONNE ! ----------------

        # horloge
        if (pygame.time.get_ticks() // 1000 - temps) >170:
            couleur=(255, 0, 0)
        elif (pygame.time.get_ticks() // 1000 - temps) >150:
            couleur = (204, 85, 0)
        else:
            couleur = (255, 255, 255)

        if (pygame.time.get_ticks() // 1000 - temps)%60 < 10:
            temps = self.font.render("Temps : 0" + str((pygame.time.get_ticks() // 1000 - temps) //60) +":0"+str((pygame.time.get_ticks() // 1000 - temps )%60), 1, couleur)
        else:
            temps = self.font.render("Temps : 0" + str((pygame.time.get_ticks() // 1000 - temps )// 60) + ":" + str((pygame.time.get_ticks() // 1000 - temps )% 60), 1, couleur)
        fenetre.blit(temps, (800, 5))

        pygame.display.flip()
