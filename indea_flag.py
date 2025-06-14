import turtle
t = turtle.Turtle()

for x in range(2):
    t.forward(500)
    t.left(90)

    t.forward(300)
    t.left(90)

t.penup()
t.goto(0,200)
t.pendown()

t.begin_fill()
t.fillcolor("orange")
for x in range(2):
    t.forward(500)
    t.left(90)

    t.forward(100)
    t.left(90)

t.end_fill()

t.penup()
t.goto(0,100)
t.pendown()

t.begin_fill()
t.fillcolor("green")
for x in range(2):
    t.forward(500)
    t.right(90)

    t.forward(100)
    t.right(90)

t.end_fill()


t.penup()
t.goto(250, 110)
t.pendown()
t.begin_fill()
t.fillcolor("navy")
t.circle(40)
t.end_fill()

t.penup()
t.goto(250, 120)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.circle(30)
t.end_fill()

t.penup()
t.goto(250, 145)
t.pendown()
t.begin_fill()
t.fillcolor("navy")
t.circle(5)
t.end_fill()
t.penup()

turtle.mainloop()