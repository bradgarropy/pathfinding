"""
a_star.py

Module which implements the A* pathfinding algorithm.
"""

import Queue


def a_star(start, end):
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
        for neighbor in current.neighbors():

            # calculate the cost to reach the neighbor
            new_cost = cost[current] + 1

            # TODO: Cost should handle obstacles

            # add new neighbors or update better neighbors
            if (neighbor not in cost) or (new_cost < cost[neighbor]):

                # add cost and parent information
                cost[neighbor] = new_cost
                parent[neighbor] = current

                # place in appropriate spot in the frontier
                priority = new_cost + neighbor.distance(node=end)
                frontier.put(neighbor, priority)

    return parent
