import turtle
t = turtle.Turtle()

t.fillcolor('green')
t.begin_fill()

for i in range(2):
    t.forward(500)
    t.left(90)

    t.forward(250)
    t.left(90)

t.end_fill()

t.penup()
t.goto(230, 45)
t.pendown()

t.fillcolor('red')
t.begin_fill()

t.circle(80)
t.end_fill()

turtle.mainloop()