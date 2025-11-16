import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

# Verifica si un canal es "Sin Ruido"
def esCanalSinRuido(matriz_canal):        
    res = True
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])
    
    for j in range(num_columnas):
        conteo_no_cero = 0
        for i in range(num_filas):
            if matriz_canal[i][j] > 0:
                conteo_no_cero += 1
                
        if conteo_no_cero != 1:
            res = False
            
    return res

# Verifica si un canal es "Determinante".
def esCanalDeterminante(matriz_canal):
    res = True
    
    for fila in matriz_canal:
        conteo_no_cero = 0
        for prob in fila:
            if prob > 0:
                conteo_no_cero += 1

        if conteo_no_cero != 1:
            res = False
            
    return res