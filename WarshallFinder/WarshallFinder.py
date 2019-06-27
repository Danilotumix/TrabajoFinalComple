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

def getValidPath(Mp, visited, j, k):
    while j != Mp[j][k]:
        if visited[k]:
            return False
        k = Mp[j][k]
    
    return True

def visitParents(Mp, visited, path, weights, j, k):
    tempPath = []
    tempWeights = []

    while j != Mp[j][k]:
        visited[k] = True
        tempPath.append(k)
        tempWeights.append(k)
        k = Mp[j][k]

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
                            print("\nProgreso: " + str(round(((i*(n-1)*n + j*n + k)/(n*(n-1)*n))*100,2)) + " %\n")

                    if Md[j][k] < min:
                        if Mp[j][k] == j:
                            min = Md[j][k]
                            idxmin = k
                        else:
                            if getValidPath(Mp, visited, j, k):
                                min = Md[j][k]
                                idxmin = k
            
            if Mp[j][k] == j:
                totalW += min
                visited[idxmin] = True
                path.append(idxmin)
                weights.append(totalW)
            else:
                visitParents(Mp, path, weights, visited, j, k)
                totalW += min
        
        totalW += Md[path[len(path) - 1]][i]
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
p, w = WarshallFinder(G)
print("\n¡¡¡Camino (relativamente) más corto encontrado!!!")

printPath(p,w)
print("\nProgreso: 100 %")