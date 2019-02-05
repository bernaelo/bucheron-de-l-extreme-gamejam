class Bucheron(object):

    def __init__(self):
        self.x=500
        self.y=400
        self.right=False
        self.left=False
        self.speed=13
        self.walkCount = 0
        self.isJump=False
        self.hitbox=(self.x + 40,self.y+40,80,114)
        self.jumpCount = 10


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

    def getwalkCount(self):
        return self.walkCount

    def incrwalkCount(self):
        self.walkCount += 1

    def reswalkCount(self):
        self.walkCount = 0

    def getisJump(self):
        return self.isJump

    def setisJump(self, iS):
        self.isJump = iS

    def sauter(self):
        if self.jumpCount >= -10:
            self.y=(self.y-(self.jumpCount * abs(self.jumpCount)) * 0.5)
            self.jumpCount -= 1
        else:
            self.isJump=False
            self.jumpCount = 10
        self.updhitbox()

    def bougerdroite(self):
        self.x += self.speed
        self.right = True
        self.left = False
        self.updhitbox()

    def bougergauche(self):
        self.x -= self.speed
        self.left = True
        self.right = False
        self.updhitbox()

    def pasbouger(self):
        self.walkCount = 0
        self.left = False
        self.right = False

    def gethitbox(self):
        return self.hitbox

    def updhitbox(self):
        self.hitbox=(self.x + 40,self.y+40,80,114)