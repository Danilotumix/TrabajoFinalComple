import subprocess as subp
import os as os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from DBConverter.CityMap import CityMap

def process(v1, v2, filename):
    subp.Popen("cls", shell=True)

    cMap = CityMap()

    if v1 == 3:
        CityMap.loadFromCSV(cMap, filename, 0)
    else:
        CityMap.loadFromCSV(cMap, filename, v1 + 1)

    CityMap.connectCitiesByDistance(cMap)

    if v2 == 0:
        CityMap.exportAsAdylst(cMap, "PathFinder/adylst.al")
        subp.Popen("cls", shell=True)
        subp.Popen("\"PathFinder\PathFinder.py\" adylst.al", shell=True)
    
    if v2 == 1:
        CityMap.exportAsAdylst(cMap, "WarshallFinder/adylst.al")
        subp.Popen("cls", shell=True)
        subp.Popen("\"WarshallFinder\WarshallFinder.py\" adylst.al", shell=True)

root = tk.Tk()
root.geometry("150x120")
root.title("Trabajo final")

tk.Label(root, text = "Conectar las ciudades por: ").grid(column=0, row=0)

combo1 = ttk.Combobox(root, 
                            values=[
                                    "Capitales regionales", 
                                    "Capitales provinciales",
                                    "Capitales distritales",
                                    "Todos los demás"])

combo1.grid(column=0, row=1)
combo1.current(0)

combo2 = ttk.Combobox(root, 
                            values=[
                                    "PathFinder (Bruteforce/Backtracking)",
                                    "WarshallFinder (Floyd-Warshall)"])

tk.Label(root, text = "Seleccionar algoritmo: ").grid(column=0, row=2)

combo2.grid(column=0, row=3)
combo2.current(0)

filename = filedialog.askopenfilename(initialdir = "./Base de datos/", title = "Seleccione la base de datos", filetypes = (("Archivos de valores delimitados por comas","*.csv"), ("Todos los archivos", "*")))

tk.Button(root, text="Correr algoritmo", command= lambda: process(combo1.current(), combo2.current(), filename)).grid(column=0, row=4)

root.mainloop()