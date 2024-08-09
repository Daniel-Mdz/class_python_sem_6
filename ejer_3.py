# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:37:24 2024

@author: HP
"""

import pandas as pd
datos = pd.read_csv('ATP.csv')
print(datos.head())
datos.set_index("Location",inplace=True)
# Solo muestra filas de la columna Surface que court tenga "Outdoor"
print("------- Solo muesdtra las palabras de la columna Surface ------")
print(datos.loc[datos['Court']=='Outdoor',['Surface']])
# Solo muestra filas de la columna Surface y Winner  que court tenga "Outdoor"
print("------- Solo muesdtra las palabras de la columna Surface y Winner ------")
print(datos.loc[datos['Court']=='Outdoor',['Surface','Winner']])
print("---------- Más de una condición -------------")
print(datos.loc[datos['Series'].str.endswith("Slam")&(datos['Surface']=='Clay')&(datos['Winner']=='Federer R.')&(datos['Round'])=='The Final'])
print(datos.loc[datos['Series'].str.endswith("Slam")&(datos['Surface']=='Clay')])