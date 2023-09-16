from turtle import *
from definitionen import *
from random import randint

def checke_kollision_mit_essen():
    if kopf.distance(essen) < 20:
    
        x = (random.randint(-9, 9) * 20)
        y = (random.randint(-9, 9) * 20)
        essen.goto(x, y)


        neues_segment = Turtle()
        neues_segment.speed(0)  
        neues_segment.shape("square")
        neues_segment.color("yellow")
        neues_segment.penup()
        segmente.append(neues_segment)