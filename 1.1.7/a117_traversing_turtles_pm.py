#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Creating the turtle shapes 
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#  Setting initial starting point and direction of the first turtle
startx = 0
starty = 0
direction = 90

#  Draws the shapes in a color from the list of turtles
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  color = turtle_colors.pop()
  t.pencolor(color)
  t.fillcolor(color)
  t.pendown()
  t.right(45)     
  t.forward(50)
  t.fillcolor()
  t.pencolor()

#  Progress from end point of the last turtle to the next turtle
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()


wn = trtl.Screen()
wn.mainloop()