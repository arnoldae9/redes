import networkx as nx
import copy

from numpy import fix
G = nx.DiGraph()
MAXN=int(input("Digite el numero de nodos \n")) + 1
INF=10**9 #TODO INF para representar el infinito
cap=[[0]*MAXN for _ in range(MAXN)] #TODO inicializando capacidad
rank=[-1]*MAXN #TODO inicializacion de niveles
n=int(input("ingreso el nodo destino \n")) #TODO n es el nodo de destino

def escribir(texto,flow,cortes):
    with open('resultadosminimum.txt', 'a') as resultados:
        resultados.write("\n")
        resultados.write("Ejemplo:")
        resultados.write("\n")
        resultados.write(str(texto))
        resultados.write("\n")
        resultados.write("El flujo máximo es de : " )
        resultados.write("\n")
        resultados.write(str(flow))
        resultados.write("\n")
        resultados.write("Los arcos son: ")
        resultados.write("\n")
        for item in cortes:
            resultados.write(str(item))
            resultados.write("\n")
    resultados.close()

def bfs(s): #TODO algoritmo bfs 
    for i in range(n+1):
        rank[i]=-1
    rank[s]=0
    q=[]
    q.append(s)
    while q:
        x=q.pop(0)
        for i in range(1,n+1):
            if cap[x][i]>0 and rank[i]==-1:
                rank[i]=rank[x]+1
                q.append(i)
def dfs(v,f): #TODO dfs
    if v==n: return f
    for i in range(1,n+1):
        if rank[i]==rank[v]+1 and cap[v][i]>0:
            d=dfs(i,min(f,cap[v][i]))
            if d>0:
                cap[v][i]-=d
                cap[i][v]+=d
                return d
    return 0

#TODO algoritmo para lecturea de datos desde archivo
renglon = []
texto = 'prueba7.txt' 
with open(texto,'r') as ejemplo1:
    for linea in ejemplo1:
        renglon.append(linea.split( ))

for item in renglon:
    for subitem in range(len(item)):
        item[subitem] = int(item[subitem])
for item in range(len(renglon)):
    cap[renglon[item][0]][renglon[item][1]] = renglon[item][2]
    aux = copy.deepcopy(cap)
    i = renglon[item][0]
    j = renglon[item][1]
    capacidad = renglon[item][2]
    G.add_edge(i,j,capacity = capacidad)
ans=0
while 1:
    bfs(1)
    if rank[n]==-1:
        print("El flujo maximo es: ", ans)
        break
    f=1
    while f>0:
        f=dfs(1,INF) #TODO bucle del algoritmo.
        ans+=f
print(cap)
if cap[1] == [0]*MAXN:
    print("El minimo corte es el nodo de origen.")
aux2 = copy.deepcopy(cap) #TODO matrix aux auxiliar residuales
nodosaccesibles = [1] 
#FIXME encontrar los nodos accesibles desde el nodo 1 matriz aux es la matriz de capacidad inicial aux2 residuales.
def search(v):
    for i in range(n+1):
        if cap[v][i] !=0:
            if i not in nodosaccesibles:
                nodosaccesibles.append(i)


for item in nodosaccesibles:
    search(item)
print(nodosaccesibles)


nodosnoaccesibles = []
for i in range(MAXN):
    nodosnoaccesibles.append(i) 
for i in nodosaccesibles:
    nodosnoaccesibles.remove(i)
print(nodosnoaccesibles)

cortes = []
for i in nodosaccesibles:
    for j in nodosnoaccesibles:
        if aux[i][j] > 0:
            print("El corte: (",i,",",j,") forma parte del minimo corte")
            cortes.append((i,j))
print("El valor de corte minimo es: ", ans)


    
    
    
    
    
    
    
