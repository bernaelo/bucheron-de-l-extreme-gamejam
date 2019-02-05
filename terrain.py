import tour as t
import case as c
import typecase as tc

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=self.initcases()
        self.posTour=(850,650)

    def getTour(self):
        return self.tour

    def getCases(self):
        return self.cases

    def getposTour(self):
        return self.posTour

    def getlargeur(self):
        return self.largeur



    def initcases(self):
        listecases=[]
        collision=[]
        for i in range(0,15):
            ligne=[]
            for j in range(0,21):
                case=c.Case()
                if i==8 and j in range(13,18):
                    case.setType(tc.typecase.NUAGE)
                if i >10:
                    if i>0 and listecases[i-1][j].getType()==tc.typecase.VIDE:
                        case.setType(tc.typecase.HERBE)
                    else:
                        case.setType(tc.typecase.TERRE)
                ligne.append(case)
            listecases.append(ligne)
        return listecases


