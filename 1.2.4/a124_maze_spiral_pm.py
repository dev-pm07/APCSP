import turtle as trtl

# Init
wn = trtl.Screen()
wn.tracer(1, 0)
wn.setup(width = 1.0, height = 1.0)
wn.title("1.2.4 - Turtle Escape")

# Draw Walls
maze_painter = trtl.Turtle()
wallLen = 50
maze_painter.pensize(10)
distBtwWalls = 100

maze_painter.setposition(0, 100)
maze_painter.left(90)

for walls in range(2):
    maze_painter.pu()
    maze_painter.forward(wallLen)
    maze_painter.left(90)
    wallLen += distBtwWalls/2

for walls in range(18):
    maze_painter.pd()
    maze_painter.forward(10)
    maze_painter.pu()
    maze_painter.forward(distBtwWalls)
    maze_painter.pd()
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(distBtwWalls)
    maze_painter.left(180)
    maze_painter.forward(distBtwWalls)
    maze_painter.left(90)
    maze_painter.forward(wallLen - (10 + 35))
    maze_painter.left(90)
    wallLen += 35

maze_painter.hideturtle()

wn.mainloop()