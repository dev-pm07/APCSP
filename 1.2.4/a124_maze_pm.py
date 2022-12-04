import turtle as trtl
import random as rand
import keyboard

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

maze_painter.pu()
maze_painter.goto(0, 50)
maze_painter.pd()
maze_painter.left(90)

def draw_barrier(toLoc):
    maze_painter.forward(toLoc)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.left(180)
    maze_painter.forward(path_width * 2)
    maze_painter.left(90)

def draw_door(toLoc):
    maze_painter.forward(toLoc)
    maze_painter.pu()
    maze_painter.forward(path_width * 2)
    maze_painter.pd()

for numOfWalls in range(24):

    if numOfWalls < 5:

        maze_painter.pu()
        maze_painter.forward(wallLen)
        maze_painter.left(90)
        wallLen += path_width
        maze_painter.pd()

    elif numOfWalls >= 20 and numOfWalls != 23:

        barrierLoc = rand.randint(0, ( wallLen - 50 ))
        remainingLen = wallLen - barrierLoc
        draw_barrier(barrierLoc)
        maze_painter.forward(remainingLen + ( path_width * 2 ))
        maze_painter.left(90)
        wallLen += path_width
    
    elif numOfWalls == 23:

        maze_painter.forward(wallLen)

    elif numOfWalls >= 5 and numOfWalls < 20:

        doorLoc = rand.randint(0, wallLen - ( path_width * 2 ))
        remainingLen = wallLen - doorLoc
        draw_door(doorLoc)
        if remainingLen < 50:
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

maze_painter.hideturtle()

# Add the runner

maze_runner = trtl.Turtle(shape = "turtle")
maze_runner.shapesize(1.5)
colors = ["silver", "royal blue", "medium turquoise", "dark slate gray", "lime green", "olive", 
          "goldenrod", "sandy brown", "maroon", "coral", "hot pink", "medium purple", "ghost white"]
maze_runner.pu()
maze_runner.setposition(-50, 0)
maze_runner.pd()
maze_runner.speed("fastest")

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160) # x,y set to fit on smaller screen
counter.pendown()
timer = 30


# countdown function
def countdown():
    global timer
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up!", font=("Nunito", 20, "normal"))
    elif keyboard.is_pressed('return'):
        return
    else:
        counter.write("Timer: " + str(timer), font=("Nunito", 20, "normal"))
        timer -= 1
        counter.getscreen().ontimer(countdown, 1000)

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
def done():    
    wn.clearscreen()
    wn.bgcolor("white smoke")
    counter.pu()
    counter.setposition(-250, 0)
    counter.pd()
    counter.write("Your time is: " + str(timer), font=("Nunito", 50, "normal"))

wn.onkeypress(up, "Up")
wn.onkeypress(right, "Right")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(changeColor, "space")
wn.onkeypress(done, "Return")

wn.listen()

countdown()

wn.mainloop()