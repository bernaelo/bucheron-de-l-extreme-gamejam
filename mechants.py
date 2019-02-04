import pygame
from pygame.locals import *

pygame.init()

hp = 1
degat = 0
y = 430
x = 0

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

while x != 350:
    # si part de la gauche
    # sprite 1
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0, 0))
    ninja = pygame.image.load("Ninja_Mouvement1.png").convert_alpha()
    fenetre.blit(ninja, (x, y))
    #
    pygame.display.update()
    pygame.time.delay(100)
    x = x + 50
    # sprite2
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0, 0))
    ninja = pygame.image.load("Ninja_Mouvement0.png").convert_alpha()
    fenetre.blit(ninja, (x, y))
    #
    pygame.display.update()
    pygame.time.delay(250)

    # sprite3
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0, 0))
    ninja = pygame.image.load("Ninja_Mouvement1.png").convert_alpha()
    fenetre.blit(ninja, (x, y))
    #
    pygame.display.update()
    pygame.time.delay(300)

    # si part de la droite
    print(x)
    if x == 350:
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

continuer = 1

# Boucle infinie
while continuer:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle
