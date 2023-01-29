import turtle as t


def makeSquare(posX=228, posY=297, angle=0, cucolor="brown"):
    t.setheading(0)
    t.penup()
    if cucolor == "blue":
        t.color("dodger blue")
    else:
        t.color("saddle brown")
    t.goto(posX,posY)
    t.pendown()
    t.begin_fill()
    #begin square
    t.forward(569)
    t.right(90)
    t.forward(569/2)
    t.right(90)
    t.forward(569)
    t.right(90)
    t.forward(569/2)
    #end square
    t.end_fill()
    print("hi")

def skyControler(angle=0, height=0):
    #clear()
    makeSquare(-285, 384, cucolor="blue")
    makeSquare(-285, 384-569/2, cucolor="borwn")
    #makeSquare(-285, 384 - 569 / 2, cucolor="blue")
    #in work
    print("in work")


def configureWindow():
    """sets the Window Size, change BG color and the Title"""
    t.screensize(1024, 966, bg="black")
    print(f" set Window Size")
    print(f" set Window BG Color")
    t.title("LUNA: Airplane PFD")
    print(f" set Window Title")

configureWindow()
#makeSquare(int(input("X: ")), int(input("Y: ")))
#makeSquare(int(input("X2: ")), int(input("Y2: ")), cucolor="blue")
skyControler()
input()

#-285
#384