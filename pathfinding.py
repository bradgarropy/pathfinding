"""
pathfinding.py

Module which implements multiple pathfinding algorithms.
"""

import Queue
import grid as g


def a_star(grid, start, end):
    """ Uses the A* algorithm to find a path from start to end. """

    frontier = Queue.PriorityQueue()
    parent = {}
    cost = {}

    # initialize start node's values
    frontier.put(start, 0)
    parent[start] = None
    cost[start] = 0

    while not frontier.empty():
        # pick the top priority node in the frontier
        current = frontier.get()

        # exit if end is found
        if current == end:
            break

        # explore the current node's neighbors
        for neighbor in grid.neighbors(current):

            # only consider the node if it is passable
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
                    frontier.put(neighbor, priority)

    # initialize the path with the end node
    path = [end]

    # construct the path based off the parents dictionary
    current = end
    while current != start:
        current = parent[current]
        path.append(current)

    # reverse the path to go from start to end
    path.reverse()

    return path
