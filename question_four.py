# Python3 implementation of above approach

# returns the minimum cost in a vector( if
# there are multiple goal states)
def uniform_cost_search(goal, start):
    # minimum cost upto
    # goal state from starting
    global graph, cost
    answer = []

    # create a priority queue
    queue = []

    # set the answer vector to max value
    for i in range(len(goal)):
        answer.append(10 ** 10)

    # insert the starting index
    queue.append([0, start])

    # map to store visited node
    visited = {}

    # count
    count = 0
    # path
    path=[]
    # while the queue is not empty
    while (len(queue) > 0):

        # get the top element of the
        queue = sorted(queue)
        p = queue[-1]

        # pop the element
        del queue[-1]

        # get the original value
        p[0] *= -1

        # check if the element is part of
        # the goal list
        if (p[1] in goal):

            # get the position
            index = goal.index(p[1])

            # if a new goal is reached
            if (answer[index] == 10 ** 10):
                count += 1

            # if the cost is less
            if (answer[index] > p[0]):
                answer[index] = p[0]

            # pop the element
            del queue[-1]

            # appending nodes in the path
            path.append(p[1])

            queue = sorted(queue)
            if (count == len(goal)):
                print("called")
                return path

        # check for the non visited nodes
        # which are adjacent to present node
        # print("visited: ",visited)
        if p[1] not in visited:

            # appending nodes in the path
            path.append(p[1])
            for i in range(len(graph[p[1]])):
                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        # mark as visited
        visited[p[1]] = 1

    return path


encoding=["SportComplex","Siwaka","Ph.1A",
          "Ph.1B","Phase2","STC","ParkingLot"
          ,"J1","Phase3","Mada"]


def decoder(value):
    return encoding[value]


# main function
if __name__ == '__main__':
    # create the graph
    graph, cost = [[] for i in range(10)], {}

    # add edge
    graph[0].append(1) # SportComplex->Siwaka
    graph[1].append(2) # Siwaka->Ph.1A
    graph[2].append(9) # Ph.1A->Mada
    graph[2].append(3) # Ph.1A->Ph.1B
    graph[3].append(4) # Ph.1B->Phase2
    graph[3].append(5) # Ph.1B->STC
    graph[4].append(7) # Phase2->J1
    graph[4].append(8) # Phase2->Phase3
    graph[4].append(5) # Phase2->STC
    graph[5].append(6) # STC->ParkingLot
    graph[7].append(9) # J1->Mada
    graph[8].append(6) # Phase3->ParkingLot
    graph[6].append(9) # ParkingLot->Mada


    # add the cost
    cost[(0, 1)] = 450
    cost[(1, 2)] = 10
    cost[(2, 9)] = 850
    cost[(2, 3)] = 100
    cost[(3, 4)] = 112
    cost[(3, 5)] = 50
    cost[(4, 7)] = 600
    cost[(4, 8)] = 500
    cost[(4, 5)] = 50
    cost[(5, 6)] = 250
    cost[(7, 9)] = 200
    cost[(8, 6)] = 350
    cost[(6, 9)] = 700

    # goal state
    goal = []

    # set the goal
    # there can be multiple goal states
    goal.append(6)

    # get the answer
    answer = uniform_cost_search(goal, 0)

    # print the answer
    print("Minimum cost from 0 to 6 is = ", answer)
    print("Graph: ",graph)

