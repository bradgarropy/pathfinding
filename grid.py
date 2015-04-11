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

    def add_obstacles(self, density):
        """ Add impassable obstacles to the grid. """

        import random

        # determine if each node should be changed to an obstacle
        for row in range(self.height):
            for column in range(self.width):
                if random.randint(0, 100) < density:
                    self.nodes[(row, column)].value = "W"

    def remove_obstacles(self):
        """ Removes all obstacles from the grid. """

        # TODO: Implement this method.
        pass

    def add_row(self):
        """ Adds a row to the grid. """

        # TODO: Implement this method.
        pass

    def add_column(self):
        """ Adds a column to the grid. """

        # TODO: Implement this method.
        pass

    def remove_row(self):
        """ Removes a row from the grid. """

        # TODO: Implement this method.
        pass

    def remove_column(self):
        """ Removes a column from the grid. """

        # TODO: Implement this method.
        pass
