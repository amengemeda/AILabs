# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

from matplotlib.pyplot import figimage, figure


class Draw:
    def __init__(self):
        figure(figsize=(10, 10), dpi=80)

        self.g = nx.Graph()

        self.g.add_node("SportsComplex", pos=(-8, 12))
        self.g.add_node("Siwaka", pos=(-5, 18))
        self.g.add_node("Ph.1A", pos=(6, 18))
        self.g.add_node("Ph.1B", pos=(5, 12))
        self.g.add_node("Phase2", pos=(16, 12))
        self.g.add_node("J1", pos=(26, 12))
        self.g.add_node("Mada", pos=(36, 12))
        self.g.add_node("STC", pos=(6, 6))
        self.g.add_node("Phase3", pos=(12, 6))
        self.g.add_node("ParkingLot", pos=(12, 0))

        self.g.add_edge("SportsComplex", "Siwaka", weight=450, label="UnkRoad")
        self.g.add_edge("Siwaka", "Ph.1A", weight=10, label="SangaleRd")
        self.g.add_edge("Siwaka", "Ph.1B", weight=230, label="SangaleLink")
        self.g.add_edge("Ph.1A", "Mada", weight=850, label="SangaleRd")
        self.g.add_edge("Ph.1A", "Ph.1B", weight=100, label="ParkingWalkWay")
        self.g.add_edge("Ph.1B", "Phase2", weight=112, label="KeriRd")
        self.g.add_edge("Ph.1B", "STC", weight=50, label="KeriRd")
        self.g.add_edge("Phase2", "J1", weight=600, label="KeriRd")
        self.g.add_edge("Phase2", "STC", weight=50, label="STCwalkway")
        self.g.add_edge("Phase2", "Phase3", weight=500, label="KeriRd")
        self.g.add_edge("J1", "Mada", weight=200, label="SangaleRd")
        self.g.add_edge("Mada", "ParkingLot", weight=700, label="langataRd")
        self.g.add_edge("STC", "ParkingLot", weight=250, label="LibraryWalkWay")
        self.g.add_edge("Phase3", "ParkingLot", weight=350, label="HimaGardensRd")

    def get_graph(self):
        return self.g

    def color(self, solution):
        color_map = []
        for node in self.g.nodes():
            if(node in solution):
                color_map.append("pink")
            else:
                color_map.append("lightblue")
        return color_map

    def draw_graph(self, solution, figname):
        pos = nx.get_node_attributes(self.g, 'pos')
        nx.draw(self.g, pos, with_labels=1)

        labels = nx.get_edge_attributes(self.g, 'label')
        weights = nx.get_edge_attributes(self.g, 'weight')

        node_col = self.color(solution);

        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=labels, label_pos=0.6)
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=weights, label_pos=0.3)
        nx.draw_networkx(self.g, pos, node_color=node_col, node_size=[len(v) * 700 for v in self.g.nodes()])

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")

        plt.savefig(figname)
        plt.plot()
        plt.show()
