import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



#try:
    #Primero leemos el fichero
  #  df = pd.read.csv("USA_Housing.csv")
#except FileNotFoundError:
    #Si el fichero no existe se muestra por pantalla lo siguiente.
  #  print("El fichero no existe.")
#else:
   # lineas = df.readlines()    
   # df.close()
    #columnas = lineas[0].split("\t")
   # traduccion = {"Avg. Area Income" : "Área de ingreso" , "Avg. Area House Age" : "Antiguedad de las casas" , "Avg. Area Number of Rooms" : "Número de habitaciones", "Avg. Area Number of Bedrooms" : "Número de dormitorios", "Area Population" : "Población del Área", "Price" : "Precio" , "Address" : "Dirección" }
  #  viviendas =[]
  #  for linea in lineas[1:]:
   #     vivienda={}
    #    campos = linea.split("\t")
   #     for i in range (len(columnas)):
      #      if columnas[i] in seleccion:
      #          vivienda[traduccion[columnas[i]]] = campos[i]
        #        viviendas.append(vivienda)
      #          print(viviendas)



viviendas = pd.read_csv("USA_Housing" , sep = "\t")
viviendas.rename(colums ={"Avg. Area Income" : "Área de ingreso" , "Avg. Area House Age" : "Antiguedad de las casas" , "Avg. Area Number of Rooms" : "Número de habitaciones", "Avg. Area Number of Bedrooms" : "Número de dormitorios", "Area Population" : "Población del Área", "Price" : "Precio" , "Address" : "Dirección" }, inplace=True)
viviendas =viviendas.dropna()
