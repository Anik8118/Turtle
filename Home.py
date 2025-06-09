import turtle
t = turtle.Turtle()

#barir char paser tin
t.begin_fill()
t.fillcolor("chocolate")
t.penup()
t.goto(-100, -100)
t.pendown()
for _ in range(4):
    t.forward(200)  
    t.left(90)
t.end_fill()


#chal
t.begin_fill()
t.fillcolor("chocolate4")
t.penup()
t.goto(-120, 100)
t.pendown()
t.goto(0, 200)
t.goto(120, 100)
t.goto(-120, 100)
t.end_fill()

#doroja
t.penup()
t.goto(-20, -100)
t.pendown()

t.begin_fill()
t.fillcolor("brown3")
t.left(90)
t.forward(100)
t.right(90)
t.forward(40)
t.right(90)
t.forward(100)
t.end_fill()


#bam paser janala
t.penup()
t.goto(-40, 0)
t.pendown()
t.begin_fill()
t.fillcolor("brown3")
for _ in range(4):
    t.forward(30)
    t.right(90)
t.end_fill()

#dan paser janala
t.penup()
t.goto(70, 0)
t.pendown()
t.begin_fill()
t.fillcolor("brown3")
for _ in range(4):
    t.forward(30)
    t.right(90)
t.end_fill()

#ghorer vit
t.penup()
t.goto(-150, -100)
t.pendown()
t.left(90)

t.begin_fill()
t.fillcolor("gray")

for _ in range(2):
    t.forward(300)
    t.right(90)

    t.forward(25)
    t.right(90)
t.end_fill()
 
turtle.mainloop()