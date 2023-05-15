import turtle
import time
import random

abstand = time.sleep(0.1)

fenster = turtle.Screen()
fenster.title("Israa @snake spiel")
fenster.setup(width=500, height=500)
fenster.bgcolor("black")

Kopf = turtle.Turtle()
Kopf.color("red")
Kopf.penup()
Kopf.goto(0,0)
Kopf.shape("square")
Kopf.direction="stop"

tortue = turtle.Turtle()
tortue.color("yellow")
tortue.penup()
tortue.goto(0,100)
tortue.shape("turtle")


def move():
    if Kopf.direction == "up":
        y = Kopf.ycor()
        Kopf.sety(y+1)
    if Kopf.direction == "right":
        x = Kopf.xcor()
        Kopf.setx(x+1)
    if Kopf.direction == "left":
        x = Kopf.xcor()
        Kopf.setx(x-1)
    if Kopf.direction == "down":
        y = Kopf.ycor()
        Kopf.sety(y-1)
def up():
    Kopf.direction = "up"
def down():
    Kopf.direction = "down"
def left():
    Kopf.direction = "left"
def right():
    Kopf.direction = "right"

fenster.listen()
fenster.onkeypress(up , "Up")
fenster.onkeypress(right , "Right")
fenster.onkeypress(left , "Left")
fenster.onkeypress(down , "Down")

erweiterung = []

while True:
    fenster.update()
    move()
    if Kopf.distance(tortue) < 20:
        y = random.randint(-255 , 255)
        x = random.randint(-255 , 255)
        tortue.goto(x,y)

        tortueNew = turtle.Turtle()
        tortueNew.color("green")
        tortueNew.penup()
        tortueNew.shape("square")
        erweiterung.append(tortueNew)
    for i in range(len(erweiterung) -1, 0 , -1):
        x = erweiterung[i-1].xcor()
        y = erweiterung[i-1].ycor()
        erweiterung[i].goto(x,y)
    
    if len(erweiterung) > 0:
        x = Kopf.xcor()
        y = Kopf.ycor()
        erweiterung[0].goto(x,y)




        abstand

fenster.mainloop()
