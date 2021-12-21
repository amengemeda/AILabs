# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure
figure(figsize=(10, 10), dpi=80)

g = nx.Graph()

g.add_node("SportsComplex", pos=(-8, 12))
g.add_node("Siwaka", pos=(-5, 18))
g.add_node("Ph.1A", pos=(6, 18))
g.add_node("Ph.1B", pos=(5, 12))
g.add_node("Phase2", pos=(16, 12))
g.add_node("J1", pos=(26, 12))
g.add_node("Mada", pos=(36, 12))
g.add_node("STC", pos=(6, 6))
g.add_node("Phase3", pos=(12, 6))
g.add_node("ParkingLot", pos=(12, 0))

g.add_edge("SportsComplex", "Siwaka", weight=450, label="UnkRoad")
g.add_edge("Siwaka", "Ph.1A", weight=10, label="SangaleRd")
g.add_edge("Siwaka", "Ph.1B", weight=230, label="SangaleLink")
g.add_edge("Ph.1A", "Mada", weight=850, label="SangaleRd")
g.add_edge("Ph.1A", "Ph.1B", weight=100, label="ParkingWalkWay")
g.add_edge("Ph.1B", "Phase2", weight=112, label="KeriRd")
g.add_edge("Ph.1B", "STC", weight=50, label="KeriRd")
g.add_edge("Phase2", "J1", weight=600, label="KeriRd")
g.add_edge("Phase2", "STC", weight=50, label="STCwalkway")
g.add_edge("Phase2", "Phase3", weight=500, label="KeriRd")
g.add_edge("J1", "Mada", weight=200, label="SangaleRd")
g.add_edge("Mada", "ParkingLot", weight=700, label="langataRd")
g.add_edge("STC", "ParkingLot", weight=250, label="LibraryWalkWay")
g.add_edge("Phase3", "ParkingLot", weight=350, label="HimaGardensRd")


pos = nx.get_node_attributes(g, 'pos')
nx.draw(g, pos, with_labels=1)
#
labels = nx.get_edge_attributes(g, 'label')
weights = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, label_pos=0.6)
nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, label_pos=0.3)
nx.draw_networkx_nodes(g, pos, node_size=[len(v) * 700 for v in g.nodes()],)


