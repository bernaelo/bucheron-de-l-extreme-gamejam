import tour as t
import case as c
import typecase as tc

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

    for i in range(1,514):
        case=c.Case()
        if i >416:
            if cases[i-33].getType()==tc.typecase.VIDE:
                case.setType(tc.typecase.HERBE)
            else:
                case.setType(tc.typecase.TERRE)
        cases.append(case)

    return cases