import turtle as t

def rect(x, y, side):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90) 


t.screensize(800, 800, "green")

for i in range(10):
    rect(i * 5, i * 5, 100 - (i + 1)*10)

t.done()

