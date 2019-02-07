import pygame
from pygame.locals import *


class Mechant(object):

    def __init__(self, lieuspawn):
        self.hp = 1
        self.degat = 0
        self.vitesse = 5
        self.x = -50
        self.y = 550
        self.mort = False
        self.spawn = lieuspawn
        self.hitbox=(self.x,self.y,50,50)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getspawn(self):
        return self.spawn

    def setvitesse(self, v):
        self.vitesse = v

    def deplacer(self):
        if not self.mort:
            if self.spawn == "G":
                self.x += self.vitesse
            else:
                self.x -= self.vitesse
        self.updhitbox()


    def respawn(self):
        if self.spawn == "G":
            self.mort = False
            self.x = -50
            self.y = 550
        else:
            self.mort = False
            self.x = 1100
            self.y = 550
        self.updhitbox()

    def tuer(self):
        self.mort = True

    def leviter(self):
        self.y += 75

    def aterre(self):
        self.y -= 75


    def gethitbox(self):
        return self.hitbox

    def updhitbox(self):
        if self.spawn == "G":
            self.hitbox = (self.x, self.y, 40, 50)
        else:
            self.hitbox = (self.x + 10, self.y, 40, 50)