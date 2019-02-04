import pygame
import typecase as tc

class Vue(object):

    def __init__(self):
        self.fenetre = pygame.display.set_mode((1600, 800))
        pygame.display.set_caption("Bucheron Vie")

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

