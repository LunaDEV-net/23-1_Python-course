import turtle as t

def clear():
    t.home()
    t.clear()
    t.reset()
def clearupSquare(posX=-285,posY=384):

    print()
def makeSquare(posX=228, posY=300, angle=10, cucolor="brown", forborwn=(-235.60,-180.68)):
    t.setheading(angle)
    t.penup()
    t.goto(posX, posY)
    if cucolor == "blue":
        t.color("dodger blue")
    else:
        t.color("saddle brown")
        t.goto(forborwn[0],forborwn[1])
    t.pendown()
    t.begin_fill()
    #begin square
    t.forward(569)
    t.right(90)
    t.forward(569/2)
    t.right(90)
    t.forward(569)
    forborwn = t.pos()
    print(forborwn)
    t.right(90)
    t.forward(569/2)
    #end square
    t.end_fill()
    print("hi")
    if cucolor == "blue":
        return forborwn
def skyControler(angle=0, height=0):
    #clear()
    t.speed(1000)
    f = makeSquare(-285, 384, cucolor="blue")
    makeSquare(-285, 384-569/2, cucolor="borwn", forborwn=f)
    #clearupSquare()
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