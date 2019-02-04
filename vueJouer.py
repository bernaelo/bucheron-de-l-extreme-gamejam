import pygame
import typecase as tc

class Vue(object):

    def __init__(self):
        self.fenetre = pygame.display.set_mode((1600, 800))
        pygame.display.set_caption("Bucheron Vie")
        self.walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png')]
        self.walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png')]


    def getFenetre(self):
        return self.fenetre

    def Update(self,terrain):
        terre = pygame.image.load('terre.png')
        herbe = pygame.image.load('herbe.png')

        for i in range(0,len(terrain.getCases())-1):
            if terrain.getCases()[i].getType()==tc.typecase.TERRE:
                self.fenetre.blit(terre,(i%terrain.getlargeur()*50,i//terrain.getlargeur()*50))
            elif terrain.getCases()[i].getType()==tc.typecase.HERBE:
                self.fenetre.blit(herbe,(i%terrain.getlargeur()*50,i//terrain.getlargeur()*50))

