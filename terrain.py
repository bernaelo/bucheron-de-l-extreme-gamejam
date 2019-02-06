import tour as t
import case as c
import typecase as tc
import pygame

class Terrain(object):

    def __init__(self):
        self.tour=t.Tour()
        self.cases=[]
        self.collide=[]
        self.arbres=[]
        self.posArbres=[]
        self.ressorts=[]


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
        boing=[]
        suede=[]
        posiArbres=[]
        for i in range(0,15):
            ligne=[]
            for j in range(0,21):
                case=c.Case()

                if i==6 and j==5:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 50, i * 50-28, 50, 78))
                    posiArbres.append((j,i))

                if i==8 and j==14:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 50, i * 50-28, 50, 78))
                    posiArbres.append((j,i))

                if i==11 and j==7:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 50, i * 50-28, 50, 78))
                    posiArbres.append((j,i))

                if i==5 and j==9:
                    case.setType(tc.typecase.TOUR)

                if i==7 and j in range(4,8):
                    if j==4:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    elif j==7:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i==9 and j in range(13,16):
                    if j == 13:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    elif j == 15:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                if i==9 and j in range(0,2):
                    if j == 0:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                    elif j == 1:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 50, i * 50, 50, 50))
                if i==12:
                    case.setType(tc.typecase.HERBE)
                    collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i >12:
                    case.setType(tc.typecase.TERRE)
                    collision.append(pygame.Rect(j * 50, i * 50,50,50))
                if i == 11 and j == 16:
                    case.setType(tc.typecase.RESSORT)
                    boing.append(pygame.Rect(j * 50, i * 50, 50, 50))
                ligne.append(case)
            listecases.append(ligne)

        collision.append((-5,0,5,700))
        collision.append((1000, 0, 5, 700))

        self.cases=listecases
        self.collide=collision
        self.ressorts=boing
        self.arbres=suede
        self.posArbres=posiArbres

    def getCollide(self):
        return self.collide

    def getArbres(self):
        return self.arbres

    def getPosArbres(self):
        return self.posArbres

    def getRessorts(self):
        return self.ressorts


