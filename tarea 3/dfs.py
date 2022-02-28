import numpy as np
matriz = [[0,1,1,0,1,0,0,0,0],[0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0],[0,0,0,0,1,0,0,1,0],[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,1],[0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0]]
matriz = np.array(matriz)
matriz2 = np.zeros((9,9))
print(matriz)
marcados = []
dimension = 9
nodos = []
for i in range(dimension):
    nodos.append(i)
print(nodos)

nodos=[0]
nodo = nodos[0]
while set(nodos) != set([]):
    indices = np.where(matriz[nodo] == 1)
    x = indices[0]
    print(x)
    if set(x) != set([]):
        for item in range(dimension):
            matriz[item][x[0]] = 0
        matriz2[nodo][x[0]] = 1
        nodo = x[0]
        print(nodo)
        if nodo not in nodos:
            nodos.append(nodo)
    else:
        if nodo in nodos:
            nodos.remove(nodo)
        else:
            nodo = nodos[0]   
    print(nodos)
print(matriz2)      

for fila in range(len(matriz2)):
    for columna in range(len(matriz2[0])):
        if matriz2[fila][columna]:
            print(fila,columna)
