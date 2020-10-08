import networkx as nx
import hashing_algo as hash

G1 = nx.Graph()


G1.add_nodes_from([1,2])

G1.add_edge(1,2)
G1.nodes[1]["label"]={'pid': 1,
                    'sid': 1,
                                            'ppid': 0,
                                            }

G1.nodes[2]["label"]={'pid': 2,
                    'sid': 1,
                                            'ppid': 1,
                                            }

G2 = nx.Graph()
G2.add_nodes_from([1,2])

G2.add_edge(1,2)
G2.nodes[1]["label"]={'pid': 1,
                    'sid': 1,'ppid': 0,
                                            }

G2.nodes[2]["label"]={'pid': 2,
                    'sid': 1, 'ppid': 1,}


G3 = nx.Graph()
G3.add_nodes_from([1,2])

G3.add_edge(1,2)
G3.nodes[1]["label"]={'pid': 1,
                    'sid': 1,'ppid': 0,
                                            }

G3.nodes[2]["label"]={'pid': 20,
                    'sid': 1, 'ppid': 1,}



print(hash.weisfeiler_lehman_graph_hash(G1,node_attr="label"))
print(hash.weisfeiler_lehman_graph_hash(G2,node_attr="label"))
print(hash.weisfeiler_lehman_graph_hash(G3,node_attr="label"))
