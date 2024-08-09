# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:02:53 2024

@author: HP
"""

import pandas as pd
print("----------- Datos de la DataSet -----------")
datos = pd.read_csv('ATP3.csv', encoding='ISO-8859-1')
print(datos.head())
datos.set_index("Location",inplace=True)
print("--------------------- Melbourne --------------")
print(datos.loc["Melbourne"]) # sola de las fila Melbourne
print("--------------------- Atlanta y Superficie --------------")
print(datos.loc['Atlanta','Surface']) # sola de las filas Atlanta y Surface
print("--------------------- Selección Amplia - Especifica --------------")
print(datos.loc[['Atlanta','Melbourne'],['Series','Court']]) # Filas, Columas (Especificas)
print("--------------------- Selección Amplia - Rango --------------")
print(datos.loc[['Atlanta','Melbourne'],'Series':'Round']) # Series hasta round
print("---------SELECCIÓN SOLAMENTE DE GRAN SLAM--------")
print(datos.loc[datos['Series'].str.endswith("Slam")])