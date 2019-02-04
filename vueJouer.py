import pygame
import typecase.typecase as tc

class Vue(object):

    def __init__(self):
        self.fenetre = pygame.display.set_mode((1600, 800))

    def getFenetre(self):
        return self.fenetre

    def Update(self,terrain):
        terre = pygame.image.load('terre.png')

        for i in range(0,len(terrain.getCases())-1):
            if terrain.getCases()[i].getType()==tc.TERRE:
                self.fenetre.blit(terre,)

