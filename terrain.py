import tour as t
import case as c
import typecase as tc

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=initcases()
        self.posTour=(850,650)

    def getTour(self):
        return self.tour

    def getCases(self):
        return self.cases

    def getposTour(self):
        return self.posTour

    def getlargeur(self):
        return self.largeur

    def printcases(self):
        for i in range(0,len(self.cases)-1):
            for j in range(0,len(self.cases[i])-1):
                if self.cases[i][j].getType()==tc.typecase.TERRE:
                    print("ta grosse mere")



def initcases():
    cases=[]

    for i in range(0,19):
        ligne=[]
        for j in range(0,33):
            case=c.Case()
            if i >14:
                if cases[i-1][j].getType()==tc.typecase.VIDE:
                    case.setType(tc.typecase.HERBE)
                else:
                    case.setType(tc.typecase.TERRE)
            ligne.append(case)
        cases.append(ligne)
    return cases