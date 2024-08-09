# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:16:16 2024

@author: HP
"""

import pandas as pd
print("----------- Datos de la DataSet -----------")
datos = pd.read_csv('ATP3.csv', encoding='ISO-8859-1')
print(datos.info())
print(datos.head()) # los 5 primeros
print(datos.iloc[0:8]) # datos de la linea del 0 al 8
print("----------- Reglones salteados -----------")
print(datos.iloc[[0,3,5,10,24],]) # especifico que lineas quiero
print("----------- Columnas -----------")
print(datos.iloc[:,0:2]) # primeras 4 filas de las dos primeras columas
print("----------- Columnas y filas especificas -----------")
print(datos.iloc[[0,3,6,24],[0,5,6]]) # filas , columnas (especificas)
print("----------- Rangos de reglones y columnas -----------")
print(datos.iloc[0:5,5:8]) # filas , columnas (rangos)
