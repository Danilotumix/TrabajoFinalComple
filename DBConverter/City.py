import math

class City:
    def __init__(self, code, name, x, y, d):
        self.code = code
        self.name = name
        self.x = x
        self.y = y
        self.dOrig = 0
        self.d = d
        self.connectedCities = [0]*4
        self.connectedDistances = [-1]*4
    
    def __lt__(self, other):
        return self.d < other.d

    def connectWithCity(self, city, posCity):
        for i in range(len(self.connectedDistances)):
            if self.connectedDistances[i] == -1:
                self.connectedDistances[i] = getDistance(self, city)
                self.connectedCities[i] = posCity
                break

def getDistance(a, b):
    diff_x = a.x - b.x
    diff_y = a.y - b.y

    return math.sqrt(((diff_x ** 2) + (diff_y ** 2)))