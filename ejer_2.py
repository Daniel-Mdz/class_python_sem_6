# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:23:15 2024

@author: HP
"""

import pandas as pd
datos=pd.read_csv('ATP.csv')
df= pd.DataFrame(datos)
df.reset_index().to_csv('DatosExportadosATP.csv', header=True, index=False)
datos.set_index("Location", inplace=True)
df= datos.loc['Melbourne']
df.reset_index().to_csv('MelbourneSeleccion.csv', header=True, index=False)
df2=datos.loc[datos['Series'].str.endswith("Slam")]
df.reset_index().to_csv('GSSelect.csv', header=True, index=False)