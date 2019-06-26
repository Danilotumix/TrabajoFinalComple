import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from DBConverter.CityMap import CityMap

filename = "C:/Users/DC/Documents/TrabajoFinalComple/DBConverter/CPDB.csv"

root = tk.Tk()
root.geometry("150x100")
root.title("Trabajo final")

msg.showinfo("Información", "Base de datos hallada")

label1 = tk.Label(root, text = "Conectar las ciudades por: ")
label1.grid(column=0, row=0)

combo1 = ttk.Combobox(root, 
                            values=[
                                    "Capitales regionales", 
                                    "Capitales provinciales",
                                    "Capitales distritales",])

combo1.grid(column=0, row=1)
combo1.current(0)

combo2 = ttk.Combobox(root, 
                            values=[
                                    "Bruteforce/Backtracking"])

label2 = tk.Label(root, text = "Seleccionar algoritmo: ")
label2.grid(column=0, row=2)

combo2.grid(column=0, row=3)
combo2.current(0)

"""
Label(root, text='Conversor de base de datos:').grid(row=0, column=0)
Button(root, text="Convertir de CSV a AdyLst", command=convertCSVToAl).grid(row=2, column=0)
Separator(root, orient=HORIZONTAL).grid(row=3, sticky="we")

Button(root, text="Correr algoritmo", command= lambda: runPathFinder(pf)).grid(row=4, column=0)


"""
root.mainloop()