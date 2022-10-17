#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "turtle", "arrow"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "maroon", "violet"]

# constructing shape-color duo
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#  Creating initial starting point and direction
startx = 0
starty = 0
direction = 175

#  Draws the shapes from the list of turtles
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  color = turtle_colors.pop()
  t.pencolor(color)
  t.fillcolor(color)
  t.pensize(20)
  t.pendown()
  t.right(45)     
  t.forward(75)
  t.fillcolor()
  t.pencolor()

#  Progress from end point
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()


wn = trtl.Screen()
wn.mainloop()