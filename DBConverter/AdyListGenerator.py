from CityMap import CityMap

import sys

filename = ""

if len(sys.argv) == 1:
    filename = "C:/Users/DC/Documents/TrabajoFinalComple/Bases de datos/CPDB.csv"
else:
    filename = sys.argv[1]

print("Cargando...")

cMap = CityMap()

CityMap.loadFromCSV(cMap, filename)

print("¡Listo!")
print("Conectando ciudades...")

CityMap.connectCitiesByDistanceOrig(cMap)

print("¡Listo!")
print("Exportando...")

CityMap.exportAsAdylst(cMap, "adylst.al", "metadata.md")

print("¡Listo!")