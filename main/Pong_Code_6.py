# Code für die vierte Einheit der Einfuehrung in Python
# 1.2.2023

# Punktestand-Zählen => fertig.

import turtle
import time

fenster = turtle.Screen()
fenster.title("Pong")
fenster.bgcolor("black")
fenster.setup(width=800, height=600)
fenster.tracer(0)

name_a = turtle.textinput("Pong", "Name der ersten Spieler*in")
name_b = turtle.textinput("Pong", "Name der zweiten Spieler*in")

bot_a = False
bot_b = False
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
ball.xbewegung = 2 + 12
ball.ybewegung = 2 + 12

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

# Funktionen für die Bewegung
def set_schlaeger_a(y):
    schlaeger_a.sety(y)

def set_schlaeger_b(y):
    schlaeger_b.sety(y)


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

if name_a == "bot":
    bot_a = True

if name_b == "bot":
    bot_b = True


# das eigentliche Spiel
while True:
    fenster.update()

    # Ballbewegung:
    # Geradeaus
    #time.sleep(0.000001)
    ball.setx(ball.xcor() + ball.xbewegung)
    ball.sety(ball.ycor() + ball.ybewegung)

    # Abprallen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.ybewegung *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.ybewegung *= -1

    #ummöglich
    if bot_a == True:
        set_schlaeger_a(ball.pos()[1])
    if bot_b == True:
        set_schlaeger_b(ball.pos()[1])

    # Ball fliegt aus dem Spielfeld
    if ball.xcor() > 350:
        punkte_a += 1  # neu
        stift.clear()
        punktestand()

        ball.goto(0, 0)
        ball.xbewegung *= -1

    if ball.xcor() < -350:
        punkte_b += 1  # neu
        stift.clear()
        punktestand()

        ball.goto(0, 0)
        ball.xbewegung *= -1

    # Ball zurückschlagen
    if ball.xcor() < -340 and ball.ycor() < schlaeger_a.ycor() + 50 and ball.ycor() > schlaeger_a.ycor() - 50:
        ball.xbewegung *= -1

    if ball.xcor() > 340 and ball.ycor() < schlaeger_b.ycor() + 50 and ball.ycor() > schlaeger_b.ycor() - 50:
        ball.xbewegung *= -1


