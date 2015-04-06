"""
grid.py

Module for creating and manipulating two dimensional grids.

    create_grid(width, height)
        Creates a grid of the given width and height initialized with zeros.

    draw_grid(grid)
        Draws the provided grid.
"""


def create_grid(width, height):
    """
    Creates and initializes a grid of the provided length and width.

    width	-- Width of the grid.
    height	-- Height of the grid.

    Returns a list of lists representing a grid. All values are initialized to
    zero. The grid can be accessed by using the following notation:

        grid[x][y]

    You can visualize the graph as shown below. The origin is at the top left.

    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

    In the example grid shown above, grid[0][0] would return 1.
    """

    # create a two dimensional list of lists initialized to zero
    grid = [[0 for _ in range(width)] for _ in range(height)]

    return grid

# TODO Implement draw_grid(grid)
