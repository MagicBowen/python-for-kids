import turtle as t

def rect(x, y, side, color = None):
    t.penup()
    t.goto(x, y)
    t.pendown() 
    if color != None:
        t.fillcolor(color)
        t.begin_fill()

    for _ in range(4):
        t.forward(side)
        t.left(90)

    if color != None:
        t.end_fill()

def rect_flower(x, y, size, n = 36, color = "red"):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.right(360 // n)
        rect(x, y, size)
    t.end_fill()

def circle_flower(x, y, size, n = 36, color = "red"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.right(360 // n)
        t.circle(size, 360)
    t.end_fill()    

t.screensize(600, 600, "yellow")

t.speed(10)

# circle_flower(0, 0, 30, 9, "blue")
circle_flower(-200, 120, 30, 12, "purple")

# rect_flower(-100, -100, 50)

rect_flower(200, 200, 50, 18, "green")

t.done()