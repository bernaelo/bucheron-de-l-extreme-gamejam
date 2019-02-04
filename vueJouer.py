import pygame
import terrain as t

class Terrain(object):

    def __init__(self):
        self.fenetre = pygame.display.set_mode((1600, 800))

    def getWind(self):
        return self.fenetre

