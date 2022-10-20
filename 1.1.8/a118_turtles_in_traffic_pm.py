 #   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across the screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later as well as two empty lists for the dead turtles
horiz_turtles = []
vert_turtles = []
deadvt_turtles = []
deadht_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

# Assign collision shape

colShape = "classic"

# Append colors to turtles and put in location

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

hts = ['fastest', 'fast', 'normal', 'slow']
vts = ['fastest', 'fast', 'normal', 'slow']

# TODO: move turtles across and down screen, stopping for collisions

for step in range(50):
  for ht in horiz_turtles:
    for vt in vert_turtles:

      if vt == 4:
        vt.speed(vts.pop())
        ht.speed(hts.pop())
      elif vt == 8:
        vt.speed(vts.pop())
        ht.speed(hts.pop())
      elif vt == 12:
        vt.speed(vts.pop())
        ht.speed(hts.pop())
      elif vt == 32:
        vt.speed(vts.pop())
        ht.speed(hts.pop())

      vt.forward(3)
      ht.forward(3)
      if (abs(ht.xcor() - vt.xcor()) < 20):
        if (abs(ht.ycor() - vt.ycor()) < 20):
          ht.fillcolor("gray")
          ht.shape(colShape)
          deadht_turtles.append(ht)
          horiz_turtles.remove(ht) 
          vt.fillcolor("gray")
          vt.shape(colShape)
          deadvt_turtles.append(vt)
          vert_turtles.remove(vt)
      

for ht in deadht_turtles:
  for vt in deadvt_turtles:
    vt.fillcolor("maroon")
    ht.fillcolor("maroon")
  
wn = trtl.Screen()
wn.mainloop()
