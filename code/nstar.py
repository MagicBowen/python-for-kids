import turtle as t

def angle(side, angle):
    t.right(angle)
    t.forward(side)
    t.right(180 - angle * 2)
    t.forward(side)
    t.left(180 - angle)

def star(x, y, side, a, n, color = "red"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        angle(side, a)
        t.right(360 // n)
    t.end_fill()

t.speed(10)
star(0, 0, 50, 30, 8)
star(100, 100, 30, 60, 9, "yellow")
t.done()