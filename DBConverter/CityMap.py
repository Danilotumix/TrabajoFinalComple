from City import City

import math

class CityMap:
    def __init__(self):
        self.mapCities = []
        self.numberCities = 0

    def sortCitiesByOrig(self):
        mergeSort(self.mapCities)
    
    def connectCitiesByDistanceOrig(self):
        CityMap.sortCitiesByOrig(self)

        c = 0

        for i in range(self.numberCities - 4):
            for j in range(1, 5):
                City.connectWithCity(self.mapCities[i], self.mapCities[i+j], i+j)
            
            if (c * 100) % self.numberCities == 0:
                processes = c / self.numberCities * 100
                print("Procesado el: " + str(processes) + "% de ciudades", sep="")
            
            c = c + 1
        
        for i in range(self.numberCities - 4, self.numberCities):
            for j in range(1, 5):
                City.connectWithCity(self.mapCities[i], self.mapCities[i-j], i-j)
        
        print("Procesado el: 100% de ciudades")

    def loadFromCSV(self, filename):
        file = open(filename, "r")

        line = file.readline()
        while True:
            line = file.readline()
            if line == "":
                break

            data = line.split(',')

            code = int(data[4])

            name = data[5]
            
            x = float(data[15])
            y = float(data[16])

            self.numberCities = self.numberCities + 1
            self.mapCities.append(City(code, name, x, y, getDistanceOrig(x,y)))
        
        file.close()

    def exportAsAdylst(self, filename, filename2 = ""):
        file = open(filename, "w+")

        if filename2 != "":
            file2 = open(filename2, "w+")

        data = ""
        data2 = ""

        for city in self.mapCities:
            cList = city.connectedCities
            dList = city.connectedDistances

            for i in range(4):
                data += str(cList[i]) + ',' + str(dList[i])
                if i != 3:
                    data += ';'
            
            data += '\n'

            if filename2 != "":
                data2 += str(city.code) + ';'
                data2 += str(city.name) + ';'
                data2 += str(city.x) + ';'
                data2 += str(city.y) + '\n'
        
        if filename2 != "":
            file2.write(data2)
            file2.close()

        file.write(data)
        file.close()

def mergeSort(vector): 
    if len(vector) > 1: 
        mid = len(vector)//2
        L = vector[:mid]
        R = vector[mid:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                vector[k] = L[i] 
                i+=1
            else: 
                vector[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            vector[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            vector[k] = R[j] 
            j+=1
            k+=1

def getDistanceOrig(x, y):
    return math.sqrt(((x ** 2) + (y ** 2)))