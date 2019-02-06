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
    screen = pygame.display.set_mode((600, 300))
    name = "Veuillez écrire votre Nom : "
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
            elif evt.type == QUIT:
                return
        screen.fill((0, 0, 0))

        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()


if __name__ == "__main__":
    name()