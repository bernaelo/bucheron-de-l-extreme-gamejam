import tour as t
import case as c
import typecase as tc
import pygame

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=[]
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
                if i==7 and j in range(3,7):
                    case.setType(tc.typecase.NUAGE)
                    collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i==9 and j in range(10,15):
                    case.setType(tc.typecase.NUAGE)
                    collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i >11:
                    if i>0 and listecases[i-1][j].getType()==tc.typecase.VIDE:
                        case.setType(tc.typecase.HERBE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                    else:
                        case.setType(tc.typecase.TERRE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                ligne.append(case)
            listecases.append(ligne)
        self.cases=listecases
        return collision


