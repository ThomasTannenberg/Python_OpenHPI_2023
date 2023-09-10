from daten import punkte_liste
from turtle import *

def gehe_wenn_nah(punkt: list):
    
    if distance(punkt) < 100:
        goto(punkt)
    else:
        goto(0, 0)

def main(liste: list):
    for punkt in liste:
        gehe_wenn_nah(punkt)



main(punkte_liste)