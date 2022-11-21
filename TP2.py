import random

def swap(a,b):
    return b,a

def Age():
    a=int(input("quel age avez vous ? : "))
    print("Vous avez", (2022-a))

def Fondue():
    Base=4
    fromage=800.0
    eau=2
    ail=2
    pain=400
    text="Pour faire une fondue fribourgeoise pour {} personnes, il vous faut : \n- {} gr de fromage \n- {} dl d'eau \n- {} gousse(s) d'ail \n- {} gr de pain"
    nbconvives=int(input("Combien etes vous ? :"))
    print(text.format(nbconvives,fromage*nbconvives/Base, eau*nbconvives/Base, ail*nbconvives/Base, pain*nbconvives/Base))


def tp2exo5():
    n=int(input("Entrez un nombre entier : "))
    if n>0:
        if n%2==0:
            print("Le nombre est positif et pair")
        else :
            print("Le nombre est positif et impair")
    elif n<0:
        if n%2==0:
            print("Le nombre est negatif et pair")
        else :
            print("Le nombre est negatif et impair")
    else: print("Le nombre est zero (et il est pair)")

def tp2exo6():
    if random.randint(0, 100)<50:
        print("Pile !")
    else: print("Face !")

def tp2exo7():
    if random.randint(1, 3)<3:
        print("Pile !")
    else: print("Face !")

def intervalle():
    x=int(input("Donner un Reel : "))
    if x<-10:
        print("x n'appartient pas a I")
    elif x<-2:
        print("x appartient a I")
    elif x==-2:
        print("x appartient a I")
    elif x<=0:
        print("x n'appartient pas a I")
    elif x==0:
        print("x n'appartient pas a I")
    elif x<=1:
        print("x appartient a I")
    elif x==1:
        print("x appartient a I")
    elif x<2:
        print("x n'appartient pas a I")
    elif x<3:
        print("x appartient a I")
    else : print("x n'appartient pas a I")
