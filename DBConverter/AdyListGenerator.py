from CityMap import CityMap

import sys

filename = ""

if len(sys.argv) == 1:
    filename = "C:/Users/DC/Documents/TrabajoFinalComple/DBConverter/CPDB.csv"
else:
    filename = sys.argv[1]

print("Cargando...")

cMap = CityMap()

CityMap.loadFromCSV(cMap, filename, 1)

print("¡Listo!")
print("Conectando ciudades...")

CityMap.connectCitiesByDistance(cMap)

print("¡Listo!")
print("Exportando...")

CityMap.exportAsAdylst(cMap, "adylst.al", "metadata.md")

print("¡Listo!")