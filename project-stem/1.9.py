# ********** Project Stem 1.9 **********
# ***** Praneel Mahalatkar 0/13/23 *****
#
# Description: This program is a tag game 
# between two turtles. The turtles will 
# move randomly around the screen. When 
# they collide, they respond with "ouch" 
# and back up from each other.
#
# Keybinds: Space (Return) - Move turtles
#
# Question imagine a more complex program 
# with hundreds of sprites. How might the 
# code be more difficult to read or maintain 
# if the default names of Sprite1, Sprite2,
# etc. were used? 
#
# They would be difficult to read and maintain
# since they would be individually numbered,
# and changing just one feature for all turtles
# would require going back to each of the 100
# turtles and change or add the feature. It would 
# be difficult to read since there would be a 100 
# statements for just one feature that the turtles
# would have. An alternative is putting the 100
# turtles in the list and use a loop to go through
# the whole loop and change one thing, so that there
# is only one place to change the code for all 100 
# turtles.
 
import turtle as trtl
import random as rand
 
wn = trtl.Screen()
 
font_setup = ("Nunito", 18, "bold")
 
trtlList = []
 
writer = trtl.Turtle()
writer.hideturtle()
writer.pu()
 
for i in range(2):
    turtle = trtl.Turtle()
    turtle.shape("turtle")
    trtlList.append(turtle)
    turtle.pu()
    turtle.color("green")
    turtle.color("green")
    turtle.goto(rand.randint(0, 400), rand.randint(0, 400))
 
interval = 25
 
def move():
    writer.clear()
    trtlList[0].color("green")
    trtlList[1].color("green")
    direction1 = rand.randint(0, 360)
    direction2 = rand.randint(0, 360)
    trtlList[0].setheading(direction1)
    trtlList[1].setheading(direction2)
    distance1 = rand.randint(50, 400)
    distance2 = rand.randint(50, 400)
    for i in range(interval):
 
        for turtles in range(len(trtlList)):
 
            if turtles == 1: 
                trtlList[turtles].forward(distance1/interval)
            else:
                trtlList[turtles].forward(distance2/interval)
 
            if abs(trtlList[turtles].xcor()) >= 400 or abs(trtlList[turtles].ycor()) >= 400:
                trtlList[turtles].goto(0, 0) 
 
            # The computer checks distance between the y coordinates of the turtles. 
            # if it is close enough, it will proceed to check the distance of the x
            # coordinates of the turtle. If both are true, then both turtles will turn
            # red, back up, and say "ouch", normal function will proceed on the next move.
 
            if abs(trtlList[0].ycor() - trtlList[1].ycor()) < 15:
                if abs(trtlList[0].xcor() - trtlList[1].xcor()) < 15:
                    for num in range(len(trtlList)):
                        trtlList[num].color("red")
                        trtlList[num].backward(75)
                        writer.goto(trtlList[num].xcor() + 20, trtlList[num].ycor() - 20)
                        writer.write("Ouch!", font=font_setup)
                        print("Ouch!")
                    return
 
wn.onkeypress(move, "space")
wn.listen()
    
wn.mainloop()
 
 
 
 

