class Tour(object):

    def __init__(self):
        self.nbetage = 0
        self.nbbuche = 0
        self.hauteuretage = 100

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
