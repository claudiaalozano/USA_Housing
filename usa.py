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

class usa:
    

    def diagrama_de_sectores (viviendas, "Área de ingreso"):
        fig, ax = plt.subplots()
        viviendas[viviendas."Área de ingreso"].plot(kind = "pie" , autopct = "%1.0f%%" , ax = ax)
        ax.set_title("Diagrama de sectores de USA housing" , loc = "center" , fontdict ={"fontsize": 12, "fontweight": "bold", "color" : "tab: green"})
        ax.set_ylabel(" ")
        plt.savefig("Diagrama_de_sectores_USA_Housing.png" , bbox_inches ="tight")
        return
    
    def diagrama_de_barras(viviendas):
        fig, ax = plt.subplots()
        viviendas.plot(kind= "bar")
        ax.set_title("Diagrama de barras USA Housing" , loc = "center" , fontdict = {"fontsize": 12, "fontweight": "bold" , "color" : "tab: green"})
        ax.grid(axis = "y" , color = "lightgray" , linestyle = "dashed")
        plt.savefig("Diagrama_de_barras.png" , bbox_inches = "tight")
        return
    
    def grafico_de_dispersion(viviendas):
        fig, ax = plt.subplots()
        viviendas_grafico = viviendas[viviendas.isin(viviendas)]
        ax.scatter(viviendas["Área de ingreso"] , viviendas["Antiguedad de las casas"])
        ax.set_title("Diagrama de dispersión del Área de ingreso con respecto a la antiguedad de las casas", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_xlabel("Área de ingreso")
        ax.set_ylabel("Antiguedad de las casas")
        plt.savefig("Diagrama_de_dispersión.png" , bbox_inches = "tight")
        return
