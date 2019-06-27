from .City import City

import math

class CityMap:
    def __init__(self):
        self.mapCities = []
        self.numberCities = 0

    def connectCitiesByDistance(self):
        for i in range(self.numberCities - 1):
            for j in range(self.numberCities - 1 - i):
                City.connectWithCity(self.mapCities[i], self.mapCities[j + 1 + i], j + 1 + i)
                City.connectWithCity(self.mapCities[j + 1 + i], self.mapCities[i], i)

    def loadFromCSV(self, filename, capital = -1):
        file = open(filename, "r")

        line = file.readline()
        while True:
            line = file.readline()
            if line == "":
                break

            data = line.split(',')

            capitalStatus = int(data[7])

            if capital != -1 and capitalStatus != capital:
                continue

            code = int(data[4])

            name = data[5]
            
            x = float(data[15])
            y = float(data[16])

            self.numberCities = self.numberCities + 1
            self.mapCities.append(City(code, name, x, y, capitalStatus))
        
        file.close()

    def exportAsAdylst(self, filename, filename2 = ""):
        file = open(filename, "w+")

        if filename2 != "":
            file2 = open(filename2, "w+")

        data = str(self.numberCities) + '\n'
        data2 = ""

        for city in self.mapCities:
            cList = city.connectedCities
            if len(cList) == 0:
                continue
            dList = city.connectedDistances

            for i in range(len(cList)):
                data += str(cList[i]) + ',' + f"{dList[i]:.6f}"
                if i != len(cList) - 1:
                    data += ';'
            
            data += '\n'

            if filename2 != "":
                data2 += str(city.code) + ';'
                data2 += str(city.name) + ';'
                data2 += str(city.x) + ';'
                data2 += str(city.y) + '\n'
        
        if filename2 != "":
            data2 = data2[0:len(data2)-1]
            file2.write(data2)
            file2.close()

        data = data[0:len(data)-1]
        file.write(data)
        file.close()

    def getAdylst(self, filename):
        file = open(filename, "w+")

        data = str(self.numberCities) + '\n'

        for city in self.mapCities:
            cList = city.connectedCities
            if len(cList) == 0:
                continue
            dList = city.connectedDistances

            for i in range(len(cList)):
                data += str(cList[i]) + ',' + f"{dList[i]:.6f}"
                if i != len(cList) - 1:
                    data += ';'
            
            data += '\n'

        return data[0:len(data)-1]