import typecase as t


class Case(object):

    def __init__(self):
        self.type = t.typecase.VIDE

    def getType(self):
        return self.type

    def setType(self, t):
        self.type  =  t

