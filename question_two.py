from queue import PriorityQueue

v = 10
graph = [[] for i in range(v)]


# Function For Implementing Best First Search
# Gives output path having lowest cost

encoding=["SportComplex","Siwaka","Ph.1A",
          "Ph.1B","Phase2","STC","ParkingLot"
          ,"J1","Phase3","Mada"]

def decoder(value):
    return encoding[value]

def best_first_search(source, target, n):
    visited = [0] * n
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(decoder(u))

        if u == target:
            break
        #print("graph: ", graph[u])

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()


# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    # graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers add_edge(x,y,cost);

addedge(0,1,405)  #SportComplex->Siwaka
addedge(1,2,380)  #Siwaka->Ph.1A
addedge(2,9,630)  #Ph.1A->Mada
addedge(2,3,280)  #Ph.1A->Ph.1B
addedge(3,4,210)  #Ph.1B->Phase2
addedge(3,5,213)  #Ph.1B->STC
addedge(4,7,500)  #Phase2->J1
addedge(4,8,160)  #Phase2->Phase3
addedge(5,7,210)  #STC->Phase2
addedge(5,8,0)  #STC->ParkingLot
addedge(7,9,630)  #J1->Mada
addedge(8,6,0)  #Phase3->ParkingLot
addedge(6,9,630)  #ParkingLot->Mada
# print(graph ,end=" \n ")
source = 0
target = 6
best_first_search(source, target, v)

# This code is contributed by Jyotheeswar Ganne
