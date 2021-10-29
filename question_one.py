import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

nodes=["SportComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","J1","Phase3","ParkingLot","Mada"]
# edges=[
#         ("SportComplex","Siwaka"), ("Siwaka","Ph.1A"),
#         ("Siwaka","Ph.1B"),("Ph.1A","Mada"),
#         ("Ph.1A","Ph.1B"), ("Ph.1B","Phase2"),
#         ("Ph.1B","STC"),("STC","Phase2"),("STC","ParkingLot"),
#         ("Phase2","J1"),("Phase2","Phase3"),
#         ("J1", "Mada"), ("Phase3", "ParkingLot"),
#         ("ParkingLot", "Mada"),
#        ]
# g.add_edge("SportComplex", "Siwaka", weight = "")

g= nx.Graph()
g.add_nodes_from(nodes)
g.add_edge("SportComplex","Siwaka",weight="450")
g.add_edge("Siwaka","Ph.1A",weight="10")
g.add_edge("Siwaka","Ph.1A",weight="230")
g.add_edge("Ph.1A","Mada",weight="850")
g.add_edge("Ph.1A","Ph.1B",weight="100")
g.add_edge("Ph.1B","Phase2",weight="112")
g.add_edge("Ph.1B","STC",weight="50")
g.add_edge("STC","Phase2",weight="50")
g.add_edge("STC","ParkingLot",weight="250")
g.add_edge("Phase2","J1",weight="600")
g.add_edge("Phase2","Phase3",weight="500")
g.add_edge("J1","Mada",weight="200")
g.add_edge("Phase3","ParkingLot",weight="350")
g.add_edge("ParkingLot","Mada",weight="700")


# g.add_edges_from(edges,length=50)
# pos = nx.spring_layout(g)


g.nodes["SportComplex"]['pos']=(-3,2)
g.nodes["Siwaka"]['pos']=(-2,2)
g.nodes["Ph.1A"]['pos']=(-1,2)
g.nodes["Ph.1B"]['pos']=(-1,0)
g.nodes["Phase2"]['pos']=(0,0)
g.nodes["STC"]['pos']=(-1,-2)
g.nodes["J1"]['pos']=(1,0)
g.nodes["Phase3"]['pos']=(1,-2)
g.nodes["ParkingLot"]['pos']=(1,-4)
g.nodes["Mada"]['pos']=(2,0)
node_pos = nx.get_node_attributes(g,'pos')
arc_weight=nx.get_edge_attributes(g,'weight')
pos = nx.spring_layout(g, k=0.15, iterations=20)
nx.draw_networkx(g, node_pos,with_labels = True, node_color= 'lightblue', node_size=2300,font_size=8)
nx.draw_networkx_edge_labels(g, node_pos, edge_labels=arc_weight)
# nx.draw(g,with_labels = True,node_size=2000,node_color='pink',font_size=8)
plt.axis('off')
plt.show()