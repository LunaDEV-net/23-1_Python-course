import turtle as t


def makeSquare(posX, posY, angle=0, cucolor="brown"):
    if cucolor == "blue":
        t.color("dodger blue")
    else:
        t.color("saddle brown")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    print("hi")

def skyControler(angle):
    #in work
    print("in work")
    quit()