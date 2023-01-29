import turtle as t


def makeSquare(posX=228, posY=297, angle=0, cucolor="brown"):
    if cucolor == "blue":
        t.color("dodger blue")
    else:
        t.color("saddle brown")
    t.goto(posX,posY)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    print("hi")

def skyControler(angle=0, height=0):
    #clear()

    #in work
    print("in work")
    quit()

#berich in dem angezeigt werden soll


# Überreste beim drehen dur 4 4ecke in schwarz überschreichen
# gößrere 4ecke und dann rest abkatten <- Nicht errichbare stellen bei drehungen