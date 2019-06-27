import subprocess as subp
import os as os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from DBConverter.CityMap import CityMap

def generateAl(v):
    subp.Popen("cls", shell=True)

    filename = filedialog.askopenfilename(initialdir = "./Base de datos/", title = "Seleccione la base de datos", filetypes = (("Archivos de valores delimitados por comas","*.csv"), ("Todos los archivos", "*")))

    cMap = CityMap()

    if v == 3:
        CityMap.loadFromCSV(cMap, filename, 0)
    else:
        CityMap.loadFromCSV(cMap, filename, v + 1)

    CityMap.connectCitiesByDistance(cMap)
    CityMap.exportAsAdylst(cMap, "adylst.al")
    print("¡Listo!")
    msg.showinfo("¡Finalizado!", "Lista de adyacencia guardada como adylst.al")

def process(v):
    subp.Popen("cls", shell=True)

    filename = filedialog.askopenfilename(initialdir = "./", title = "Seleccione input", filetypes = (("Archivo de lista de adyacencia","*.al"), ("Todos los archivos", "*")))

    if v == 0:
        #subp.Popen("cls", shell=True)
        subp.Popen("\"PathFinder\PathFinder.py\" " + filename, shell=True)
    
    if v == 1:
        #subp.Popen("cls", shell=True)
        subp.Popen("\"WarshallFinder\WarshallFinder.py\" " + filename, shell=True)
    
    if v == 2:
        #subp.Popen("cls", shell=True)
        print("\"MCB\MCB.py\" " + filename)
        subp.Popen("\"MCB\MCB.py\" " + filename, shell=True)

    if v == 3:
        filename = filedialog.askopenfilename(initialdir = "./BF/", title = "Seleccione input", filetypes = (("Archivos de valores delimitados por comas","*.csv"), ("Todos los archivos", "*")))
        #subp.Popen("cls", shell=True)
        subp.Popen("\"BF\BF.py\" " + filename, shell=True)

root = tk.Tk()
root.geometry("160x140")
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

tk.Button(root, text="Generar lista de adyacencia", command= lambda: generateAl(combo1.current())).grid(column=0, row=2)

combo2 = ttk.Combobox(root, 
                            values=[
                                    "PathFinder (Bruteforce/Backtracking)",
                                    "WarshallFinder (Floyd-Warshall)",
                                    "MCB! (Kruskal)",
                                    "BF (Bellman-Ford)"])

tk.Label(root, text = "Seleccionar algoritmo: ").grid(column=0, row=3)

combo2.grid(column=0, row=4)
combo2.current(0)

tk.Button(root, text="Correr algoritmo", command= lambda: process(combo2.current())).grid(column=0, row=5)

root.mainloop()