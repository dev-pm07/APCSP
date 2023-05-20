import turtle as trtl
import random as rand
 
wn = trtl.Screen()

def constructPoly(side, len, xcoord, ycoord):

    trtl.pu()
    trtl.goto(xcoord, ycoord)

    angle = 180 - ( ( 180 * side - 360 ) / side ) 

    trtl.pd()

    for i in range(side):
        trtl.forward(len)
        trtl.right(angle)

polygons = []

numOfPoly = int(input("How many polygons would you like to draw?\t"))

for num in range(numOfPoly):

    side = int(input(str(num + 1) + ". How many sides would you like this polygon to have?\t"))

    while side > 25 or side < 3:
        side = input(str(num + 1) + ". Please input a number between 3 and 25. How many sides would you like this polygon to have?\t")

    len = int(input(str(num + 1) + ". How long would you like each side to be?\t"))

    while len > 200 or len < 1:
        len = input(str(num + 1) + ". Please input a number between 1 and 200. How long would you like each side to be?\t")

    polygons.append([side, len])

for shape in polygons:
    x = rand.randint(0, 300) 
    y = rand.randint(0, 300)
    constructPoly(shape[0], shape[1], x, y)

wn.mainloop()