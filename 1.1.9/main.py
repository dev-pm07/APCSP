from turtle import Screen, Turtle
import random as rand

# Set colors for gradient

COLOR = (0, .4118, .5804)  # (0% red, 41.18% green and 58.04% blue) top color
TARGET = (.1804, .5451, .3412)  # (18.04% red, 54.51% green and 34.12% blue) bottom color

# Init Screen

wn = Screen()
wn.tracer(False)
turtle = Turtle()

# wn.setup(width = 1920, height = 1080)


WIDTH, HEIGHT = wn.window_width(), wn.window_height()

# Set deltas

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]


turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH, HEIGHT)#size1
turtle.pendown()

# Set direction and create gradient

direction = 2

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):#size2

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

wn.tracer(True)

# Create organism turtle to create organisms

organism = Turtle()

organism.speed('fastest')

# Create starfish organism

organism.pencolor('crimson')
organism.penup()
organism.goto(200, -50)
organism.pendown()

head = 0
organism.fillcolor('crimson')
organism.begin_fill()

for i in range(5):
    head = head + 144
    organism.setheading(head)
    organism.forward(400)
    
organism.end_fill()



# # Ask user how many barnacles they want on each side of the starfish

numOfBarnacles = int(input("How many barnacles do you want on each side of the starfish?    "))

# Create top right barnacles in certain area and record each coordinate and compare to make sure they are not touching at least one barnacle

topTakenCoords = []
sizeOfBarnacles = 20
distBtwBarnacles = sizeOfBarnacles*2
numOfTakenCoords = 0
takenXValues = []
takenYValues = []

for i in range(numOfBarnacles):

    differenceXValues = []
    differenceYValues = []

    xcoordinate = rand.randint(200, 400)
    ycoordinate = rand.randint(200, 400)

    coordinate = [xcoordinate, ycoordinate]
    
    def check():
        for numOfCoords in range(len(topTakenCoords)):
            takenXValues.append(topTakenCoords[numOfCoords][0])
            takenYValues.append(topTakenCoords[numOfCoords][1])
    differenceXValues = [abs(xvalues - coordinate[0]) for xvalues in takenXValues]
    differenceYValues = [abs(yvalues - coordinate[1]) for yvalues in takenYValues]

    

    if all(value < distBtwBarnacles for value in differenceXValues):
        coordinate[0] = rand.randint(200, 400)
        check()
    else:
        pass
    
    if all(value < distBtwBarnacles for value in differenceYValues):
        coordinate[1] = rand.randint(200, 400)
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

# Create bottom left barnacles in certain area and record each coordinate and compare to make sure they are not touching at least one barnacle

bottomTakenCoords = []
sizeOfBarnacles = 20
distBtwBarnacles = sizeOfBarnacles*2
numOfTakenCoords = 0
takenXValues = []
takenYValues = []

for i in range(numOfBarnacles):

    differenceXValues = []
    differenceYValues = []

    xcoordinate = rand.randint(-400, -200)
    ycoordinate = rand.randint(-400, -200)

    coordinate = [xcoordinate, ycoordinate]
    
    def check():
        for numOfCoords in range(len(bottomTakenCoords)):
            takenXValues.append(bottomTakenCoords[numOfCoords][0])
            takenYValues.append(bottomTakenCoords[numOfCoords][1])
    differenceXValues = [abs(xvalues - coordinate[0]) for xvalues in takenXValues]
    differenceYValues = [abs(yvalues - coordinate[1]) for yvalues in takenYValues]

    

    if all(value < distBtwBarnacles for value in differenceXValues):
        coordinate[0] = rand.randint(-400, -200)
        check()
    else:
        pass
    
    if all(value < distBtwBarnacles for value in differenceYValues):
        coordinate[1] = rand.randint(-400, -200)
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

# Pick barnacle coordinate on random and create bubble there

bubble = Turtle()
bubble.speed('slowest')

wn.tracer(0)

while True:
    for numOfCoordinates in range(len(barnacleCoords)):
        bubbleSize = rand.randint(5, 10)

        indexNum = rand.randint(0, ((numOfBarnacles*2) - 1))

        def airBubble(bubble):  
        
            bubble.fillcolor('medium turquoise')  
            bubble.begin_fill()  
            bubble.circle(bubbleSize)
            bubble.end_fill()  

        bubble.color('light sea green')  
        bubble.speed(0)  
        bubble.width(2)  
        bubble.hideturtle()  
  
        bubble.penup()  
        bubble.goto(barnacleCoords[indexNum][0], barnacleCoords[indexNum][1])  
        bubble.pendown() 
        bubble.speed('slowest')

        while bubble.ycor() < 450:  

            bubble.clear()  
            airBubble(bubble) 
            bubble.setheading(90)
            wn.update()  
            bubble.forward(5)
        
        bubble.clear()
