import turtle as t

t.color("red", "red")
t.speed(3)

t.begin_fill()
# t.right(27)

for _ in range(5):
    t.forward(200)
    t.right(144)

t.end_fill()

t.penup()

t.goto(-100, 100)

t.pencolor("blue")

t.write("王嘉硕", font=('Arial', 40, 'normal'))

t.done()