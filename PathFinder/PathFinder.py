from .City import City
from .Pair import Pair

import msvcrt
import time
import sys

startTime = time.time()

class Path:
    def __init__(self, parent, weight):
        self.parent = parent
        self.weight = weight

class PathFinder:
    def __init__(self):
        self.cities = []
    
    def loadAdylst(self, filename):
        file = open(filename, "r")
        file.readline()

        i = 0
        while True:
            line = file.readline()
            if line == '':
                break
            
            while len(self.cities) <= i:
                self.cities.append(City())
            
            data = line.split(";")

            for connection in data:
                conData = connection.split(',')

                city = int(conData[0], 10)

                while len(self.cities) <= city:
                    self.cities.append(City())
                
                weight = float(conData[1])

                City.addConnection(self.cities[i], Pair(city, weight))
                City.addConnection(self.cities[city], Pair(i, weight))

            i = i + 1
        
        file.close()

    def bigFSearch(self, start, path, visited, actualWeight, citiesLeft, startCity, totalCities, minPath):
        path.append(Path(start, actualWeight))

        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b's' or key == b'S':
                printPath(path, False)
                
                total = totalCities - citiesLeft + 1
                
                if citiesLeft == 0:
                    total = total - 1
                
                print("\nTotal de ciudades en el camino:", total, '\n')
        
        if start != startCity:
            visited[start] = True
            
        if start == startCity and citiesLeft == 0:
            if len(minPath) == 0:
                minPath = path
            elif path[len(path) - 1].weight < minPath[len(minPath) - 1].weight:
                minPath = path
            
            return minPath

        for pair in self.cities[start].connections:
            if visited[pair.city] == False:
                if pair.city == startCity and citiesLeft != 1:
                    continue
                
                if len(minPath) == 0 or actualWeight + pair.weight < minPath[len(minPath) - 1].weight:
                    minPath = PathFinder.bigFSearch(self, pair.city, path.copy(), visited.copy(), actualWeight + pair.weight, citiesLeft - 1, startCity, totalCities, minPath.copy())
        
        return minPath

    def findPath(self):
        minWeight = float('inf')
        path = None
        for i in range(len(self.cities)):
            tempPath = PathFinder.bigFSearch(self, i, [], [False]*len(self.cities), 0, len(self.cities), i, len(self.cities), [])
            if tempPath[-1].weight < minWeight:
                path = tempPath.copy()
        
        return path
        
def printPath(path, final):
    print("\nCamino:")
        
    for i in range(len(path)):
        print(path[i].parent, end='')
        
        if i + 1 != len(path):
            print(" -> ", end='')
            
    print("\n\nDistancias (en kilómetros):")
        
    for i in range(len(path)):
        print(round(path[i].weight,2 ), end='')
        
        if i + 1 != len(path):
            print(" -> ", end='')
        else:
            print("\n\nDistancia total:", round(path[i].weight, 2), "kilómetros")

    actualTime = time.time()
    if final == False:
        print("\nTiempo de ejecución hasta el momento:", round((actualTime - startTime), 2), "segundos")
    else:
        print("\nTiempo de ejecución total:", round((actualTime - startTime), 2), "segundos")

def run(filename = "adylst.al"):
    pf = PathFinder()
    PathFinder.loadAdylst(pf, filename)
    print("¡Se ha cargado la lista de adyacencia!")

    print("\nAlgoritmo en ejecución\nPresione S para obtener el estado actual")

    shortestPath = PathFinder.findPath(pf)

    print("\n¡¡¡Camino más corto encontrado!!!")

    printPath(shortestPath, True)

    print("\nPresione F para continuar")