import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import os
import sys
df = pd.read_csv("USA_Housing.csv")
df.rename(colums={"Avg. Area Income" : "Área de ingreso" , "Avg. Area House Age" : "Antiguedad de las casas" , "Avg. Area Number of Rooms" : "Número de habitaciones", "Avg. Area Number of Bedrooms" : "Número de dormitorios", "Area Population" : "Población del Área", "Price" : "Precio" , "Address" : "Dirección" }, inplace=True)
df.columns
df =df.dropna()
df = df.reset_index(drop=True)

class Housing:
  def diagrama_de_barras(self, df, columna1, columna2):
    columna1 = pd.DataFrame(df["Precio"])
    columna2 = pd.DataFrame(df["Antiguedad de las casas"])
    plt.xlabel("Precio")
    plt.ylabel("Antiguedad de las casas")
    plt.legend(["Precio", "Antiguedad de las casas"], loc=1)
    self.df[columna1, columna2].plot(kind="bar", width= 0.5, color= "red" , title="Precio vs Antiguedad de las casas")
    plt.savefig("Precio/Antiguedad_casas.png")
    plt.show()

  def diagrama_de_barras_2 (self, df, columna3, columna4):
    columna3 = pd.DataFrame(df["Número de habitaciones"])
    columna4 = pd.DataFrame(df["Precio"])
    plt.xlabel("Precio")
    plt.ylabel("Número de habitaciones")
    self.df[columna3 , columna4].plot(kind="bar", width= 0.5, color= "blue" , title="Precio vs Número de habitaciones")
    plt.savefig("Precio/Número_habitaciones.png")
    plt.show()


  def diagrama_de_dispersion(self, df, variable1, variable2):
    variable1= pd.DataFrame(df["Poplación del Área"])
    variable2= pd.DataFrame(df["Número de habitaciones"])
    plt.xlabel("Número de habitaciones")
    plt.ylabel("Poplación del Área")
    my_plot = self.df[variable1, variable2].plot(kind="scatter", color= "green" , title="Poplación del Área vs Número de habitaciones")
    plt.savefig("Poplación_del_Área/Número_habitaciones.png")
    plt.show()


  def diagrama_de_linea(self, df, columna1, columna2):
    columna1 = pd.DataFrame(df["Precio"])
    columna2 = pd.DataFrame(df["Población del Área"])
    plt.xlabel("Precio")
    plt.ylabel("Población del Área")
    plt.legend(["Precio", "Población del Área"], loc=1)
    self.df[columna1, columna2].plot(kind="line", width= 0.5, color= "red" , title="Precio vs Antiguedad de las casas")
    ax= plt.subplot()
    for i, txt in enumerate(columna2):
      ax.annotate(txt, (columna1[i], columna2[i]))

#aplico k-means para decidir el número de clusters que quiero
  def elbow (self):
    nc = range(1, 1000000)
    kmeans = [kmeans(n_clusters=i) for i in nc]
    puntuacion = [kmeans[i].fit(df).puntuacion(df) for i in range (len(kmeans))]
    plt.xlabel("Número de clusters")
    plt.ylabel("Suma de los errores cuadráticos")
    plt.plot(nc, puntuacion)
    plt.show()

#añado una columna al Dataset con los clusters para analizarlos posteriormente
  def kmeans (self, n_clusters):
    kmeans = kmeans(n_clusters= 4).fit(df)
    labels = kmeans.predict(df)
    df["Clusters"] = labels
    return df
  
#ahora muestro una gráfica de los clusters 
  def grafica_cluster(self,df):
    colores = ["yellow", "blue", "red", "green"]
    asignar = []
    kmeans = kmeans(n_clusters= 4).fit(df)
    labels = kmeans.predict(df)
    for row in labels:
      asignar.append(colores[row])
    plt.xlabel("Precio")
    plt.ylabel("Número de habitaciones")
    plt.title("Número de habitaciones stocks k-means clustering")
    plt.scatter(df["Precio"], df["Número de habitaciones"], c=asignar, s=50)
    plt.show()




