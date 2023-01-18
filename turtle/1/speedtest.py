import turtle as t
t.penup()
t.goto(50,50)

for i in range(1, 5):
    t.pendown()
    t.right(90)
    t.forward(100)
    print(i)
    t.penup()
t.home()
input("")