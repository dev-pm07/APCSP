#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "1.2.3/sprites/pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("1.2.3/sprites/background.gif")
apple = trtl.Turtle()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()

def drop():
  apple.penup()
  apple.right(90) # turtle always face the right, so to make it "fall" it must turn right by 90
  while apple.ycor() > -150:
    apple.forward(10) # Apple falling of the tree"

wn.onkeypress(drop, "a")
wn.listen()
    
#-----function calls-----
draw_apple(apple)

wn.mainloop()
