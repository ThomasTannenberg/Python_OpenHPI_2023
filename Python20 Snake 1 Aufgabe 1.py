'''
grafische Steurung
'''
rechts = Turtle()
rechts.shape("triangle")
rechts.color("green")
rechts.speed(0)
rechts.penup()
rechts.goto(180, -160)

unten = Turtle()
unten.shape("triangle")
unten.color("green")
unten.right(90)
unten.speed(0)
unten.penup()
unten.goto(160, -180)

oben = Turtle()
oben.shape('triangle')
oben.color('green')
oben.left(90)
oben.speed(0)
oben.penup()
oben.goto(160,-140)

links = Turtle()
links.shape('triangle')
links.color('green')
links.left(180)
links.speed(0)
links.penup()
links.goto(140, -160)