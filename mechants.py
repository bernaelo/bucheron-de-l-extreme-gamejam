import pygame
from pygame.locals import *


class Mechant(object):

    def __init__(self):
        pygame.display.set_caption("Bucheron Vie")
        self.hp = 1
        self.degat = 0
        self.x = 1
        self.y = 550
        self.mort = 0
        self.hitbox=(self.x,self.y,50,50)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def attaqueBucheronDroite(self, fenetre):

        if self.mort == 0:
            ninja = pygame.image.load("Ninja PAUSE ATT0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()

            ninja = pygame.image.load("Ninja PAUSE ATT1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()

    def deplacerDroite(self, fenetre):
        if self.mort == 0:
            # sprite1
            ninja = pygame.image.load("Ninja_Mouvement1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()
            pygame.display.flip()

            # sprite2
            ninja = pygame.image.load("Ninja_Mouvement0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()
            pygame.display.flip()

            self.x += 0.5
            self.updhitbox()

    def attaqueTourDroite(self, fenetre):
        if self.mort == 0:
            # sprite 1
            ninja = pygame.image.load("Ninja MOUV attaque0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))

            pygame.display.update()

            # sprite 2
            ninja = pygame.image.load("Ninja MOUV attaque1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))

            pygame.display.update()

    def recréerDroite(self):
        self.mort = 0
        self.x = 1
        self.y = 550

    def suprimer(self):
        self.mort = 1

    def attaqueBucheronGauche(self, fenetre):

        if self.mort == 0:
            ninja = pygame.image.load("Ninja PAUSE ATT GAUCHE0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()

            ninja = pygame.image.load("Ninja PAUSE ATT GAUCHE1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()

    def deplacerGauche(self, fenetre):
        if self.mort == 0:
            # sprite1
            ninja = pygame.image.load("Ninja MOUV GAUCHE1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()
            pygame.display.flip()

            # sprite2
            ninja = pygame.image.load("Ninja MOUV GAUCHE0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))
            pygame.display.update()
            pygame.display.flip()

            self.x -= 0.5
            self.updhitbox()

    def attaqueTourGauche(self, fenetre):
        if self.mort == 0:
            # sprite 1
            ninja = pygame.image.load("Ninja MOUV ATT GAUCHE0.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))

            pygame.display.update()

            # sprite 2
            ninja = pygame.image.load("Ninja MOUV ATT GAUCHE1.png").convert_alpha()
            fenetre.blit(ninja, (self.x, self.y))

            pygame.display.update()

    def recréerGauche(self):
        self.mort = 0
        self.x = 900
        self.y = 550

    def updhitbox(self):
        self.hitbox = (self.x, self.y, 50, 50)

    def gethitbox(self):
        return self.hitbox