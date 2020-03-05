import turtle as t

t.pencolor("yellow")
t.pensize(5)

t.fillcolor("yellow")

t.begin_fill()
t.circle(100, 360)
t.end_fill()

t.penup()
t.goto(-50, 110)
t.pendown()

t.fillcolor("black")

t.begin_fill()
t.circle(25, 360)
t.end_fill()

t.penup()
t.goto(50, 110)
t.pendown()

t.begin_fill()
t.circle(25, 360)
t.end_fill()

t.penup()
t.goto(0, 100)
t.pendown()

t.fillcolor("blue")
t.begin_fill()
t.goto(-30, 70)
t.goto(30, 70)
t.goto(0, 100)
t.end_fill()

t.penup()
t.goto(0, 33)

t.pendown()
t.pencolor("red")

t.circle(25, 90)
t.penup()
t.circle(25,180)
t.pendown()
t.circle(25,90)


t.mainloop()