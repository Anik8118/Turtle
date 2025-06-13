import turtle

# Set up
screen = turtle.Screen()
screen.title("Duplex Home Drawing")
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(10)

# Function to draw rectangle
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw triangle (for roof)
def draw_triangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.goto(x + width/2, y + height)
    pen.goto(x, y)
    pen.end_fill()

# Draw Ground
draw_rectangle("green", -400, -150, 800, 150)

# First Floor
draw_rectangle("lightyellow", -150, -150, 300, 150)

# Second Floor
draw_rectangle("lightblue", -120, 0, 240, 120)

# Roof
draw_triangle("brown", -120, 120, 240, 80)

# Door
draw_rectangle("saddlebrown", -30, -150, 60, 90)

# Left Window (First Floor)
draw_rectangle("white", -120, -80, 50, 50)

# Right Window (First Floor)
draw_rectangle("white", 70, -80, 50, 50)

# Left Window (Second Floor)
draw_rectangle("white", -90, 30, 40, 40)

# Right Window (Second Floor)
draw_rectangle("white", 50, 30, 40, 40)

# Hide the turtle
pen.hideturtle()

# Done
turtle.done()
