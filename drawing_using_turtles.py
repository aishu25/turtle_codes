from turtle import *
from random import *
import itertools
import turtle

# drawing stars:
spiral = turtle.Turtle()
for i in range(30):
    spiral.forward(i * 10)
    spiral.right(144)
    turtle.done()

# drawing spiral rings
t = Turtle()
t.screen.bgcolor("black")
colors = ["red","yellow","purple","pink"]
t.screen.tracer(0,0)

for x in range(100):
	t.circle(x)
	t.color(colors[x%4])
	t.left(60)
t.screen.exitonclick()
t.screen.mainloop()


# drawing rectangle:
def random_place():
	penup()
  	x = randint(-100, 100)
  	y = randint(-100, 100)
  	goto(x,y)
  	pendown()

def drawrectangle():
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
  r = randint(0,255) # makes variables r,g,b whose value is an integer,
  g = randint(0,255) # which is between 0 and 255. It is random, and
  b = randint(0,255) # changes every time the loop runs
  colormode(255)  # this is something that is irrelevant at this point
	         	  #check the pythondocs link at the end for more info
  pencolor(r,g,b) # changes the color of the pen to the rgb coordinates
	              # obtained by the variables r, g, b changing each time
	
for i in range(30):
	drawrectangle()
	random_place()
Turtle().screen.exitonclick()
Turtle().screen.mainloop()
 
# writing using turtle
t = Turtle()
t.hideturtle()
t.write("Cool Python Codes",move=True,align="center",font=("Freestyle Script",50,"normal"))
Turtle().screen.exitonclick()
Turtle().screen.mainloop()



# moving and changing speed
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()