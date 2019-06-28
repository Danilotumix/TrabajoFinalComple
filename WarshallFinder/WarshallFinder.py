import msvcrt
import time
import sys
import math

startTime = time.time()

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
    path = [[-1]*n for _ in range(n)]
    dist = [[float('inf')]*n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0
    
    for u in range(n):
        for v, w in G[u]:
            path[u][v] = u
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
                    path[i][j] = k
    
    if(n/temp != n//temp):
        print("100 %\n¡Listo!")

    return path, dist

def getValidPath(Mp, visited, idx, j):
    while j != Mp[idx][j]:
        if visited[j]:
            return False

        j = Mp[idx][j]
    
    return True

def visitParents(Mp, visited, path, weights, idx, j):
    tempPath = []
    tempWeights = []

    while idx != Mp[idx][j]:
        print(len(visited))
        visited[j] = True
        tempPath.append(j)
        tempWeights.append(j)
        j = Mp[idx][j]

    for i in reversed(tempPath):
        path.append(i)
    
    for i in reversed(tempWeights):
        weights.append(i)

def WarshallFinder(G):
    Mp, Md = floydWarshall(G)

    print("\nAlgoritmo en ejecución\nPresione S para obtener el estado actual")

    n = len(Md)
    minPath = None
    minWeights = None

    minW = float('inf')

    for i in range(n):
        visited = [False]*n
        path = []
        weights = []

        visited[i] = True
        path.append(i)
        weights.append(0)

        totalW = 0
        idx = i
        while len(path) != n:
            min = float('inf')
            idxmin = -1
            for j in range(n):
                if j != i and not visited[j]:
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
            
                        if key == b's' or key == b'S':
                            printPath(path, weights)
                
                    if Md[idx][j] < min:
                        if Mp[idx][j] == idx:
                            min = Md[idx][j]
                            idxmin = j
                        else:
                            if getValidPath(Mp, visited, idx, j):
                                min = Md[idx][j]
                                idxmin = j
            
            if Mp[idx][idxmin] == idx:
                visited[idxmin] = True
                path.append(idxmin)
                totalW += min
                weights.append(totalW)
            else:
                visitParents(Mp, path, weights, visited, idx, j)
                totalW += min
            
            idx = idxmin

        for u, w in G[idx]:
            if u == i:
                totalW += w
                break
        
        path.append(i)
        weights.append(totalW)

        if totalW < minW:
            minW = totalW
            minPath = path
            minWeights = weights
    
    return minPath, minWeights

def printPath(path, weights, final = False):
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
    
    actualTime = time.time()
    if not final:
        print("\nTiempo de ejecución hasta el momento:", round((actualTime - startTime), 2), "segundos")
    else:
        print("\nTiempo de ejecución total:", round((actualTime - startTime), 2), "segundos")

if len(sys.argv) == 1:
    adyLstFN = "adylst.al"
else:
    adyLstFN = sys.argv[1]

G = loadWeightedGraph(adyLstFN)
p, w = WarshallFinder(G)
print("\n¡¡¡Camino (relativamente) más corto encontrado!!!")

printPath(p,w,True)
print("\nProgreso: 100 %")
