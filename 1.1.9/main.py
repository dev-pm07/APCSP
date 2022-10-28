from turtle import Screen, Turtle
import random as rand

COLOR = (0, .4118, .5804)  # (0% red, 41.18% green and 58.04% blue) top color
TARGET = (.1804, .5451, .3412)  # (18.04% red, 54.51% green and 34.12% blue) bottom color


wn = Screen()
wn.tracer(False)

WIDTH, HEIGHT = wn.window_width(), wn.window_height()

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH, HEIGHT)#size1
turtle.pendown()

direction = 2

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):#size2

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

wn.tracer(True)

organism = Turtle()

organism.speed('fastest')

# Set background color to sea
wn.bgcolor('medium blue') 

organism.pencolor('crimson')
organism.penup()
organism.goto(100, 0)
organism.pendown()

head = 0
organism.fillcolor('crimson')
organism.begin_fill()

# Create Starfish
for i in range(5):
    head = head + 144
    organism.setheading(head)
    organism.forward(200)

organism.end_fill()

topTakenCoords = []
sizeOfBarnacles = 20
numOfBarnacles = 25
distBtwBarnacles = sizeOfBarnacles*2
spawnSquare = 300
numOfTakenCoords = 0
takenXValues = []
takenYValues = []

for i in range(numOfBarnacles):

    differenceXValues = []
    differenceYValues = []

    xcoordinate = rand.randint(100, spawnSquare)
    ycoordinate = rand.randint(100, spawnSquare)

    coordinate = [xcoordinate, ycoordinate]
    
    def check():
        for numOfCoords in range(len(topTakenCoords)):
            takenXValues.append(topTakenCoords[numOfCoords][0])
            takenYValues.append(topTakenCoords[numOfCoords][1])
        differenceXValues = [abs(xvalues - coordinate[0]) for xvalues in takenXValues]
        differenceYValues = [abs(yvalues - coordinate[1]) for yvalues in takenYValues]

    

    if all(value < distBtwBarnacles for value in differenceXValues):
        coordinate[0] = rand.randint(100, spawnSquare)
        check()
    else:
        pass
    
    if all(value < distBtwBarnacles for value in differenceYValues):
        coordinate[1] = rand.randint(100, spawnSquare)
        check()
    else:
        pass

    topTakenCoords.append(coordinate)

    organism.pencolor('gainsboro')
    organism.fillcolor('gainsboro')

    organism.penup()
    organism.goto(coordinate[0], coordinate[1])
    organism.pendown()

    organism.begin_fill()
    organism.circle(10)
    organism.end_fill()

bottomTakenCoords = []
sizeOfBarnacles = 20
numOfBarnacles = 15
distBtwBarnacles = sizeOfBarnacles*2
numOfTakenCoords = 0
takenXValues = []
takenYValues = []

for i in range(numOfBarnacles):

    differenceXValues = []
    differenceYValues = []

    xcoordinate = rand.randint(-300, -100)
    ycoordinate = rand.randint(-300, -100)

    coordinate = [xcoordinate, ycoordinate]
    
    def check():
        for numOfCoords in range(len(bottomTakenCoords)):
            takenXValues.append(bottomTakenCoords[numOfCoords][0])
            takenYValues.append(bottomTakenCoords[numOfCoords][1])
        differenceXValues = [abs(xvalues - coordinate[0]) for xvalues in takenXValues]
        differenceYValues = [abs(yvalues - coordinate[1]) for yvalues in takenYValues]

    

    if all(value < distBtwBarnacles for value in differenceXValues):
        coordinate[0] = rand.randint(-300, -100)
        check()
    else:
        pass
    
    if all(value < distBtwBarnacles for value in differenceYValues):
        coordinate[1] = rand.randint(-300, -100)
        check()
    else:
        pass

    bottomTakenCoords.append(coordinate)

    organism.pencolor('gainsboro')
    organism.fillcolor('gainsboro')

    organism.penup()
    organism.goto(coordinate[0], coordinate[1])
    organism.pendown()

    organism.begin_fill()
    organism.circle(10)
    organism.end_fill()

barnacleCoords = topTakenCoords + bottomTakenCoords
organism.hideturtle()

bubble = Turtle()
bubble.speed('slowest')

wn.tracer(0)

while True:
    for numOfCoordinates in range(len(barnacleCoords)):
        bubbleSize = rand.randint(5, 10)

        indexNum = rand.randint(0, ((numOfBarnacles*2) - 1))

        def airBubble(bubble):  
        
            # filling the color in the bubble  
            bubble.fillcolor('medium turquoise')  
        
            # starting to color the bubble  
            bubble.begin_fill()  
        
            # drawing the circle  
            bubble.circle(bubbleSize)  
        
            # ending the color filling in the bubble  
            bubble.end_fill()  

        # setting the turtle object color to light sea green  
        bubble.color('light sea green')  

        # setting the turtle object speed  
        bubble.speed(0)  

        # setting the turtle object width  
        bubble.width(2)  

        # hiding the turtle object  
        bubble.hideturtle()  

        # turtle object in air  
        bubble.penup()  

        # # setting the initial position  
        bubble.goto(barnacleCoords[indexNum][0], barnacleCoords[indexNum][1])  

        # moving turtle object to the surface  
        bubble.pendown() 

        bubble.speed('slowest')

        while bubble.ycor() < 450:  

            # clearing the past location of bubble
            bubble.clear()  

            # calling the method to draw the bubble  
            airBubble(bubble) 

            bubble.setheading(90)

            # updating the screen  
            wn.update()  

            # forward motion by turtle object  
            bubble.forward(5)  
        
        bubble.clear()