import turtle as t

def angle(j, l):
    t.forward(l)
    t.right(180 - j)
    t.forward(l)
    t.left(180 - j)

def star(x, y, n, a, l, c = "red"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(n):
        angle(a, l)
        t.right(360 // n)
    t.end_fill()

t.screensize(600,600,"yellow")
t.speed(10)

star(-200, -200, 5, 30, 20)
star(-100, -100, 6, 40, 30, "purple")
star(0, 0, 7, 50, 40, "green")
star(200, 200, 8, 60, 50)
star(280, 280, 9, 90, 10, "blue")

t.done()