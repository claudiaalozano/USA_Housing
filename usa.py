import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    #Primero leemos el fichero
    df = pd.read.csv("USA_Housing.csv")
except FileNotFoundError:
    #Si el fichero no existe se muestra por pantalla lo siguiente.
    print("El fichero no existe.")
else:
    lineas = df.readlines()    
    df.close()
    columnas = lineas[0].split("\t")
    traduccion = {"Avg. Area Income" , "Avg. Area House Age" , "Avg. Area Number of Rooms" , "Avg. Area Number of Bedrooms" , "Area Population" : "", "Price" : "Precio" , "Address" : "Dirección" }