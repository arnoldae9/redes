import sys
from heapq import heapify, heappush, heappop
def dijsktra(grafo,ini,fin):
    inf = sys.maxsize
    etiquetas = {   'a' : {'costo' : inf, 'pred' : []},
                'b' : {'costo' : inf, 'pred' : []},
                'c' : {'costo' : inf, 'pred' : []},
                'd' : {'costo' : inf, 'pred' : []},
                'e' : {'costo' : inf, 'pred' : []},
                'f' : {'costo' : inf, 'pred' : []},
    }
    etiquetas[inicio]['costo'] = 0
    visitados = []
    temporal = ini
    for i in range(5):
        if temporal not in visitados:
            visitados.append(temporal)
            min_heap = []
            for j in grafo[temporal]:
                if j not in visitados:
                    costo = etiquetas[temporal]['costo'] + grafo[temporal][j]
                    if costo < etiquetas[j]['costo']:
                        etiquetas[j]['costo'] = costo
                        etiquetas[j]['pred'] = etiquetas[temporal]['pred'] + list(temporal)
                    heappush(min_heap, (etiquetas[j]['costo'],j) )
                    print(min_heap)
        heapify(min_heap)
        temporal = min_heap[0][1]
        print(temporal)
    print("Shortest distance " + str(etiquetas[fin]['costo']))
    print("Shortest Path: " + str(etiquetas[fin]['pred'] + list(fin)))
if __name__ == "__main__":
    grafo = { 'a' : {'b':2,'c':4},
            'b' : {'a':2,'c':3, 'd':8},
            'c' : {'a':4,'b':3, 'e': 5, 'd':2},
            'd' : {'b':8,'c':2,'e':11,'f':22},
            'e' : {'c':5,'d':11,'f':1},
            'f' : {'d':22,'e':1}
    }
    inicio = 'a'
    final = 'f'
    dijsktra(grafo,inicio,final)