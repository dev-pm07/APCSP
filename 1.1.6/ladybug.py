#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

# Init the total number of legs and leg length
totalLegs = 6
leg_length = 70
# y = 70

# Calculates and Init angle depnding on total number of legs
angle = 240 / totalLegs
ladybug.pensize(5)

# Draws totalLegs legs from center of ladybug leg_num times
leg_num = 0
angleAtleg_num = 0
while (leg_num < totalLegs/2):
    angleAtleg_num = angle*leg_num
    ladybug.penup()
    ladybug.goto(0,-25)
    ladybug.pendown()
    ladybug.setheading(angleAtleg_num)
    ladybug.forward(leg_length)
    leg_num = leg_num + 1

while (leg_num < totalLegs):
    angleAtleg_num = angle*leg_num + 40
    ladybug.penup()
    ladybug.goto(0,-25)
    ladybug.pendown()
    ladybug.setheading(angleAtleg_num)
    ladybug.forward(leg_length)
    leg_num = leg_num + 1
ladybug.setheading(0)
ladybug.penup()

# create ladybug head
ladybug.goto(-17,0)
ladybug.pendown()
ladybug.pensize(27)
ladybug.circle(5)

# and body
color = input("What color do you want the body to be?    ")
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color(color)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1
  print(xpos + ypos)


ladybug.hideturtle()

trtl.Screen().bgcolor('green')
wn = trtl.Screen()
wn.mainloop()