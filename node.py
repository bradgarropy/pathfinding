"""
node.py

Module for defining a graph node and its contents.
"""


class Node(object):
    """ Class for defining a graph node."""

    def __init__(self, x_coord, y_coord, value):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.value = value
