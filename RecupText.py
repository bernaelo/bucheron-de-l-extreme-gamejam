# Display keyboard input using pygame.  Only prints letters (no numbers
# or special chars).  Backspace deletes one character.  Return clears
# the entire input.
#
# Run with the following command:
#   python pygame-display-input.py

import pygame
from pygame.locals import *

def name(screen):
    pygame.init()
    name = ""
    font = pygame.font.Font(None, 50)
    pasfin = True
    compteur = 0

    while pasfin:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    pasfin = False
                    return name

                elif evt.unicode.isalpha():
                    if compteur < 10:
                        name += evt.unicode
                        compteur += 1

                elif evt.key == K_BACKSPACE:
                    if len(name) > 0:
                        name = name[:-1]
                        compteur -= 1

        screen.blit(pygame.image.load('background.png'), (0, 0))

        block = font.render("Partie terminé merci d'avoir jouer. ", True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = (500, 100)
        screen.blit(block, rect)
        pygame.display.flip()

        block2 = font.render("Veuillez écrire votre nom: ", True, (255, 255, 255))
        rect2 = block2.get_rect()
        rect2.center = (400, 350)
        screen.blit(block2, rect2)
        pygame.display.flip()

        block3 = font.render(name, True, (255, 255, 255))
        rect3 = block3.get_rect()
        rect3.center = (700, 350)
        screen.blit(block3, rect3)
        pygame.display.flip()


if __name__ == "__main__":
    name()