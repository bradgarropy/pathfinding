"""
test.py

Test module for the pathfinding algorithms.
"""

import random

# import modules to test
import pathfinding as pf
import grid as g

# select a random width and height
width = random.randint(1, 75)
height = random.randint(1, 75)

print "Dimensions: %d x %d" % (width, height)

# create a grid using the random dimensions
grid = g.Grid(width, height)

print
grid.draw()
print

# select random start coordinates
start_x = random.randint(0, width - 1)
start_y = random.randint(0, height - 1)
start = (start_x, start_y)

print "Start: %s" % str(start)

# select random end coordinates
end_x = random.randint(0, width - 1)
end_y = random.randint(0, height - 1)
end = (end_x, end_y)

print "End: %s" % str(end)

# mark the start and end nodes on the grid
grid.nodes[start].value = "0"
grid.nodes[end].value = "X"

print
grid.draw()
print
