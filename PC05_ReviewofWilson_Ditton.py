"""
Created on Mon Sep 14 14:26:17 2020

@author: Brice Wilson
Reviewed by: Larry Ditton (shankLarry)

This is a generative art piece that uses a the Python Turtle library
to create a turtle that makes shapes of various colors. The piece is designed
to become a background for the teleconferencing app Zoom.
"""

import turtle


#Color variables
black = [0, 0, 0]
blueGreen = [160, 234, 222]
chromeYellow = [250, 169, 22]
violet = [141, 107, 148]
redCrayola = [255, 16, 83]


#Variables for number of iterations to do/shape
numCircles = range(36)
numTris = range (4)
triangleSides = range(3)
hexagonSides = range(6)
squareSides = range(4)


#Variables for sizing and positioning of shapes
radius = 18
triSize = 150 #length of triangle sides
hexSize = 100 #length of hexagon sides
squareSize = 120 #length of square sides
circleTravel = 10 #amount turtle moves forward while making circle ring
circAngle = 10 #angle turtle moves to make circle ring
triAngle = 120 #angle turtle makes to make triangle
hexAngle = 60 #angle turtle makes to make hexagon
squareAngle = 90


#Location Variables
circLoc = [450,150]
triLoc = [100,25]
hexLoc = [110, 400]
squareLoc = [400,425]
outlineLoc = [-3,-3]


#Turtle setup
panel = turtle.Screen()
panel.colormode(255)
w = 600 
h = 600 
panel.setup(width=w, height=h) 
panel.setworldcoordinates(0, w, h, 0)
panel.bgcolor(black)

shapeTurt = turtle.Turtle() #Create a turtle that makes various shapes!
shapeTurt.speed(0)
shapeTurt.up()


#Make a circle of smaller circles:
shapeTurt.goto(circLoc)
shapeTurt.down()
shapeTurt.color(blueGreen)

for circles in numCircles:  #Makes a ring of circles
    
    shapeTurt.circle(radius)
    shapeTurt.forward(circleTravel)
    shapeTurt.right(circAngle)

shapeTurt.up()

    
#Make a filled triangle:
shapeTurt.goto(triLoc)
shapeTurt.down()
shapeTurt.color(chromeYellow)
shapeTurt.begin_fill()

for element in triangleSides:   #Draws a triangle
    
    shapeTurt.forward(triSize)
    shapeTurt.left(triAngle) 
    
shapeTurt.end_fill()
shapeTurt.up()


#Make a filled hexagon:
shapeTurt.goto(hexLoc)
shapeTurt.down()
shapeTurt.color(violet)
shapeTurt.begin_fill()

for element in hexagonSides:    #Draws a hexagon
    
    shapeTurt.forward(hexSize)
    shapeTurt.left(hexAngle)

shapeTurt.end_fill()
shapeTurt.up()


#Make a filled square:
shapeTurt.goto(squareLoc)
shapeTurt.down()
shapeTurt.color(redCrayola)
shapeTurt.begin_fill()

for element in squareSides: #draws a square
    
    shapeTurt.forward(squareSize)
    shapeTurt.left(squareAngle)

shapeTurt.end_fill()
shapeTurt.up()


#Make a square outline around all the shapes
shapeTurt.width(4)
shapeTurt.color('white')
shapeTurt.goto(outlineLoc)
shapeTurt.setheading(90)
shapeTurt.down()
for element in squareSides:
    
    shapeTurt.forward(w)
    shapeTurt.right(squareAngle)


shapeTurt.hideturtle()
turtle.done()


"""
Summary Review:
    Overall, Brice’s code was decently organized and straightforward making it 
easy for somebody to quickly grasp what the code did and get up to speed with
his program. Most of the changes I made were designed to help further those
strengths to make editing in the future faster. First I placed all the 
variables at the top, including the variables for the number of iterations for 
each for loop. I added variables for the sizing of the shapes, the 
locations of the shapes, and the colors as well. This allows Brice 
(or somebody else) in the future to quickly change those values should they 
need to (and lessens the amount of “hard-coding” in the program). I broke up 
the body of the code using spaces and then added comments as to what those 
subsections do to help aid in readability and to quickly see which part of the 
code does what. 
    I really liked Brice’s code. Right away the circle of circles is cool. He 
definitely has a good grasp on for-loops and I liked the shapes and colors he 
chose for his artwork. 
    

Upgrade extra credit: I talked to Brice and asked him what he would have liked 
to do to upgrade his code, and he said he wanted to add a box around all of 
the shapes. So I used a for-loop to add that, and improved the symmetry of the 
shapes as well so they all fit. 
"""
