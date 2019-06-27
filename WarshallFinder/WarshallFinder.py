import msvcrt
import sys
import math

def loadWeightedGraph(filename):
    file = open(filename)
    file.readline()
    G = []
    for line in file:
        if line == '\n':
            G.append([])
            continue
        
        G.append([])
        for nums in line.split(';'):
            nums = nums.split(',')
            G[len(G) - 1].append((int(nums[0]), float(nums[1])))
    
    return G

def floydWarshall(G):
    n = len(G)
    dist = [[float('inf')]*n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0
    
    for u in range(n):
        for v, w in G[u]:
            dist[u][v] = w
    
    print("Generando matriz de caminos...")

    temp = 1 + 3.3322*math.log10(n)
    thing = n//temp

    for k in range(n):
        if(k % thing == 0):
            print(str(round((k/n)*100,2)) + " %")

        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    if(n/temp != n//temp):
        print("100 %\n¡Listo!")

    return dist

def WarshallFinder(M):
    n = len(M)
    minPath = None
    minWeights = None

    minW = float('inf')

    for i in range(n):
        visited = [False]*n
        path = []*n
        weights = []*n

        visited[i] = True
        path.append(i)

        totalW = 0
        for j in range(n - 1):
            min = float('inf')
            idxmin = -1
            for k in range(n):
                if j != k and not visited[k]:
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
            
                        if key == b's' or key == b'S':
                            print("Resumen de ejecución hasta el momento:")
                            printPath(path, weights)
                            print("Progreso: " + str(round(((i*(n-1)*n + j*n + k)/(n*(n-1)*n))*100,2)) + " %")

                    if M[j][k] < min:
                        min = M[j][k]
                        idxmin = k
            
            totalW += min
            visited[idxmin] = True
            path.append(idxmin)
            weights.append(totalW)
        
        totalW += M[path[len(path) - 1]][i]
        path.append(i)

        if totalW < minW:
            minW = totalW

            minPath = path
            minWeights = weights
    
    return minPath, minWeights

def printPath(path, weights):
    print("\nCamino:")
        
    for i in range(len(path)):
        print(path[i], end='')
        
        if i + 1 != len(path):
            print(" -> ", end='')
            
    print("\n\nDistancias (en kilómetros):")
        
    for i in range(len(weights)):
        print(round(weights[i],2), end='')
        
        if i + 1 != len(weights):
            print(" -> ", end='')
        else:
            print("\n\nDistancia total:", round(weights[i], 2), "kilómetros")

if len(sys.argv) == 1:
    adyLstFN = "adylst.al"
else:
    adyLstFN = "WarshallFinder/" + sys.argv[1]

G = loadWeightedGraph(adyLstFN)
M = floydWarshall(G)

print("\nAlgoritmo en ejecución\nPresione S para obtener el estado actual")

p, w = WarshallFinder(M)
print("\n¡¡¡Camino (relativamente) más corto encontrado!!!")

printPath(p,w)
print("Progreso: 100 %")