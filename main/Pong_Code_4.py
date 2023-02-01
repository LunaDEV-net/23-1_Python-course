# Code für die vierte Einheit der Einfuehrung in Python
# 1.2.2023

# Code by Volker

# Namen und Schlägerbewegung

import turtle

fenster = turtle.Screen()
fenster.title("Pong")
fenster.bgcolor("black")
fenster.setup(width=800, height=600)
fenster.tracer()

# neu:
name_a = turtle.textinput("Pong", "Name der ersten Spieler*in")
name_b = turtle.textinput("Pong", "Name der zweiten Spieler*in")


punkte_a = 0
punkte_b = 0
# Spieler*innen
schlaeger_a = turtle.Turtle()
schlaeger_b = turtle.Turtle()

schlaeger_a.speed(0)
schlaeger_a.shape("square")
schlaeger_a.color("white")
schlaeger_a.turtlesize(stretch_len=1, stretch_wid=5)
schlaeger_a.penup()
schlaeger_a.goto(-350, 0)

schlaeger_b.speed(0)
schlaeger_b.shape("square")
schlaeger_b.color("white")
schlaeger_b.turtlesize(stretch_len=1, stretch_wid=5)
schlaeger_b.penup()
schlaeger_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.xbewegung = 2
ball.ybewegung = 2

# Punktestandausgabe
stift = turtle.Turtle()
stift.speed(0)
stift.shape("square")
stift.color("white")
stift.penup()
stift.hideturtle()
stift.goto(0, 260)

def punktestand():
    ausgabetext = "Punkte A: " + str(punkte_a) + "   " + "Punkte B: " + str(punkte_b)
    stift.write(ausgabetext, align="center", font=("Courier", 20, "normal"))

punktestand()

# neu:

# Funktionen für die Bewegung
def schlaeger_a_hoch():
    y = schlaeger_a.ycor()
    y += 20
    schlaeger_a.sety(y)

def schlaeger_b_hoch():
    y = schlaeger_b.ycor()
    y += 20
    schlaeger_b.sety(y)

def schlaeger_a_runter():
    y = schlaeger_a.ycor()
    y -= 20
    schlaeger_a.sety(y)

def schlaeger_b_runter():
    y = schlaeger_b.ycor()
    y -= 20
    schlaeger_b.sety(y)



# Tasten
fenster.listen()
fenster.onkeypress(schlaeger_a_hoch, "w")
fenster.onkeypress(schlaeger_a_runter, "s")
fenster.onkeypress(schlaeger_b_hoch, "Up")
fenster.onkeypress(schlaeger_b_runter, "Down")

turtle.done()
