from turtle import *

winkel = 90
winkel2 = 120

def dreieck():

    forward(100)
    left(winkel2)
    forward(100)
    left(winkel2)
    forward(100)
    return 'Dreieck'

def quadrat():
    for _ in range(4):
        forward(100)
        right(winkel)
    return "Quadrat" 

ausgabe_dreieck = dreieck()
print(ausgabe_dreieck)
    
rueckgabe = quadrat()
print(rueckgabe)
