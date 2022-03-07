import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')
G.add_node('f')
# G.add_node('g')
# ejemplo 1 no dirigido
# elist = [('a', 'b', 2), ('a', 'c', 4), ('b', 'a', 2), ('b', 'c', 3), ('b', 'd', 8), ('c', 'a', 4), ('c', 'b', 3), ('c', 'e', 5), ('c', 'd', 2), ('d', 'b', 8), ('d', 'c', 2), ('d', 'e', 11), ('d', 'f', 22), ('e', 'c', 5), ('e', 'd', 11), ('e', 'f', 1), ('f', 'd', 22), ('f', 'e', 1)]
# ejemplo 2 no dirigido
# elist = [('a', 'b', 2), ('a', 'c', 5), ('a', 'd', 4), ('b', 'a', 2), ('b', 'c', 2), ('b', 'e', 7), ('c', 'a', 5), ('c', 'b', 2), ('c', 'd', 1), ('c', 'e', 4), ('c', 'f', 3), ('d', 'a', 4), ('d', 'c', 1), ('d', 'f', 4), ('e', 'b', 7), ('e', 'c', 4), ('e', 'f', 1), ('e', 'g', 5), ('f', 'c', 3), ('f', 'd', 4), ('f', 'e', 1), ('f', 'g', 7), ('g', 'e', 5), ('g', 'f', 7)]
# ejemplo 3 dirigido
# elist = [('a', 'b', 1), ('a', 'c', 2), ('a', 'd', 1), ('b', 'c', 2), ('b', 'e', 1), ('c', 'd', 1), ('c', 'e', 2), ('c', 'f', 2), ('d', 'f', 5), ('e', 'f', 3), ('e', 'g', 1), ('f', 'g', 4)]
# ejemplo 4 negativo no dirigido
# elist = [('a', 'b', 2), ('a', 'c',-4), ('b', 'a', 2), ('b', 'c', 3), ('b', 'd', 8), ('c', 'a', -4), ('c', 'b', 3), ('c', 'e', 5), ('c', 'd', 2), ('d', 'b', 8), ('d', 'c', 2), ('d', 'e', 11), ('d', 'f', -22), ('e', 'c', 5), ('e', 'd', 11), ('e', 'f', 1), ('f', 'd', -22), ('f', 'e', 1)]
# ejemplo 5 negativo no dirigido
# elist = [('a', 'b', 2), ('a', 'c', -5), ('a', 'd', 4), ('b', 'a', 2), ('b', 'c', 2), ('b', 'e', -7), ('c', 'a', -5), ('c', 'b', 2), ('c', 'd', 1), ('c', 'e', 4), ('c', 'f', 3), ('d', 'a', 4), ('d', 'c', 1), ('d', 'f', 4), ('e', 'b', -7), ('e', 'c', 4), ('e', 'f', 1), ('e', 'g', 5), ('f', 'c', 3), ('f', 'd', 4), ('f', 'e', 1), ('f', 'g', 7), ('g', 'e', 5), ('g', 'f', 7)]
# ejemplo 6 negativo bellman ford
# elist = [('a', 'b', 1), ('a', 'c', -2), ('a', 'd', 1), ('b', 'c', 2), ('b', 'e', 1), ('c', 'd', 1), ('c', 'e', -2), ('c', 'f', 2), ('d', 'f', 5), ('e', 'f', 3), ('e', 'g', 1), ('f', 'g', 4)]
# ejemplo 7 negativo bellman ford
elist = [('a', 'b', 1), ('a', 'c', 2), ('a', 'd', 1), ('b', 'c', 2), ('b', 'e', 1), ('c', 'd', 1),
         ('c', 'e', -2), ('c', 'f', 2), ('d', 'f', -5), ('e', 'f', 3), ('e', 'g', 1), ('f', 'g', 4)]

G.add_weighted_edges_from(elist)
# G.add_edge('A', 'B', weight=1)
# G.add_edge('A', 'C', weight=2)
# G.add_edge('A', 'D', weight=1)
# G.add_edge('B', 'C', weight=1)
# G.add_edge('B', 'E', weight=2)
# G.add_edge('C', 'E', weight=2)
# G.add_edge('C', 'F', weight=2)
# G.add_edge('C', 'D', weight=1)
# G.add_edge('D', 'F', weight=10)
# G.add_edge('E', 'F', weight=25)
# G.add_edge('E', 'G', weight=14)
# G.add_edge('F', 'G', weight=4)


options = {
    'node_color': 'blue',
    'node_size': 500,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 10,
}
# pos = nx.get_node_attributes(G,'pos')
# cambiar planar por circular o random
pos = nx.circular_layout(G, center=None, dim=2)
# valores de los caminos
labels = nx.get_edge_attributes(G, 'weight')
# dibujar caminos y nodos
# TODO pone los nombres de los nodos.
nx.draw_networkx(G, pos, arrows=True, **options, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# FIXME no dibuja los edges directed
# x = nx.dijkstra_path(G, 'a', 'g', weight='weight')
y = nx.bellman_ford_path(G, 'a', 'g', weight='weight')
# print("Resultado en base a algoritmo dijkstra: ",x)
print("Resultado en base a algoritmo bellman ford: ", y)
# Guardar la imagen en formato eps no admite jpg
plt.savefig("ejemplo7.eps")
