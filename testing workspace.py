import turtle as trtl
import random as rand

# Configurations / Variables for the maze

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
maze_painter = trtl.Turtle()
maze_painter.speed("fastest")
maze_painter.left(90)
path_width = 15
doorlength = 10
wallLen = 50
barrierlength = path_width * 2
num_sides = 29
 
def drawdoor(pos):
  maze_painter.forward(pos)
  maze_painter.penup()
  maze_painter.forward(path_width*2)
  maze_painter.pendown()
 
def drawbarrier(pos):
  maze_painter.forward(pos)
  maze_painter.left(90)
  maze_painter.forward(path_width*2)
  maze_painter.backward(path_width*2)
  maze_painter.right(90)
 

# draw maze and make it draw from middle out

wallLen = path_width
for w in range(num_sides):
  wallLen += path_width
 
  if (w > 5):
    maze_painter.left(90)
 
    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wallLen - path_width*2))
    barrier = rand.randint(path_width*2, (wallLen - path_width*2))
    # if a door and barrier would be rendered on top of each other, get a new value
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wallLen - path_width*2))
 
    if (door < barrier):
      drawdoor(door)
      drawbarrier(barrier - door - path_width*2)
      # draw rest of the wall
      maze_painter.forward(wallLen - barrier)
    else:
      drawbarrier(barrier)
      drawdoor(door - barrier)
      # draw rest of the wall
      maze_painter.forward(wallLen - door - path_width*2)
maze_painter.hideturtle()
 
# Add the maze runner

maze_runner = trtl.Turtle(shape="turtle")
maze_runner.fillcolor("black")
maze_runner.color("red")
maze_runner.penup()
maze_runner.goto(-50, -60)
maze_runner.pendown()

# Changing direction

def up():
    maze_runner.setheading(90)
def down():
    maze_runner.setheading(270)
def left():
    maze_runner.setheading(180)
def right():
    maze_runner.setheading(0)

# How far the runner will move based on user's keypress

def ss(): # Slow speed
  maze_runner.forward(5)
def ms(): # Medium speed
  maze_runner.forward(10)
def hs(): # High speed
  maze_runner.forward(15)
def vfs(): # Very fast speed
  maze_runner.forward(25)
def fst(): # Fastest speed( Turtle will legit be the flash)
  maze_runner.forward(35)
# Make it so the turtle moves when the specified key is pressed
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')
wn.onkeypress(ss, '1')
wn.onkeypress(ms, '2')
wn.onkeypress(hs, '3')
wn.onkeypress(vfs, '4')
wn.onkeypress(fst, '5')
wn.listen()


wn.mainloop()