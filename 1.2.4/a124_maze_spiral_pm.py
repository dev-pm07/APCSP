import turtle as trtl
import random as rand

# Init
wn = trtl.Screen()
wn.tracer(1, 0)
wn.setup(width = 1.0, height = 1.0)
wn.title("1.2.4 - Turtle Escape")

# Draw Walls
maze_painter = trtl.Turtle()
wallLen = 50
path_width = 35
maze_painter.pensize(10)

maze_painter.pu()
maze_painter.goto(0, 50)
maze_painter.pd()
maze_painter.left(90)

def draw_barrier():
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.left(180)
    maze_painter.forward(path_width * 2)
    maze_painter.left(90)

for numOfWalls in range(24):

    if numOfWalls < 5:

        maze_painter.forward(wallLen)
        maze_painter.left(90)
        wallLen += path_width

    elif numOfWalls >= 20 and numOfWalls != 23:

        barrier = rand.randint(0, ( wallLen - 50 ))
        remainingLen = wallLen - barrier
        maze_painter.forward(barrier)
        draw_barrier()
        maze_painter.forward(remainingLen + ( path_width * 2 ))
        maze_painter.left(90)
        wallLen += path_width
    
    elif numOfWalls == 23:

        maze_painter.forward(wallLen)

    elif numOfWalls >= 5 and numOfWalls < 20:

        door = rand.randint(0, wallLen - ( path_width * 2 ))
        remainingLen = wallLen - door
        maze_painter.forward(door)
        maze_painter.pu()
        maze_painter.forward(path_width * 2)
        maze_painter.pd()
        if remainingLen < 50:
            maze_painter.forward(remainingLen)
            maze_painter.left(90)
            wallLen += path_width
        else: 
            barrier = rand.randint(0, ( remainingLen - 50 ))
            remainingLen = remainingLen - barrier
            maze_painter.forward(barrier)
            draw_barrier()
            maze_painter.forward(remainingLen)
            maze_painter.left(90)
            wallLen += path_width

maze_painter.hideturtle()

wn.mainloop()