import turtle as trtl
import random as rand
wn = trtl.Screen()

# Set background color to sea
wn.bgcolor('medium blue') 

trtl.pencolor('crimson')
trtl.penup()
trtl.goto(100, 0)
trtl.pendown()

head = 0
trtl.fillcolor('crimson')
trtl.begin_fill()

# Create Starfish
for i in range(5):
    head = head + 144
    trtl.setheading(head)
    trtl.forward(200)

trtl.end_fill()

topTakenCoords = []
sizeOfBarnacles = 10
numOfBarnacles = 20
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

    trtl.pencolor('gainsboro')
    trtl.fillcolor('gainsboro')

    trtl.penup()
    trtl.goto(coordinate[0], coordinate[1])
    trtl.pendown()

    trtl.begin_fill()
    trtl.circle(10)
    trtl.end_fill()

bottomTakenCoords = []
sizeOfBarnacles = 10
numOfBarnacles = 20
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

    trtl.pencolor('gainsboro')
    trtl.fillcolor('gainsboro')

    trtl.penup()
    trtl.goto(coordinate[0], coordinate[1])
    trtl.pendown()

    trtl.begin_fill()
    trtl.circle(10)
    trtl.end_fill()


wn.tracer(0)
wn.mainloop()