#   a114_nested_loops_3.py
import turtle as trtl

color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1

  angle = float(input("angle:"))
  
  while painter.ycor() < height:
    if space % 100 == 0:
        painter.fillcolor(color1)
        painter.color(color1)
    elif space % 100 >= 1:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1
  
  seg = float(360/angle)

  answer = input("again?")

wn.bye()