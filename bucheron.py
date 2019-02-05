class Bucheron(object):

    def __init__(self):
        self.x=500
        self.y=596
        self.right=False
        self.left=False
        self.speed=13
        self.walkCount = 0
        self.isJump=False


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

    def bougerdroite(self):
        self.x += self.speed
        self.right = True
        self.left = False

    def bougergauche(self):
        self.x -= self.speed
        self.left = True
        self.right = False

    def pasbouger(self):
        self.walkCount = 0
        self.left = False
        self.right = False