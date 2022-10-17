#   a116_buggy_image.py

import turtle as trtl

# Init pen to create the spider
spider = trtl.Turtle()
spider.pensize(40)

# Draw body of the spider
spider.circle(20)

# Init the total number of legs and leg length
totalLegs = 8
leg_length = 70
# y = 70

# Calculates and Init angle depnding on total number of legs
angle = 240 / totalLegs
spider.pensize(5)

# Draws totalLegs legs from center of spider leg_num times
leg_num = 0
angleAtleg_num = 0
while (leg_num < totalLegs/2):
  angleAtleg_num = angle*leg_num
  spider.goto(0,20)
  spider.setheading(angleAtleg_num)
  spider.forward(leg_length)
  leg_num = leg_num + 1

while (leg_num < totalLegs):
  angleAtleg_num = angle*leg_num + 40
  spider.goto(0,20)
  spider.setheading(angleAtleg_num)
  spider.forward(leg_length)
  leg_num = leg_num + 1

# Draw eyes

spider.goto(-6, 0)
spider.pencolor('red')
spider.fillcolor('red')
spider.begin_fill()
spider.circle(5)
spider.end_fill()
spider.penup()

spider.goto(16, 10)
spider.pendown()
spider.pencolor('red')
spider.fillcolor('red')
spider.begin_fill()
spider.circle(5)
spider.end_fill()
spider.penup()

  
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()