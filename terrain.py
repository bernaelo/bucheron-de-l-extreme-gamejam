import tour as t
import case as c
import typecase.typecase as tc

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=initcases()
        self.posTour=(850,650)
        self.largeur=32

    def getTour(self):
        return self.tour

    def getCases(self):
        return self.cases

    def getposTour(self):
        return self.posTour

    def getlargeur(self):
        return self.largeur




def initcases():
    cases=[]

    for i in range(1,512):
        case=c.Case()
        if i%32==0 or i%32 == 1 or i >448:
            case.setType(tc.TERRE)
        cases.append(case)

    return cases