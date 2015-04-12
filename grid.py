"""
grid.py

Module for creating and manipulating two dimensional grids.
"""

import node as n


class Grid(object):
    """Class for creating and manipulating two dimensional grids."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = {}

        # create a node object for every point on the grid
        for row in range(self.height):
            for column in range(self.width):
                new_node = n.Node(row, column)
                self.nodes[(row, column)] = new_node

    def in_bounds(self, node):
        """ Determines if a grid node is in bounds. """

        within_width = (0 <= node.x_coord < self.width)
        within_height = (0 <= node.y_coord < self.height)

        return within_width and within_height

    def draw(self):
        """ Draws the grid and its node values. """

        for row in range(self.height):
            for column in range(self.width):
                print self.nodes[(row, column)].value,
            print

    def add_obstacles(self, density=None, obstacles=None):
        """ Add impassable obstacles to the grid. """

        # if density argument is provided
        if density is not None:
            import random

            # determine if each node should be changed to an obstacle
            for row in range(self.height):
                for column in range(self.width):
                    if random.randint(0, 100) < density:
                        self.nodes[(row, column)].value = "W"
                        print "Added obstacle at (%d, %d)" % (row, column)

        # if obstacles argument is provided
        if obstacles is not None:
            for obstacle in obstacles:
                x_coord = obstacle[0]
                y_coord = obstacle[1]

                self.nodes[(x_coord, y_coord)].value = "W"
                print "Added obstacle at (%d, %d)" % (x_coord, y_coord)

    def remove_obstacles(self, obstacles=None):
        """ Removes obstacles from the grid. """

        # if obstacles argument is provided
        if obstacles is not None:
            for obstacle in obstacles:
                x_coord = obstacle[0]
                y_coord = obstacle[1]

                self.nodes[(x_coord, y_coord)].value = 0
                print "Removed obstacle at (%d, %d)" % (x_coord, y_coord)
        else:
            # if no argument is provided, remove all obstacles
            for row in range(self.height):
                for column in range(self.width):
                    if not self.nodes[(row, column)].passable():
                        self.nodes[(row, column)].value = 0
                        print "Removed obstacle at (%d, %d)" % (row, column)
