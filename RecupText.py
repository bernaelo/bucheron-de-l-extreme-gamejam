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
    name = "Veuillez écrire votre nom: "
    name2 = ""
    font = pygame.font.Font(None, 50)
    pasfin = True
    while pasfin:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    pasfin = False
                    return name2

                elif evt.unicode.isalpha():
                    name += evt.unicode
                    name2 += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                    name2 = name[:-1]

        screen.blit(pygame.image.load('background.png'), (0, 0))

        block = font.render("Partie terminé merci d'avoir jouer. ", True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = (500, 100)
        screen.blit(block, rect)
        pygame.display.flip()

        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()


if __name__ == "__main__":
    name()