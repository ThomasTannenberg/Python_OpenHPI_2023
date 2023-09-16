from turtle import *
from definitionen import *

def koerper_bewegen():
    # Starten von hinten und bewege jedes Segment an die Position des vorherigen Segments
    for index in range(len(segmente) - 1, 0, -1):
        x = segmente[index - 1].xcor()
        y = segmente[index - 1].ycor()
        segmente[index].goto(x, y)

    # Überprüfe, ob die Schlange aus mehr als nur dem Kopf besteht
    if len(segmente) > 0:
        # Bewege das vorderste Segment (index 0) zur Position des Kopfes
        x = kopf.xcor()
        y = kopf.ycor()
        segmente[0].goto(x, y)
