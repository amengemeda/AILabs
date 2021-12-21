import heapq
import graph_question_four as main
from classes.Process import Process

def uniformCostSearch(g, start, finish):
    frontier = []
    frontierIndex = {}
    node = (0, start, [start])

    frontierIndex[node[1]] = [node[0], node[2]]
    # Insert the node inside the frontier (queue)
    heapq.heappush(frontier, node)
    explored = set()
    while frontier:
        if len(frontier) == 0:
            return None
        # Pop element with lower path cost in the queue
        node = heapq.heappop(frontier)

        del frontierIndex[node[1]]
        # Check if the solution has been found
        if node[1] == finish:
            return node
        explored.add(node[1])
        # Get a list of all the child nodes of node
        adjacent_nodes = list(g.neighbors(node[1]))
        path = node[2]
        for child in adjacent_nodes:
            path.append(child)
            # create the child node that will be inserted in frontier
            childNode = (node[0] + g.get_edge_data(node[1], child)["weight"], child, path)

            # Check the child node is not explored and not in frontier through the dictionary
            if child not in explored and child not in frontierIndex:
                heapq.heappush(frontier, childNode)
                frontierIndex[child] = [childNode[0], childNode[2]]
            elif child in frontierIndex:
                # Checks if the child node has a lower path cost than the node already in frontier
                if childNode[0] < frontierIndex[child][0]:
                    nodeToRemove = (frontierIndex[child][0], child, frontierIndex[child][1])
                    frontier.remove(nodeToRemove)
                    heapq.heapify(frontier)
                    del frontierIndex[child]

                    heapq.heappush(frontier, childNode)
                    frontierIndex[child] = [childNode[0], childNode[2]]
            path = path[:-1]


finalRoute = uniformCostSearch(main.g, "SportsComplex", "ParkingLot")
print(finalRoute[2])

problem = Process("SportsComplex", "ParkingLot")
problem.graphing.draw_graph(finalRoute[2], "question_four.png")
