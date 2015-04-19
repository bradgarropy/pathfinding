"""
pathfinding.py

Module which implements multiple pathfinding algorithms.
"""

import Queue as q
import grid as g


def a_star(grid, start, end):
    """ Uses the A* algorithm to find a path from start to end. """

    frontier = q.PriorityQueue()
    parent = {}
    cost = {}

    # initialize start point's values
    frontier.put((0, start))
    parent[start] = None
    cost[start] = 0

    while not frontier.empty():
        # pick the top priority point in the frontier
        current = frontier.get()[1]

        # exit if end is found
        if current == end:
            break

        # explore the current point's neighbors
        for neighbor in grid.neighbors(current):

            # only consider the point if it is passable
            if grid.nodes[neighbor].passable():

                # calculate the cost to reach the neighbor
                new_cost = cost[current] + 1

                # add new neighbors or update better neighbors
                if (neighbor not in cost) or (new_cost < cost[neighbor]):

                    # add cost and parent information
                    cost[neighbor] = new_cost
                    parent[neighbor] = current

                    # place in appropriate spot in the frontier
                    priority = new_cost + g.distance(neighbor, end)
                    frontier.put((priority, neighbor))

    # initialize the path with the end point
    path = [end]

    # construct the path based off the parents dictionary
    current = end
    while current != start:

        # no path exists if current node does not have a parent
        if current in parent:
            current = parent[current]
            path.append(current)
        else:
            path = []
            break

    # reverse the path to go from start to end
    path.reverse()

    return path
