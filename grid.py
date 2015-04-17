"""
grid.py

Module for creating and manipulating two dimensional grids.
"""

import node as n
import math


class Grid(object):
    """Class for creating and manipulating two dimensional grids."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = {}

        # create a node object for every point on the grid
        for row in range(self.height):
            for column in range(self.width):
                new_node = n.Node(column, row)
                self.nodes[(column, row)] = new_node

    def in_bounds(self, coords):
        """ Determines if a point is in bounds. """

        # determine x and y coordinate values
        x_coord = coords[0]
        y_coord = coords[1]

        # ensure both x and y coordinates are in bounds
        within_width = (0 <= x_coord < self.width)
        within_height = (0 <= y_coord < self.height)

        # calculate the result
        result = within_width and within_height

        return result

    def neighbors(self, coords):
        """ Lists the neighbors for a given point. """

        neighbors = []

        # determine x and y coordinate values
        x_coord = coords[0]
        y_coord = coords[1]

        # gather all possible neighbor coordinates
        top = (x_coord, y_coord - 1)
        bottom = (x_coord, y_coord + 1)
        left = (x_coord - 1, y_coord)
        right = (x_coord + 1, y_coord)

        # add all possible neighbor coordinates to list
        neighbors.append(top)
        neighbors.append(bottom)
        neighbors.append(left)
        neighbors.append(right)

        # remove out of bounds coordinates
        neighbors = [coord for coord in neighbors if self.in_bounds(coord)]

        return neighbors

    def draw(self):
        """ Draws the grid and its node values. """

        for row in range(self.height):
            for column in range(self.width):
                print self.nodes[(column, row)].value,
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
                        self.nodes[(column, row)].value = "#"

        # if obstacles argument is provided
        if obstacles is not None:
            for obstacle in obstacles:
                x_coord = obstacle[0]
                y_coord = obstacle[1]

                self.nodes[(x_coord, y_coord)].value = "#"

    def remove_obstacles(self, obstacles=None):
        """ Removes obstacles from the grid. """

        # if obstacles argument is provided
        if obstacles is not None:
            for obstacle in obstacles:
                x_coord = obstacle[0]
                y_coord = obstacle[1]

                self.nodes[(x_coord, y_coord)].value = 0
        else:
            # if no argument is provided, remove all obstacles
            for row in range(self.height):
                for column in range(self.width):
                    if not self.nodes[(column, row)].passable():
                        self.nodes[(column, row)].value = 0


def distance(start_coords, end_coords):
    """ Calculates the distance to a particular Node. """

    # determine the start x and y coordinate values
    x_start = start_coords[0]
    y_start = start_coords[1]

    # determine the end x and y coordinate values
    x_end = end_coords[0]
    y_end = end_coords[1]

    # calculate the distance along each axis
    x_dist = abs(x_start - x_end)
    y_dist = abs(y_start - y_end)

    # calculate the total distance using the Pythagorean Theorem
    result = math.sqrt(x_dist**2 + y_dist**2)

    return result
