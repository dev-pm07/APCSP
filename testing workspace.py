import turtle as trtl

maze_painter = trtl.Turtle()

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
maze_painter.speed("fastest")
maze_painter.left(90)
path_width = 15
doorlength = 10
wallLen = 50
barrierlength = path_width * 2
for i in range(25):
    if i < 4:
      maze_painter.forward(wallLen)
      maze_painter.left(90)
      wallLen += path_width
    else:
      maze_painter.forward(10)
      maze_painter.penup()
      maze_painter.forward(path_width * 2)
      maze_painter.pendown()
      maze_painter.forward(40)
      maze_painter.left(90)
      maze_painter.forward(path_width*2)
      maze_painter.back(path_width*2)
      maze_painter.right(90)
      maze_painter.forward(wallLen - ((path_width * 2) + 10))
      maze_painter.left(90)
      wallLen += path_width
  
maze_painter.hideturtle()

wn.mainloop()
