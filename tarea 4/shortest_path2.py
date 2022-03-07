import sys

def dijsktra(grafo,ini,fin,etiquetas,dimension): #TODO definicion de la funcion dijsktra
    etiquetas[inicio]['costo'] = 0
    visitados = [] 
    temporal = ini
    
    for i in range(dimension):
        if temporal not in visitados:
            visitados.append(temporal)
            print(visitados)
            for j in grafo[temporal]:
                if j not in visitados:
                    costo = etiquetas[temporal]['costo'] + grafo[temporal][j]
                    if costo < etiquetas[j]['costo']:
                        etiquetas[j]['costo'] = costo
                        etiquetas[j]['pred'] = etiquetas[temporal]['pred'] + list(temporal)
        lista = []
        for k in etiquetas.items():
            if k[0] not in visitados:
                lista.append(etiquetas[k[0]]['costo'])
        print(lista)
        aux = []
        for k in etiquetas.items():
            if etiquetas[k[0]]['costo'] == min(lista):
                if k[0] not in visitados:
                    print(k[0])
                    aux.append(k[0])
                    print(aux)
                    temporal = k[0]
    print("Distancia más corta: " + str(etiquetas[fin]['costo'])) #TODO imprime el costo del nodo final
    print("Ruta de la distancia más corta: " + str(etiquetas[fin]['pred'] + list(fin))) #TODO imprime la ruta almacenada en el nodo final
if __name__ == "__main__":
    inf = sys.maxsize
    opcion = int(input("Digite una opcion: "))
    while opcion not in [1,2,3]:  #TODO  si quieres agregar un grafo más aumenta esta lista
        print("opcion incorrecta")
        opcion = int(input("Digite una opcion: "))

    if opcion == 1:  #TODO agregar por elif grafo,etiquetas,inicio,final,dimension
        grafo = {   'a' : {'b':2,'c':4}, 
                    'b' : {'a':2,'c':3, 'd':8},
                    'c' : {'a':4,'b':3, 'e': 5, 'd':2},
                    'd' : {'b':8,'c':2,'e':11,'f':22},
                    'e' : {'c':5,'d':11,'f':1},
                    'f' : {'d':22,'e':1}}
        etiquetas = {   'a' : {'costo' : inf, 'pred' : []},
                    'b' : {'costo' : inf, 'pred' : []},
                    'c' : {'costo' : inf, 'pred' : []},
                    'd' : {'costo' : inf, 'pred' : []},
                    'e' : {'costo' : inf, 'pred' : []},
                    'f' : {'costo' : inf, 'pred' : []}}
        inicio = 'b'
        final = 'f'
        dimension = 5 #TODO la dimensión es nodos - 1
    elif opcion == 2:
        grafo = {   'a' : {'b':2,'c':5, 'd':4},
                    'b' : {'a':2,'c':2, 'e':7},
                    'c' : {'a':5,'b':2, 'd': 1, 'e':4,'f':3},
                    'd' : {'a':4,'c':1,'f':4},
                    'e' : {'b':7,'c':4,'f':1,'g':5},
                    'f' : {'c':3,'d':4,'e':1,'g':7},
                    'g' : {'e':5,'f':7}}
        etiquetas = {   'a' : {'costo' : inf, 'pred' : []},
                    'b' : {'costo' : inf, 'pred' : []},
                    'c' : {'costo' : inf, 'pred' : []},
                    'd' : {'costo' : inf, 'pred' : []},
                    'e' : {'costo' : inf, 'pred' : []},
                    'f' : {'costo' : inf, 'pred' : []},
                    'g' : {'costo' : inf, 'pred' : []}}
        inicio = 'a'
        final = 'g'
        dimension = 6
    elif opcion == 3:
        grafo = {   'a' : {'b':1,'c':2, 'd':1},
                'b' : {'c':2, 'e':1},
                'c' : {'d': 1, 'e':2,'f':2},
                'd' : {'f':5},
                'e' : {'f':3,'g':1},
                'f' : {'g':4},
                'g' : {}}
        etiquetas = {   'a' : {'costo' : inf, 'pred' : []},
                    'b' : {'costo' : inf, 'pred' : []},
                    'c' : {'costo' : inf, 'pred' : []},
                    'd' : {'costo' : inf, 'pred' : []},
                    'e' : {'costo' : inf, 'pred' : []},
                    'f' : {'costo' : inf, 'pred' : []},
                    'g' : {'costo' : inf, 'pred' : []}}
        inicio = 'a'
        final = 'g'
        dimension = 6
        
    dijsktra(grafo,inicio,final,etiquetas,dimension)
with open('resultados_dijkstra.txt', 'a') as resultados:
    resultados.write("\n")
    resultados.write("Ejemplo:")
    resultados.write("\n")
    resultados.write(str(opcion))
    resultados.write("\n")
    resultados.write("Distancia más corta: " )
    resultados.write("\n")
    resultados.write(str(etiquetas[final]['costo']))
    resultados.write("\n")
    resultados.write("Ruta de la distancia más corta: ")
    resultados.write("\n")
    resultados.write(str(etiquetas[final]['pred'] + list(final)))
resultados.close()