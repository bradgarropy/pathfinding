"""
node.py

Module for defining a graph node and its contents.
"""


class Node(object):
    """ Class for defining a graph node and its contents. """

    def __init__(self, x_coord, y_coord, value=0):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.value = value

    def draw(self):
        """ Draws a node's value. """

        return self.value

    def passable(self):
        """ Determines if a node is passable. """

        return self.value != "W"
