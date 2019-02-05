import pygame

class Bucheron(object):

    def __init__(self):
        self.x=200
        self.y=440
        self.right=False
        self.left=False
        self.speed=13
        self.isJump=False
        self.hitbox=(self.x + 60,self.y+40,40,114)
        self.hitboxAttG = (self.x , self.y + 40, 60, 114)
        self.hitboxAttD = (self.x + 100, self.y + 40, 60, 114)
        self.jumpCount = 9.5
        self.oldleft=False
        self.isAttack=False
        self.traitrise=False


    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def setx(self,x1):
        self.x=x1

    def sety(self, y1):
        self.y = y1

    def setleft(self,b):
        self.left=b

    def setright(self,b):
        self.right=b

    def getspeed(self):
        return self.speed

    def setspeed(self, sp):
        self.speed = sp

    def getisJump(self):
        return self.isJump

    def setisJump(self, iS):
        self.isJump = iS

    def sauter(self,collide):
        if self.isAttack == False:
            test=False
            if self.jumpCount >=0:
                self.y-=(self.jumpCount * abs(self.jumpCount)) * 0.5
                self.updhitbox()
                if not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                    while not pygame.Rect(self.hitbox).collidelist(collide)== -1:
                        self.y += 1
                        self.updhitbox()
                    if self.jumpCount>0:
                        self.jumpCount=0


                self.jumpCount -= 1
            elif self.jumpCount <0:

                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.updhitbox()

                if not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                    while not pygame.Rect(self.hitbox).collidelist(collide)== -1:
                        self.y -= 1
                        self.updhitbox()
                    test=True

                self.jumpCount -= 1

                if test:
                    self.jumpCount = 9.5
                    self.isJump = False

            else:
                self.isJump=False
                self.jumpCount = 9.5
            self.updhitbox()

    def bougerdroite(self,collide):
        if self.isAttack == False:

            self.x += self.speed
            self.updhitbox()
            if not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                while not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                    self.x -= 1
                    self.updhitbox()
            # descendre
            if not self.isJump:
                self.descendre(collide)
            self.updhitbox()

        self.right = True
        self.left = False
        self.oldleft = False
        self.traitrise = False


    def bougergauche(self,collide):
        self.traitrise = True
        if self.isAttack==False:
            self.x -= self.speed
            self.updhitbox()
            if not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                while not pygame.Rect(self.hitbox).collidelist(collide) == -1:
                    self.x += 1
                    self.updhitbox()
            # descendre
            if not self.isJump:
                self.descendre(collide)
            self.updhitbox()

        self.left = True
        self.right = False
        self.oldleft = True
        self.traitrise = False

    def attack(self):
        self.isAttack=True

    def pasbouger(self):
        self.left = False
        self.right = False

    def gethitbox(self):
        return self.hitbox

    def updhitbox(self):
        self.hitbox=(self.x + 60,self.y+40,40,114)
        self.hitboxAttG = (self.x , self.y + 40, 60, 114)
        self.hitboxAttD = (self.x + 100, self.y + 40, 60, 114)

    def gethitboxAttG(self):
        return self.hitboxAttG

    def gethitboxAttD(self):
        return self.hitboxAttD

    def getoldleft(self):
        return self.oldleft

    def descendre(self,collide):
        self.jumpCount=-1
        self.isJump=True
        self.sauter(collide)

    def isAttacking(self):
        return self.isAttack

    def setAttack(self,b):
        self.isAttack = b

    def getTraitrise(self):
        return self.traitrise