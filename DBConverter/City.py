import math

class City:
    def __init__(self, code, name, x, y, capitalStatus):
        self.code = code
        self.name = name
        self.x = x
        self.y = y
        self.capitalStatus = capitalStatus
        self.connectedCities = []
        self.connectedDistances = []

    def connectWithCity(self, city, posCity):
        self.connectedDistances.append(getDistance(self, city))
        self.connectedCities.append(posCity)

def getDistance(a, b):
    diff_x = a.x - b.x
    diff_y = a.y - b.y

    return math.sqrt(((diff_x ** 2) + (diff_y ** 2)))