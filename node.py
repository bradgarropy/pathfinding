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

    def distance(self, coords):
        """ Calculates the distance to a particular point. """

        x_dest = coords[0]
        y_dest = coords[1]

        distance = abs(self.x_coord - x_dest) + abs(self.y_coord - y_dest)

        return distance
