import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP2_Funciones

matriz = [ [1/2, 1/3, 0] ,
           [1/2, 1/3, 1] ,
           [0, 1/3, 0]
         ]

vector = TP2_Funciones.genVectorEstacionario(matriz)
print(vector)
print(TP2_Funciones.calculoEntropiaMarkov(matriz))