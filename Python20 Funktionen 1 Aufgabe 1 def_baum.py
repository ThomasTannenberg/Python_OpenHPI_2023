from turtle import *

def baum():
    left(90)
    forward(30)
    left(90)
    forward(30)
    right(120)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(30)

def gehe_nach_rechts():
    penup()
    forward(50)
    setheading(0)
    pendown()

baum()
gehe_nach_rechts()
baum()
gehe_nach_rechts()
baum()