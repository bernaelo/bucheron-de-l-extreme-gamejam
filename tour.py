class Tour(object):

    def __init__(self):
        self.nbetage = 0
        self.nbbuche = 0
        self.hauteuretage = 100
        self.x=500
        self.y=600
        self.hitbox = (self.x-52, self.y-250,122,250)

    def gethauteuretage(self):
        return self.hauteuretage

    def getnbEtage(self):
        return self.nbetage

    def getnbbuche(self):
        return self.nbbuche

    def setnbetage(self, e):
        self.nbetage = e

    def setnbbuche(self, b):
        self.nbbuche = b

    def gethitbox(self):
        return self.hitbox

    def augnbbuche(self, nb):
        self.nbbuche += nb
        if self.nbbuche//4 > self.nbetage:
            self.nbetage += 1

