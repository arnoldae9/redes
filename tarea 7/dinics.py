import networkx as nx
G = nx.DiGraph()
MAXN=220
INF=10**9 #TODO INF para representar el infinito
cap=[[0]*MAXN for _ in range(MAXN)] #TODO inicializando capacidad
rank=[-1]*MAXN #TODO inicializacion de niveles
n=int(input()) #TODO n es el nodo de destino
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
def dfs(v,f): #TODO algoritmo dfs
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
with open('prueba2.txt','r') as ejemplo1:
    for linea in ejemplo1:
        renglon.append(linea.split( ))

for item in renglon:
    for subitem in range(len(item)):
        item[subitem] = int(item[subitem])
for item in range(len(renglon)):
    cap[renglon[item][0]][renglon[item][1]] = renglon[item][2]
    i = renglon[item][0]
    j = renglon[item][1]
    capacidad = renglon[item][2]
    G.add_edge(i,j,capacity = capacidad)
 
ans=0
while 1:
    bfs(1)  #TODO condicion para si el nodo destino es el nodo inicial.
    if rank[n]==-1:
        print(ans)
        break
    f=1
    while f>0:
        f=dfs(1,INF) #TODO bucle del algoritmo.
        ans+=f
    
ans = input("Desea ejecutar Networkx ? \n")
if ans == "si":
    nodoinicio = int(input("Digite el nodo inicial \n"))
    nodofinal = int(input("Digite el nodo final \n"))
    flow_value = nx.maximum_flow_value(G, nodoinicio , nodofinal)
    print(flow_value)
else:
    print("fin")
    
    
    
    
    
    
    
