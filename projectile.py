import pygame

class projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 40
        self.hitbox = (self.x, self.y , 0, 0)

    def gethitbox(self):
        return self.hitbox

    def ajouterhitbox(self):
        self.hitbox = (self.x -10, self.y + 10, 150, 160)

    def retirerhitbox(self):
        self.hitbox = (self.x, self.y , 0, 0)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def updhitbox(self):
        self.hitbox = (self.x + 60, self.y + 50, 60, 70)

    def shoot(self, direction):
        if direction == "D":
            print('Shoot Droite')
            self.x += self.vitesse
            self.updhitbox()

        elif direction == "G":
            print('Shoot Gauche')
            self.x -= self.vitesse
            self.updhitbox()