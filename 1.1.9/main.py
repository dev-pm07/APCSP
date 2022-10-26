import turtle
import random as rand
import time

organism = turtle.Turtle()

wn = turtle.Screen()

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
numOfBarnacles = 15
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
        print(differenceXValues)
        print(differenceYValues)

    

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

    print(topTakenCoords)

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
        print(differenceXValues)
        print(differenceYValues)

    

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

    print(bottomTakenCoords)

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

bubble = turtle.Turtle()
bubble.speed('slowest')

wn.tracer(0)

while True:
    for numOfCoordinates in range(len(barnacleCoords)):
        bubbleSize = rand.randint(5, 10)

        print(barnacleCoords[numOfCoordinates])

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

        # setting the turtle object width  
        bubble.width(2)  

        # hiding the turtle object  
        bubble.hideturtle()  

        # turtle object in air  
        bubble.penup()  

        # setting the initial position  
        bubble.goto(barnacleCoords[numOfCoordinates][0], barnacleCoords[numOfCoordinates][1])  

        # moving turtle object to the surface  
        bubble.pendown() 

        # clearing the past location of bubble
        bubble.clear()  

        # calling the method to draw the bubble  
        airBubble(bubble) 

        bubble.setheading(90)

        # updating the screen  
        turtle.update()  

        # forward motion by turtle object  
        while bubble.ycor() < 450:
            bubble.forward(0.6)
            turtle.delay(5000)