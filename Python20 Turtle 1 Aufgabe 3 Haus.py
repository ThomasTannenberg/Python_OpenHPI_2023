from turtle import * 

'''
Nun möchte Leonie ein bisschen Farbe verwenden. 
Sie will ein Quadrat mit Kantenlänge 100 malen, das blau gefüllt ist 
und auf einem grünen Hintergrund steht. 
Außerdem soll die Stiftfarbe gelb sein und alle vier Seiten 
des Quadrats sollen durch Turtle abgelaufen werden.
'''


bgcolor("green")
pencolor("yellow")
fillcolor("blue")
begin_fill()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()