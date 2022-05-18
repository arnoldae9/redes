import networkx as nx

G = nx.DiGraph()
G.add_edge("x", "a",capacity=3.0)
G.add_edge("x", "b",capacity=1.0)
G.add_edge("a", "c",capacity=3.0)
G.add_edge("b", "c",capacity=5.0)
G.add_edge("b", "d",capacity=4.0)
G.add_edge("d", "e",capacity=2.0)
G.add_edge("c", "y",capacity=2.0)
G.add_edge("e", "y",capacity=3.0)

cut_value, partition = nx.minimum_cut(G, "x", "y")
reachable, non_reachable = partition

cutset = set()

for u, nbrs in ((n, G[n]) for n in reachable):
    cutset.update((u, v) for v in nbrs if v in non_reachable)

print("Los arcos a cortar son: ",sorted(cutset))

cut_value = nx.minimum_cut_value(G, "x", "y")

print("El valor del corte mínimo es: ",cut_value)




