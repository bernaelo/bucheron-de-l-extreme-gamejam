import pygame
from pygame.locals import *


class Mechant(object):

    def __init__(self, lieuspawn, startx):
        self.hp = 1
        self.degat = 0
        self.vitesse = 0
        self.startx = startx
        self.x = 0
        self.y = 550
        self.mort = False
        self.enlevitation = False
        self.templevitaion = 0
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

    def setemplevitation(self, i):
        self.templevitation = i

    def getemplevitation(self):
        return self.templevitation

    def setenlevitation(self, b):
        self.enlevitation = b

    def getenlevitation(self):
        return self.enlevitation

    def deplacer(self):
        if not self.mort:
            if self.spawn == "G":
                self.x += self.vitesse
            else:
                self.x -= self.vitesse
        self.updhitbox()


    def respawn(self):
        self.mort = False
        self.x = self.startx
        self.y = 550
        self.updhitbox()

    def tuer(self):
        self.mort = True

    def leviter(self):
        self.setvitesse(1.5)
        self.y -= self.vitesse
        self.updhitbox()

    def aterre(self):
        self.enlevitation = False
        self.y += 150
        self.updhitbox()


    def gethitbox(self):
        return self.hitbox

    def updhitbox(self):
        if self.spawn == "G":
            self.hitbox = (self.x, self.y, 40, 50)
        else:
            self.hitbox = (self.x + 10, self.y, 40, 50)