import networkx as nx
import hashing_algo as hash

G1 = nx.Graph()
G1.add_nodes_from([1,2,3,4])
G1.add_edge(1,3)
G1.add_edge(1,2)
G1.add_edge(2,4)
G1.nodes[1]["label"]={'sid_dist': 0}
G1.nodes[2]["label"]={'sid_dist': 1}
G1.nodes[3]["label"]={'sid_dist': 1}
G1.nodes[4]["label"]={'sid_dist': 2}

G2 = nx.Graph()

G2.add_nodes_from([1,2,3,4])
G2.add_edge(1,3)
G2.add_edge(1,2)
G2.add_edge(3,4)
G2.nodes[1]["label"]={'sid_dist': 0}
G2.nodes[2]["label"]={'sid_dist': 1}
G2.nodes[3]["label"]={'sid_dist': 1}
G2.nodes[4]["label"]={'sid_dist': 2}


d1 = hash.weisfeiler_lehman_graph_hash(G1,node_attr="label")
d2 = hash.weisfeiler_lehman_graph_hash(G2,node_attr="label")
print("C =", abs(int(d1,16)-int(d2,16)))




