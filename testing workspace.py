import turtle as trtl
import math
 
wn = trtl.Screen()

# num = int(input("How many sides would you like this polygon to have?\t"))
# len = int(input("How long would you like each side to be?\t"))

# while num > 500:
#     num = input("How many sides would you like this polygon to have?\t")

# while len > 200 and len < 1:
#     len = input("How long would you like each side to be?\t")

# angle = ( 180 * num - 360 ) / num

for side in range(5):
    trtl.forward(25)
    trtl.right(98)

wn.mainloop()