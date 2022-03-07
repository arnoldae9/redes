import numpy as np

#TODO algoritmo floyd warshall
def floyd_warshall(nodos,caminos):
    #TODO primer paso de asignar infinitos o ceros dependiendo si existe el camino
    d = {(u,v):  float('inf') if u != v else 0 for u in nodos for v in nodos }
    etiquetas = {(u,v): {'pred' : []} for u in nodos for v in nodos}
    #TODO asignación de los costos por caminos
    for (u,v), w_uv in caminos.items():
        d[(u,v)] = w_uv
    #TODO aplicación de la formula de floyd warshall
    for k in nodos:
        for u in nodos:
            for v in nodos:
                if d[(u,k)] + d[(k,v)] < d[(u,v)]:
                    etiquetas[(u,v)]['pred'] = [k]
                d[(u,v)] = min(d[(u,v)], d[(u,k)] + d[(k,v)])
                
    #TODO condición de ciclos negativos
    #FIXME checar si esta bien 
        if any(d[(u,u)] <0 for u in nodos):
            print("El grafo tiene un ciclo negativo")
            with open('resultados.txt','a') as resultados:
                resultados.write("\n")
                resultados.write("El grafo tiene un ciclo negativo \n")
            break
    #FIXME no me gusta la variable d XD
    return d ,etiquetas

#TODO algoritmo lectura de grafo
def lectura_datos (ejemplo1):
    nodos = []
    renglon = []
    caminos = {}
    #TODO se leen las lineas del archivo
    with open(ejemplo1,'r') as ejemplo1:
        for linea in ejemplo1:
            renglon.append(linea.split( ))
    #TODO convertir a flotante los valores leidos
    for item in renglon:
        for subitem in range(len(item)):
            item[subitem] = float(item[subitem])
    #TODO creamos el diccionario caminos
    for i in range(len(renglon)):
        for j in range(len(renglon)):
            if renglon[i][j] != 0:
                caminos.update({(i,j): renglon[i][j]})
    #TODO creamos los nodos
    for item in range(len(renglon)):
        nodos.append(item)
    return nodos , caminos
#TODO función para obtener la trayectoria
def trayec (inicio,destino):
    trayectoria = [destino]
    while (len(eti[(inicio,destino)]['pred']) != 0  ):
        trayectoria.append(eti[(inicio,destino)]['pred'][0])
        destino = eti[(inicio,destino)]['pred'][0]
    trayectoria.append(inicio)
    trayectoria.reverse()
    return trayectoria
def escritura(trayecto,costo):
    with open('resultados.txt','a') as resultados:
        resultados.write("\n")
        resultados.write("El costo menor es de %f \n" %costo)
        resultados.write("El camino es de: \n")
        for item in trayecto:
            resultados.write("%i " %item)
        resultados.write("\n")
        resultados.write("---------------------------------------------------------------------------")

#TODO se manda llamar la función para leer nodos y caminos
nodes, paths = lectura_datos('ejemplo3.txt')
#TODO se manda llamar la función del algoritmo
shortest_path , eti = floyd_warshall(nodes,paths)
#TODO se manda imprimir la matriz resultante

inicio = int(input("Escriba el nodo de inicio: "))
destino = int(input("Escriba el nodo de destino: "))

print("El costo menor es de: " , shortest_path[(inicio,destino)])
print("El camino es: ", trayec(inicio,destino))

#TODO función para escribir los datos en resultados.
escritura(trayec(inicio,destino),shortest_path[(inicio,destino)])