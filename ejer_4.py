# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:56:32 2024

@author: HP
"""

import pandas as pd
import numpy as np
df = pd.read_csv('DatosYT.csv')
print(df.dtypes) # print de tipos de variables
print(df.sort_values(by=['xs'],ascending=[True])) # odenar ascendete columna xs
df1 = pd.DataFrame(np.sort(df.values,axis=0),index=df.index,columns=df.columns)
print(df1) # ordena todas las columnas
