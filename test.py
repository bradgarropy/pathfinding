"""
test.py

Test module for the pathfinding algorithms.
"""

import random

# import modules to test
import pathfinding as pf
import grid as g

print "Input a width and height for the grid."
print "Alternatively, just press <Enter> for random values.\n"

# take user input for width and height
width = raw_input("width: ")
height = raw_input("height: ")

# select a random width and height if none were input
if not width:
    width = random.randint(1, 75)
else:
    width = int(width)
if not height:
    height = random.randint(1, 75)
else:
    height = int(height)

print "\nDimensions: %d x %d" % (width, height)

# create a grid
grid = g.Grid(width, height)

print
grid.draw()
print

print "Input a wall density for the grid."
print "Alternatively, just press <Enter> for a random value.\n"

# take user input for wall density
density = raw_input("wall density: ")

# select a random wall density if one was not provided
if not density:
    density = random.randint(0, 100)
else:
    density = int(density)

print "\nWall Density: %d" % density

# add walls to the grid
grid.add_obstacles(density)

print
grid.draw()
print

print "Input start and end coordinates for pathfinding."
print "Alternatively, just press <Enter> for random values.\n"

# take user input for width and height
start_x = raw_input("starting x: ")
start_y = raw_input("starting y: ")
end_x = raw_input("ending x: ")
end_y = raw_input("ending y: ")

# select random start and end coordinates if none were input
if not start_x and not start_y:
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
else:
    start_x = int(start_x)
    start_y = int(start_y)
if not end_x and not end_y:
    end_x = random.randint(0, width - 1)
    end_y = random.randint(0, height - 1)
else:
    end_x = int(end_x)
    end_y = int(end_y)

# construct the start and end coordinates
start = (start_x, start_y)
end = (end_x, end_y)

print "\nStart: %s" % str(start)
print "End: %s" % str(end)

# mark the start and end nodes on the grid
grid.nodes[start].value = "0"
grid.nodes[end].value = "X"

print
grid.draw()
print

# use A* to find the path
path = pf.a_star(grid, start, end)

# print the path and the node values
for coord in path:
    print grid.nodes[coord]

# mark the path on the grid
for coord in path:
    if (coord != start) and (coord != end):
        grid.nodes[coord].value = "+"

print
grid.draw()
print
