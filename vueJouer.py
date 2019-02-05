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
        self.stopCount =0
        self.walkCount = 0


    def Update(self,terrain,bu,fenetre):
        terre = pygame.image.load('terre.png')
        herbe = pygame.image.load('herbe.png')
        nuagefD = pygame.image.load('NUAGE FIN D.png')
        nuagefG = pygame.image.load('NUAGE FIN G.png')
        nuage = pygame.image.load('nuage.png')
        fenetre.blit(pygame.image.load('background.png'),(0,0))

        for i in range(0,len(terrain.getCases())-1):
            for j in range(0,len(terrain.getCases()[i])-1):
                if terrain.getCases()[i][j].getType()==tc.typecase.TERRE:
                    fenetre.blit(terre,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.HERBE:
                    fenetre.blit(herbe,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.NUAGE:
                    fenetre.blit(nuage,(j*50,i*50))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGED:
                    fenetre.blit(nuagefD, (j * 50, i * 50))
                elif terrain.getCases()[i][j].getType() == tc.typecase.NUAGEG:
                    fenetre.blit(nuagefG,(j*50,i*50))


        if self.walkCount >= 12:
            self.walkCount=0

        if bu.getleft():
            if bu.getisJump():
                fenetre.blit(self.walkLeft[5], (bu.getx(), bu.gety()))
                self.walkCount=0
            else:
                fenetre.blit(self.walkLeft[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount+=1
        elif bu.getright():
            if bu.getisJump():
                fenetre.blit(self.walkRight[5], (bu.getx(), bu.gety()))
                self.walkCount=0
            else:
                fenetre.blit(self.walkRight[self.walkCount // 2], (bu.getx(), bu.gety()))
                self.walkCount+=1
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

        pygame.display.flip()

