"""
node.py

Module for defining a graph node and its contents.
"""


class Node(object):
    """ Class for defining a graph node and its contents. """

    def __init__(self, x_coord, y_coord, value="."):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.value = value

    def __str__(self):
        x_coord = "x_coord: %d" % self.x_coord
        y_coord = "y_coord: %d" % self.y_coord
        value = "value: %s" % self.value

        result = "%s, %s, %s" % (x_coord, y_coord, value)

        return result

    def draw(self):
        """ Draws a node's value. """

        return self.value

    def passable(self):
        """ Determines if a node is passable. """

        return self.value != "#"
