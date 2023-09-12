import turtle
import random

def wildes_fahren():


    wild = turtle.Turtle()

    

    anzahl_linien = random.randint(10, 40)

    for _ in range(anzahl_linien):

        laenge = random.randint(10, 100)
        winkel = random.randint(10, 170)


        wild.forward(laenge)

        if random.choice([True, False]):
            wild.right(winkel)
        else:
            wild.left(winkel)


wildes_fahren()