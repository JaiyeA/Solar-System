import turtle
import random
#function that creates and postions the sun and planets
def planet(speed,r,g,b,xcor,ycor,circle_size):
  name=turtle.Turtle()
  name.speed(speed)
  name.hideturtle()
  name.color(r,g,b)
  name.penup()
  name.setpos(xcor,ycor)
  name.pendown()
  name.begin_fill()
  name.circle(circle_size)
  name.end_fill()
#function that creates a ring around a planet
def ring(speed,color,xcor,ycor,right,forward):
  r = turtle.Turtle()
  r.speed(speed)
  r.hideturtle()
  r.pencolor(color)
  r.penup()
  r.setpos(xcor,ycor)
  r.pendown()
  r.right(right)
  r.forward(forward)
#function that creates stars
def stars(xcor,ycor):
  s = turtle.Turtle()
  s.speed(10)
  s.hideturtle()
  s.penup()
  s.setpos(xcor,ycor)
  s.pendown()
  s.color('white')
  s.begin_fill()
  s.circle(1)
  s.end_fill()
#filling the background black
screen = turtle.Screen()
screen.bgcolor('black')
#setting the attributes and positions for the sun and each planet
sun = planet(10,255,109,0,-400,-200,200)
mercury = planet(10,150,150,150,-150,-40,10)
venus = planet(10,265,160,122,-100,-50,20)
earth = planet(10,0,0,255,-35,-55,25)
#creating earth land
g=turtle.Turtle()
g.hideturtle()
g.color('green')
g.penup()
g.setpos(-36,-54)
g.pendown()
g.begin_fill()
g.circle(25,140,10)
g.end_fill()

mars = planet(10,255,0,0,20,-45,10)
jupiter = planet(10,265,160,122,120,-120,80)
saturn = planet(10,210,180,140,275,-100,50)
sat_ring = ring(10,'c2b280',210,-50,0,130)
uranus = planet(10,13,152,186,380,-90,35)
u_ring = ring(10,'d3d3d3',380,-10,90,90)
neptune = planet(10,30,144,255,460,-80,25)
pluto = planet(10,194,178,128,510,-60,6.5)
#creating and positioning stars without them overlapping planets and the sun
for star in range(80):
  stars(random.randint(-250,600),random.randint(50,400))
  stars(random.randint(-250,600),random.randint(-400,-150))
 
