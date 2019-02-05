import pygame
from pygame.locals import *


class Mechant(object):

    def __init__(self):
        pygame.display.set_caption("Bucheron Vie")
        self.hp = 1
        self.degat = 0
        self.quitter = False
        self.mouvement = 0

    def Creer(self, x, y, fenetre):

        while x <= 350 and self.quitter == False:
            # si part de la gauche
            # sprite 1
            for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
                if event.type == KEYDOWN:  # Si un de ces événements est de type QUIT
                    self.quitter = True  # On arrête la boucle
            if self.mouvement == 1:
                fond = pygame.image.load("background.jpg").convert()
                fenetre.blit(fond, (0, 0))
                ninja = pygame.image.load("Ninja_Mouvement1.png").convert_alpha()
                fenetre.blit(ninja, (x, y))
                pygame.display.update()
                pygame.time.delay(100)
                self.mouvement = 0
                # sprite2
            elif self.mouvement == 0:
                fond = pygame.image.load("background.jpg").convert()
                fenetre.blit(fond, (0, 0))
                ninja = pygame.image.load("Ninja_Mouvement0.png").convert_alpha()
                fenetre.blit(ninja, (x, y))
                pygame.display.update()
                pygame.time.delay(100)
                self.mouvement = 1

            x += 3

            print(x)
            if x >= 350:
                # sprite 1
                fond = pygame.image.load("background.jpg").convert()
                fenetre.blit(fond, (0, 0))
                ninja = pygame.image.load("Ninja MOUV attaque0.png").convert_alpha()
                fenetre.blit(ninja, (x, y))

                pygame.display.update()
                pygame.time.delay(100)

                # sprite 2
                fond = pygame.image.load("background.jpg").convert()
                fenetre.blit(fond, (0, 0))
                ninja = pygame.image.load("Ninja MOUV attaque1.png").convert_alpha()
                fenetre.blit(ninja, (x, y))

                pygame.display.update()
                pygame.time.delay(250)

                # sprite 3
                fond = pygame.image.load("background.jpg").convert()
                fenetre.blit(fond, (0, 0))
                ninja = pygame.image.load("Ninja MOUV attaque0.png").convert_alpha()
                fenetre.blit(ninja, (x, y))

                pygame.display.update()
                pygame.time.delay(300)

            # si part de la droite
            if y == 100:
                # x = taille de la map (512)
                x = 512
                x = x - 1
                # sprite 1

                #
                pygame.display.update()
                pygame.time.delay(100)
                # sprite2

                #
                pygame.display.update()
                pygame.time.delay(100)

        pygame.display.flip()
