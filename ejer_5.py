# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:21:18 2024

@author: HP
"""

import pandas as pd
df = pd.read_csv('canciones.csv')
print(df.info())
print(df)
filas = len(df.index)
print("Filas: ",filas)
df.drop(df.index[[filas-1]],inplace=True) # indice de la ultima fila -1
print("Filas: ",filas)
print(df)