#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "1.2.3/sprites/apple.gif"  # Store the file name of your shape

alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("1.2.3/sprites/background.gif")
appleList = []
letterList = []
letterTrtlList = []
letterTrtlIndex = 0
letterTrtl = trtl.Turtle()
for letters in range(5):
  letter = trtl.Turtle()
  letterTrtl.hideturtle()
  letterTrtlList.append(letter)
for apples in range(5):
  apple = trtl.Turtle()
  apple.hideturtle()
  appleList.append(apple)


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  active_apple.penup()
  wn.update()
  alphaIndex = rand.randint(0, 25)
  active_apple.setx(rand.randint(-175,175)) #reset the apple position
  active_apple.sety(rand.randint(-25,100)) #reset the apple position
  global letterTrtl
  global letter
  global alpha
  global letterTrtlIndex
  letter = alpha.pop(alphaIndex)
  letterList.append(letter)
  letterTrtlList[letterTrtlIndex].color('white')
  letterTrtlList[letterTrtlIndex].hideturtle()
  letterTrtlList[letterTrtlIndex].penup()
  letterTrtlList[letterTrtlIndex].setposition(active_apple.xcor() - 13,                                                              active_apple.ycor() - 30)
  letterTrtlList[letterTrtlIndex].write(letter, font=("Arial", 35))
  letterTrtlIndex += 1

# pressedApple
def drop(apple, letter):
  wn.tracer(n=1, delay=0)
  apple.penup()
  apple.penup()
  apple.right(
      90
  )  # turtle always face the right, so to make it "fall" it must turn right by 90
  letter.right(90)
  while apple.ycor() > -150:
      letter.forward(10)  # Apple falling of the tree"
      letter.clear()
      letter.forward(10)
      letter.write(letter, font=("Arial", 35))



#-----function calls-----
for appleIndex in range(5):
  draw_apple(appleList[appleIndex])
  
for i in range(5):
  
  wn.onkeypress(lambda apple = appleList[i]: lambda letter = letterTrtlList[i]: drop(apple, letter), letterList[i])
  
wn.listen()

wn.mainloop()
