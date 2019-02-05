import tour as t
import case as c
import typecase as tc
import pygame

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=[]
        self.posTour=(850,650)
        self.collide=[]
        self.arbres=[]


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
        suede=[]
        for i in range(0,15):
            ligne=[]
            for j in range(0,21):
                case=c.Case()
                if i==6 and j==5:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 50, i * 50, 50, 50))

                if i==11 and j==7:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 50, i * 50, 50, 50))

                if i==7 and j in range(3,7):
                    if j==3:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    elif j==6:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i==9 and j in range(10,15):
                    if j == 10:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    elif j == 14:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                if i >11:
                    if i>0 and listecases[i-1][j].getType()==tc.typecase.VIDE:
                        case.setType(tc.typecase.HERBE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                    else:
                        case.setType(tc.typecase.TERRE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i == 11 and j == 16:
                    case.setType(tc.typecase.RESSORT)
                    collision.append(pygame.Rect(j * 50, i * 50,50,50))
                ligne.append(case)
            listecases.append(ligne)
        self.cases=listecases
        self.collide=collision

    def getCollide(self):
        return self.collide


