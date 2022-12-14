import turtle as trtl
import random as rand

# Init
wn = trtl.Screen()
wn.tracer(1, 0)
wn.setup(width = 1.0, height = 1.0)
wn.title("1.2.4 - Turtle Escape")
wn.bgcolor("white smoke")

# Draw Walls
maze_painter = trtl.Turtle()
wallLen = 50
path_width = 35
maze_painter.pensize(10)
isFirst = rand.randint(0, 1)
maze_painter.pu()
maze_painter.goto(0, 50)
maze_painter.pd()
maze_painter.left(90)

# Function for drawing barrier
def draw_barrier(toLoc):
    maze_painter.forward(toLoc)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.left(180)
    maze_painter.forward(path_width * 2)
    maze_painter.left(90)

# Function for drawing door
def draw_door(toLoc):
    maze_painter.forward(toLoc)
    maze_painter.pu()
    maze_painter.forward(path_width * 2)
    maze_painter.pd()

# Draw 24 walls
for numOfWalls in range(24):

    isFirst = rand.randint(0, 1)
    
    # For the first 5 walls, spiral, but with the pen up
    if numOfWalls < 5:

        maze_painter.pu()
        maze_painter.forward(wallLen)
        maze_painter.left(90)
        wallLen += path_width
        maze_painter.pd()

    # For walls 20 and 21, draw only wall and barrier
    elif numOfWalls >= 20 and numOfWalls < 22:

        barrierLoc = rand.randint(0, ( wallLen - 50 ))
        remainingLen = wallLen - barrierLoc
        draw_barrier(barrierLoc)
        maze_painter.forward(remainingLen + ( path_width * 2 ))
        maze_painter.left(90)
        wallLen += path_width
    
    # For wall 22, just draw flat wall
    elif numOfWalls == 22:

        maze_painter.forward(wallLen + (path_width * 2))
        maze_painter.left(90)
        wallLen += path_width

    # For wall 23, just draw a flat wall but not going past width and turning.
    elif numOfWalls == 23:

        maze_painter.forward(wallLen)

    # For walls 5 - 19, draw walls and barriers normally.
    elif numOfWalls >= 5 and numOfWalls < 20:

        # Draw door first, then barrier
        if isFirst == 0:

            # Draw door with random location.
            doorLoc = rand.randint(path_width * 2, wallLen - ( path_width * 2 ))
            remainingLen = wallLen - doorLoc
            draw_door(doorLoc)

            # Draw barrier if the remaining distance is greater than twice the path width
            if remainingLen < path_width * 2:
                maze_painter.forward(remainingLen)
                maze_painter.left(90)
                wallLen += path_width
            else: 
                barrierLoc = rand.randint(0, ( remainingLen - 50 ))  
                remainingLen = remainingLen - barrierLoc
                draw_barrier(barrierLoc)
                maze_painter.forward(remainingLen)
                maze_painter.left(90)
                wallLen += path_width

        # Draw barrier first, then door. 
        elif isFirst == 1:

            # Draw barrier with random location
            barrierLoc = rand.randint(path_width * 2, wallLen - 50)  
            remainingLen = wallLen - barrierLoc
            draw_barrier(barrierLoc)

            # Draw door if the remaining distance is greater than twice the path width
            if remainingLen < path_width * 2:

                maze_painter.forward(remainingLen)
                maze_painter.left(90)
                wallLen += path_width
                
            else: 
                
                doorLoc = rand.randint(0, ( remainingLen - ( path_width * 2 ) ))
                remainingLen = remainingLen - doorLoc
                draw_door(doorLoc)
                maze_painter.forward(remainingLen)
                maze_painter.left(90)
                wallLen += path_width

# Draw Finish Line

maze_painter.pu()
maze_painter.goto(400, -375)
maze_painter.pd()
maze_painter.seth(270)
maze_painter.pencolor('lime green')
maze_painter.pensize(35)
maze_painter.forward(75)

maze_painter.hideturtle()

# Add the runner

maze_runner = trtl.Turtle(shape = "turtle")
maze_runner.shapesize(1.5)

# Add custom colors
colors = ["silver", "royal blue", "medium turquoise", "dark slate gray", "lime green", "olive", 
          "goldenrod", "sandy brown", "maroon", "coral", "hot pink", "medium purple", "ghost white"]
maze_runner.color(colors[rand.randint(0, 12)])
maze_runner.pu()
maze_runner.setposition(-50, 0)
maze_runner.pd()
maze_runner.speed("fastest")

# Init the timer
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(550, 350)
counter.pendown()
timer = 30

def countdown():
  global timer
  counter.clear()
  # Add fail message
  if timer <= 0:
    wn.clearscreen()
    counter.pu()
    counter.setposition(-350, 0)
    counter.pd()
    counter.write("You Failed to Escape!", font=("Nunito", 50, "normal"))
  # Add succeed message
  elif maze_runner.xcor() > 400:
    wn.clearscreen()
    counter.pu()
    counter.setposition(-425, 0)
    counter.pd()
    counter.write("You Escaped in: " + str( 60 - timer ) + " seconds!", font=("Nunito", 50, "normal"))
  else:
    counter.write("Timer: " + str(timer), font=("Nunito", 35, "normal"))
    timer -= 1
    counter.getscreen().ontimer(countdown, 1000)     

# Init controls
def up():
    maze_runner.seth(90)
    maze_runner.forward(10)
def right():
    maze_runner.seth(0)
    maze_runner.forward(10)
def down():
    maze_runner.seth(270)
    maze_runner.forward(10)
def left():
    maze_runner.seth(180)
    maze_runner.forward(25)
def changeColor():
    maze_runner.color(colors[rand.randint(0, 12)])

wn.onkeypress(up, "Up")
wn.onkeypress(up, "w")
wn.onkeypress(right, "Right")
wn.onkeypress(right, "d")
wn.onkeypress(down, "Down")
wn.onkeypress(down, "s")
wn.onkeypress(left, "Left")
wn.onkeypress(left, "a")
wn.onkeypress(changeColor, "space")

wn.listen()

# Start Countdown
countdown()

wn.mainloop()