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
        self.nuagefD = [pygame.image.load('NUAGE FIN D.png'), pygame.image.load('NUAGE FIN D2.png')]
        self.nuagefG = [pygame.image.load('NUAGE FIN G.png'), pygame.image.load('NUAGE FIN G2.png')]
        self.nuage = [pygame.image.load('nuage.png'), pygame.image.load('NUAGE mouv2.png')]
        self.terre = pygame.image.load('terre.png')
        self.herbe = pygame.image.load('herbe.png')
        self.arbre = pygame.image.load('Arbre.png')
        self.tour = pygame.image.load('tour23.png')
        self.stopCount =0
        self.walkCount = 0
        self.nuageCount=0
        self.attCount=0


    def Update(self,terrain,bu,fenetre, mechant, mechant2):


        fenetre.blit(pygame.image.load('background.png'),(0,0))

        for i in range(0,len(terrain.getCases())-1):
            for j in range(0,len(terrain.getCases()[i])-1):
                if terrain.getCases()[i][j].getType()==tc.typecase.TERRE:
                    fenetre.blit(self.terre,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.HERBE:
                    fenetre.blit(self.herbe,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.NUAGE:
                    #fenetre.blit(nuage,(j*50,i*50))
                    fenetre.blit(self.nuage[self.nuageCount // 10], (j*50, i*50))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGED:
                    #fenetre.blit(nuagefD, (j * 50, i * 50))
                    fenetre.blit(self.nuagefD[self.nuageCount // 10], (j * 50, i * 50))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGEG:
                    #fenetre.blit(nuagefG,(j*50,i*50))
                    fenetre.blit(self.nuagefG[self.nuageCount // 10], (j * 50, i * 50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.ARBRE:
                    fenetre.blit(self.arbre,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.TOUR:
                    fenetre.blit(self.tour,(j*50,i*50))

        self.nuageCount +=1
        if self.nuageCount>19:
            self.nuageCount=0



        if bu.isAttacking():
            if bu.getoldleft():
                fenetre.blit(self.attaqueGauche[self.attCount ], (bu.getx(), bu.gety()))
            else:
                fenetre.blit(self.attaqueDroite[self.attCount ], (bu.getx(), bu.gety()))

            self.attCount+=1
            if self.attCount>4:
                self.attCount=0
                bu.setAttack(False)

        elif bu.getleft():
            if bu.getisJump():
                fenetre.blit(self.walkLeft[5], (bu.getx(), bu.gety()))
                self.walkCount=0
            else:
                fenetre.blit(self.walkLeft[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount+=1
                if self.walkCount > 11:
                    self.walkCount = 0
        elif bu.getright():
            if bu.getisJump():
                fenetre.blit(self.walkRight[5], (bu.getx(), bu.gety()))
                self.walkCount=0
            else:
                fenetre.blit(self.walkRight[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount+=1
                if self.walkCount > 11:
                    self.walkCount = 0
        else:
            if bu.getoldleft():
                fenetre.blit(self.immobileGauche[self.stopCount//4], (bu.getx(), bu.gety()))
            else:
                fenetre.blit(self.immobileDroite[self.stopCount // 4], (bu.getx(), bu.gety()))
            bu.setright(False)
            bu.setleft(False)
            self.walkCount=0
            self.stopCount += 1
            if self.stopCount>7:
                self.stopCount=0

        pygame.draw.rect(fenetre,(255,0,0),bu.gethitbox(),2)
        pygame.draw.rect(fenetre, (0, 255, 0), bu.gethitboxAttG(), 2)
        pygame.draw.rect(fenetre, (0, 0, 0), bu.gethitboxAttD(), 2)

        if bu.getx() == mechant.getx() and bu.gety() == mechant.gety():
            mechant.attaqueBucheronDroite(fenetre)

        elif mechant.getx() == 500:  # emplacement de la tour
            mechant.attaqueTourDroite(fenetre)
            mechant.suprimer()
            mechant.recréerDroite()

        else:
            mechant.deplacerDroite(fenetre)
        # ninja a gauche
        # if bu.getx() == mechant2.getx() and bu.gety() == mechant2.gety():
        #     mechant2.attaqueBucheronGauche(fenetre)
        #
        # elif mechant2.getx() == 500:  # emplacement de la tour
        #     mechant2.attaqueTourGauche(fenetre)
        #     mechant2.suprimer()
        #     mechant2.recréerGauche()
        #
        # else:
        #     mechant2.deplacerGauche(fenetre)

        pygame.display.flip()

