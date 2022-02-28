import numpy as np
matriz = [[0,0,1,0,0,0,0,1],[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1],[0,1,0,1,0,1,0,0],[1,1,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,0,0,0]]
matriz = np.array(matriz)
matriz2 = np.zeros((8,8))
# print(matriz2)
dimension = 8
nodos = []
for i in range(dimension):
    nodos.append(i)
print(nodos)
indegree = []

# obtiene los indegree
for item in nodos:
    suma = 0
    for item2 in nodos:
        suma = suma + matriz[item2][item]
    indegree.append(suma)
print(indegree)
indegree = np.array(indegree)
list = []
next = 0

# encuentra los nodos con llegadas cero
for nodo in nodos:
    x = np.where(indegree == 0)

#convertir a lista el ndarray
for item in x[0]:
    list.append(item)
print(list)

#algoritmo
while set(list) != set([]):
    nodo = list[0]
    print(nodo)
    list.remove(list[0])
    next = next + 1
    for item in nodos:
        if matriz[nodo][item] != 0:
            indegree[item] =indegree[item]-1
            if indegree[item] ==0:
                if item not in list:
                    list.append(item)
if next < dimension:
    print("the network constains a directed cycle")
else:
    print("the network is acyclic and the array order gives a topological order of nodes")    
print(indegree) 