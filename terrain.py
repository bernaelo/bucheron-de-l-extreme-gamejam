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
        for i in range(0,26):
            ligne=[]
            for j in range(0,35):
                case=c.Case()

                #ARBRES
                if i==2 and j==1:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==9 and j==0:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==10 and j==10:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==0 and j==12:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==6 and j==11:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==15 and j==1:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==18 and j==8:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))



                if i==2 and j==20:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==1 and j==31:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==6 and j==28:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==10 and j==21:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==12 and j==27:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))

                if i==18 and j==31:
                    case.setType(tc.typecase.ARBRE)
                    suede.append(pygame.Rect(j * 30 + 5, i * 30 - 10, 45, 68))
                    posiArbres.append((j,i))





                #tour
                if i==19 and j==15:
                    case.setType(tc.typecase.TOUR)

                #plateformes
                if i==4 and j in range(0,3):
                    if j==0:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==2:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==3 and j in range(7,10):
                    if j==7:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==9:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==2 and j in range(11,14):
                    if j==11:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==13:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==8 and j in range(6,13):
                    if j==6:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==12:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==11 and j in range(0,4):
                    if j==0:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==3:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==12 and j in range(9,13):
                    if j==9:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==12:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==15 and j in range(6,9):
                    if j==6:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==8:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==17 and j in range(0,3):
                    if j==0:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==2:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==4 and j in range(19,23):
                    if j==19:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==22:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==3 and j in range(29,35):
                    if j==29:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==34:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==6 and j in range(23,26):
                    if j==23:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==25:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==8 and j in range(26,31):
                    if j==26:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==30:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==12 and j in range(20,23):
                    if j==20:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==22:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==14 and j in range(26,30):
                    if j==26:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==29:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i==17 and j in range(21,25):
                    if j==17:
                        case.setType(tc.typecase.NUAGEG)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    elif j==24:
                        case.setType(tc.typecase.NUAGED)
                        collision.append(pygame.Rect(j * 30, i * 30, 30, 30))
                    else:
                        case.setType(tc.typecase.NUAGE)
                        collision.append(pygame.Rect(j * 30, i * 30,30,30))



                #sol
                if i==20:
                    case.setType(tc.typecase.HERBE)
                    collision.append(pygame.Rect(j * 30, i * 30,30,30))
                if i >20:
                    case.setType(tc.typecase.TERRE)
                    collision.append(pygame.Rect(j * 30, i * 30,30,30))

                if i == 19 and j == 31:
                    case.setType(tc.typecase.RESSORT)
                    boing.append(pygame.Rect(j * 30, i * 30, 30, 30))
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