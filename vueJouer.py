import pygame
import typecase as tc

class Vue(object):

    def __init__(self):
        self.fenetre = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
        pygame.display.set_caption("Bucheron Vie")
        self.walkLeft = [pygame.image.load('Bucheron-Run-Left0.png'), pygame.image.load('Bucheron-Run-Left1.png'), pygame.image.load('Bucheron-Run-Left2.png'), pygame.image.load('Bucheron-Run-Left3.png'), pygame.image.load('Bucheron-Run-Left4.png'),pygame.image.load('Bucheron-Run-Left5.png')]
        self.walkRight = [pygame.image.load('Bucheron-Run-Right0.png'), pygame.image.load('Bucheron-Run-Right1.png'), pygame.image.load('Bucheron-Run-Right2.png'), pygame.image.load('Bucheron-Run-Right3.png'), pygame.image.load('Bucheron-Run-Right4.png'),pygame.image.load('Bucheron-Run-Right5.png')]
        self.immobile = [pygame.image.load('Bucheron-Stop-Right0.png'), pygame.image.load('Bucheron-Stop-Right1.png')]
        self.stopCount =0

    def getFenetre(self):
        return self.fenetre

    def Update(self,terrain,bu):
        terre = pygame.image.load('terre.png')
        herbe = pygame.image.load('herbe.png')
        bg = pygame.image.load('background.jpg')

        self.fenetre.blit(bg,(0,0))

        for i in range(0,len(terrain.getCases())-1):
            for j in range(0,len(terrain.getCases()[i])-1):
                if terrain.getCases()[i][j].getType()==tc.typecase.TERRE:
                    self.fenetre.blit(terre,(j*50,i*50))
                elif terrain.getCases()[i][j].getType()==tc.typecase.HERBE:
                    self.fenetre.blit(herbe,(j*50,i*50))

        if bu.getwalkCount() >= 12:
            bu.reswalkCount()

        if bu.getleft():
            if bu.getisJump():
                self.fenetre.blit(self.walkLeft[5], (bu.getx(), bu.gety()))
                bu.reswalkCount()
            else:
                self.fenetre.blit(self.walkLeft[bu.getwalkCount() // 2], (bu.getx(), bu.gety()))
                bu.incrwalkCount()
        elif bu.getright():
            if bu.getisJump():
                self.fenetre.blit(self.walkRight[5], (bu.getx(), bu.gety()))
                bu.reswalkCount()
            else:
                self.fenetre.blit(self.walkRight[bu.getwalkCount() // 2], (bu.getx(), bu.gety()))
                bu.incrwalkCount()
        else:
            self.fenetre.blit(self.immobile[self.stopCount//4], (bu.getx(), bu.gety()))
            bu.setright(False)
            bu.setleft(False)
            bu.reswalkCount()
            self.stopCount += 1
            if self.stopCount>7:
                self.stopCount=0

        pygame.display.flip()

