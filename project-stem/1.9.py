import turtle as trtl
import random as rand

wn = trtl.Screen()

trtlList = []

for i in range(2):
    turtle = trtl.Turtle()
    turtle.shape("turtle")
    trtlList.append(turtle)

def move():
    for turtles in range(len(trtlList)):
        direction = rand.randint(0, 360)
        trtlList[turtles].setheading(direction)
        distance = rand.randint(15, 400)
        trtlList[turtles].forward(distance)
        if abs(trtlList[turtles].xcor()) >= 400 or abs(trtlList[turtles].ycor()) >= 400:
            trtlList[turtles].pu()
            trtlList[turtles].goto(0, 0) 
            trtlList[turtles].pd()

wn.onkeypress(move, "space")
wn.listen()
    
wn.mainloop()


 