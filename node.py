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

    def neighbors(self):
        """ Lists a node's neighbors. """

        neighbors = []

        top = (self.x_coord, self.y_coord + 1)
        bottom = (self.x_coord, self.y_coord - 1)
        left = (self.x_coord - 1, self.y_coord)
        right = (self.x_coord + 1, self.y_coord)

        neighbors.append(top)
        neighbors.append(bottom)
        neighbors.append(left)
        neighbors.append(right)

        return neighbors

    def passable(self):
        """ Determines if a node is passable. """

        return self.value != "W"

    def distance(self, coords=None, node=None):
        """ Calculates the distance to a particular point or Node. """

        # handle no argument case
        if coords is None and node is None:
            return 0

        # if coords argument is provided
        if coords is not None:
            x_coord = coords[0]
            y_coord = coords[1]

        # if node argument is provided
        if node is not None:
            x_coord = node.x_coord
            y_coord = node.y_coord

        x_dist = abs(self.x_coord - x_coord)
        y_dist = abs(self.y_coord - y_coord)

        distance = x_dist + y_dist

        return distance
