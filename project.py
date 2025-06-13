import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(3)

# house base
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("black", "#6F4E37")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# roof
t.penup()
t.goto(-120, 100)
t.pendown()
t.color("black", "brown")
t.begin_fill()
t.goto(-40, 160)
t.goto(40, 160)
t.goto(120, 100)
t.goto(-120, 100)
t.end_fill()

# door
t.penup()
t.goto(-20, -100)
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(40)
t.right(90)
t.forward(100)
t.end_fill()

# left window
t.penup()
t.goto(-40, 0)
t.pendown()
t.color("black", "lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(30)
    t.right(90)
t.end_fill()

# right window
t.penup()
t.goto(70, 0)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(30)
    t.right(90)
t.end_fill()

# ground
t.penup()
t.goto(-300, -100)
t.setheading(0)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(25)
    t.right(90)
t.end_fill()

# sun
t.penup()
t.goto(200, 110)
t.color("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# sun rays
for angle in range(0, 360, 30):
    t.penup()
    t.goto(200, 150)
    t.setheading(angle)
    t.forward(40)
    t.pendown()
    t.forward(15)

# tree trunk (left)
t.penup()
t.goto(-230, -100)
t.setheading(0)
t.pendown()
t.color("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# tree trunk (right)
t.penup()
t.goto(180, -100)
t.setheading(0)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# tree leaves function
def draw_leaves(x, y):
    t.penup()
    t.goto(x, y)
    t.color("forestgreen")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# left tree leaves
draw_leaves(-220, -40)
draw_leaves(-240, -10)
draw_leaves(-200, -10)
draw_leaves(-240, -30)
draw_leaves(-200, -35)
draw_leaves(-220, -1)

# right tree leaves
draw_leaves(190, -40)
draw_leaves(170, -10)
draw_leaves(210, -10)
draw_leaves(170, -30)
draw_leaves(210, -35)
draw_leaves(190, -1)

# bird function
def draw_bird(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.setheading(60)
    t.forward(10)
    t.backward(10)
    t.setheading(120)
    t.forward(10)
    t.backward(10)

draw_bird(100, 200)
draw_bird(120, 210)
draw_bird(140, 195)

# chimney
t.penup()
t.goto(90, 100)
t.setheading(0)
t.pendown()
t.color("gray")
t.begin_fill()
for _ in range(2):
    t.forward(15)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

# smoke
def draw_smoke(x, y):
    t.penup()
    t.goto(x, y)
    t.color("lightgray")
    for _ in range(3):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        y += 15
        t.goto(x, y)

draw_smoke(97, 160)

# cloud function
def draw_cloud(x, y):
    for offset in [0, 15, 30, 45]:
        t.penup()
        t.goto(x + offset, y)
        t.pendown()
        t.color("white")
        t.begin_fill()
        t.circle(20)
        t.end_fill()

draw_cloud(-200, 180)
draw_cloud(0, 180)

# fence
def draw_fence(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.color("sienna")
    t.begin_fill()
    t.pendown()
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.end_fill()

for fx in range(-120, 121, 15):
    draw_fence(fx, -100)

t.hideturtle()
screen.mainloop()
