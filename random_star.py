import turtle
from random import randint, random

def zufaellige_ungerade_zahl():
    while True:
        zahl = randint(5, 20)
        if zahl % 2 != 0: 
            return zahl
            break

def zeichne_stern(ecken_anzahl: int):
    winkel = 180 - (180 / ecken_anzahl)
    turtle.color(random(), random(), random())

    for _ in range(ecken_anzahl):
        turtle.forward(100)
        turtle.right(winkel)
    
    turtle.done()

def main():
    zeichne_stern(zufaellige_ungerade_zahl())

main()