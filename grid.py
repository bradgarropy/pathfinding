"""
grid.py

Module for creating and manipulating two dimensional grids.

    create_grid(width, height)
        Creates and initializes a grid of the provided length and width.

    draw_grid(grid)
        Prints the given grid and its values to standard out.

    add_obstacles(grid, density)
        Adds impassable obstacles to the grid.
"""

__version__ = "0.0.1"


class Grid(object):
    """Class for creating and manipulating two dimensional grids."""

    def __init__(self, width, height):
        self.width = width
        self.height = height


def create_grid(width, height):
    """
    Creates and initializes a grid of the provided length and width.

    Arguments:
    width  -- Width of the grid
    height -- Height of the grid

    Returns:
    grid -- A list of lists representing a grid with all values are initialized
            to zero.

    The grid can be accessed by using the following notation:

        grid[x][y]
    """

    # create a two dimensional list of lists initialized to zero
    grid = [[0 for _ in range(width)] for _ in range(height)]

    return grid


def draw_grid(grid):
    """
    Prints the given grid and its values to standard out.

    Arguments:
    grid -- A list of lists representing a grid

    Returns:
    None
    """

    # calculate the width and height of the grid
    width = len(grid[0])
    height = len(grid)

    # print top bar
    print "----" * width + "-"

    # iterate over rows and columns
    for row in range(height):
        for column in range(width):
            print("| %d" % grid[row][column]),
        print "|"

        # print row separator unless it's the last row
        if row != (height - 1):
            print "|---" * width + "|"

    # print bottom bar
    print "----" * width + "-"


def add_obstacles(grid, density):
    """
    Adds impassable obstacles to the grid.

    Arguments:
    grid    -- A list of lists representing a grid
    density -- Integer between 0 and 100 representing the percent of grid
               spaces to be marked as obstacles.

    Returns:
    grid -- The provided grid with some spaces marked as obstacles based on the
            density percentage. Obstacles in the grid are denoted by a '1'.

    This function only adds obstacles based on the density, it does not reset
    the obstacle density of a grid.
    """

    import random

    # calculate the width and height of the grid
    width = len(grid[0])
    height = len(grid)

    # iterate over rows and columns
    for row in range(height):
        for column in range(width):

            # if randomly generated number is within the density percentage,
            # set the grid space to '1' to indicate an obstacle
            if random.randint(0, 100) < density:
                grid[row][column] = 1
                print "changed grid[%d][%d] to 1" % (row, column)

    return grid
