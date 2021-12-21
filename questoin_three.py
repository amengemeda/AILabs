import networkx as nx
from queue import PriorityQueue
import matplotlib.pyplot as plt

v = 10
graph_for_path = [[] for i in range(v)]

nodesList = ["SportComplex", "Siwaka", "Ph.1A", "Ph.1B", "Phase2", "STC", "J1", "Phase3", "ParkingLot", "Mada"]
graph = nx.Graph()
# representing the nodes by integer using their index
encoding = ["SportComplex", "Siwaka", "Ph.1A",
            "Ph.1B", "Phase2", "STC", "ParkingLot",
            "J1", "Phase3", "Mada"]


def decoder(value):
    return encoding[value]


# Function for adding edges to graph
def add_edge(x, y, cost):
    graph_for_path[x].append((y, cost))


def best_first_search(source, target, n, graph_for_path):
    visited = [0] * n
    path = []
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # appending the path having lowest cost into the array
        path.append(u)
        if u == target:
            break

        for a, b in graph_for_path[u]:
            if visited[a] == False:
                visited[a] = True
                pq.put((b, a))
    return path


def get_path():
    add_edge(0, 1, 405)  # SportComplex->Siwaka
    add_edge(1, 2, 380)  # Siwaka->Ph.1A
    add_edge(2, 9, 630)  # Ph.1A->Mada
    add_edge(2, 3, 280)  # Ph.1A->Ph.1B
    add_edge(3, 4, 210)  # Ph.1B->Phase2
    add_edge(3, 5, 213)  # Ph.1B->STC
    add_edge(4, 7, 500)  # Phase2->J1
    add_edge(4, 8, 160)  # Phase2->Phase3
    add_edge(4, 5, 213)  # Phase2->STC
    add_edge(5, 8, 0)  # STC->ParkingLot
    add_edge(7, 9, 630)  # J1->Mada
    add_edge(8, 6, 0)  # Phase3->ParkingLot
    add_edge(6, 9, 630)  # ParkingLot->Mada
    source = 0
    target = 6
    return best_first_search(source, target, v, graph_for_path)


def draw_diagram(nodes, g):
    # adding all the nodes
    g.add_nodes_from(nodes)
    # getting the path with the lowest cost
    shortest_path = get_path()

    # constructing the color map
    color_map = color_nodes(g, shortest_path)

    # adding the edges
    g.add_edge("SportComplex", "Siwaka", weight="450")
    g.add_edge("Siwaka", "Ph.1A", weight="10")
    g.add_edge("Ph.1A", "Mada", weight="850")
    g.add_edge("Ph.1A", "Ph.1B", weight="100")
    g.add_edge("Ph.1B", "Phase2", weight="112")
    g.add_edge("Ph.1B", "STC", weight="50")
    g.add_edge("Phase2", "STC", weight="50")
    g.add_edge("STC", "ParkingLot", weight="250")
    g.add_edge("Phase2", "J1", weight="600")
    g.add_edge("Phase2", "Phase3", weight="500")
    g.add_edge("J1", "Mada", weight="200")
    g.add_edge("Phase3", "ParkingLot", weight="350")
    g.add_edge("ParkingLot", "Mada", weight="700")

    # positioning the nodes
    g.nodes["SportComplex"]['pos'] = (-3, 2)
    g.nodes["Siwaka"]['pos'] = (-2, 2)
    g.nodes["Ph.1A"]['pos'] = (-1, 2)
    g.nodes["Ph.1B"]['pos'] = (-1, 0)
    g.nodes["Phase2"]['pos'] = (0, 0)
    g.nodes["STC"]['pos'] = (-1, -2)
    g.nodes["J1"]['pos'] = (1, 0)
    g.nodes["Phase3"]['pos'] = (1, -2)
    g.nodes["ParkingLot"]['pos'] = (1, -4)
    g.nodes["Mada"]['pos'] = (2, 0)

    node_pos = nx.get_node_attributes(g, 'pos')
    arc_weight = nx.get_edge_attributes(g, 'weight')

    nx.draw_networkx(g, node_pos, with_labels=True, node_color=color_map, node_size=2300, font_size=8)
    nx.draw_networkx_edge_labels(g, node_pos, edge_labels=arc_weight)

    plt.axis('off')
    plt.show()


def color_nodes(g, shortest_path):
    color_map = []
    # decoding node names from integer to strings

    for i in range(0,len(shortest_path),1):
        shortest_path[i] = decoder(shortest_path[i])

    for node in g:
        if node in shortest_path:
            color_map.append('pink')
        else:
            color_map.append('lightblue')
    return color_map


draw_diagram(nodesList, graph)
