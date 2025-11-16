import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils
import math

# Toma una matriz de canal y aplica todas las reducciones suficientes
def realizarReduccionMaxima(matriz_canal):
    # Copiamos la matriz para no modificar la original
    matriz_actual = [fila[:] for fila in matriz_canal]
    
    # Bucle principal: sigue intentando reducir mientras pueda
    while True:
        num_cols_actual = len(matriz_actual[0])
        
        # Si la matriz ya tiene una sola columna, no se puede reducir más
        if num_cols_actual == 1:
            break
            
        par_encontrado = None

        # 1. Buscar un par de columnas reducibles (llama a 6a)
        #    (Buscamos de a un par por vez)
        for j in range(num_cols_actual):
            for k in range(j + 1, num_cols_actual):
                if TP6_Funciones.verificarColumnasProporcionales(matriz_actual, j, k):
                    par_encontrado = (j, k)
                    break
            if par_encontrado:
                break
        
        # 2. Si encontramos un par, reducimos la matriz
        if par_encontrado:
            j, k = par_encontrado
            
            # (Llama a 6b) Generar la matriz de transformación P(C|B)
            matriz_transform = TP6_Funciones.genMatrizReduccion(matriz_actual, j, k)
            
            # (Llama a 4) Multiplicar para obtener el canal reducido P(C|A)
            matriz_reducida = TP6_Funciones.calcularMatrizCompuesta(matriz_actual, matriz_transform)
            
            # Actualizamos la matriz para la siguiente iteración del 'while'
            matriz_actual = matriz_reducida
        
        # 3. Si no encontramos más pares, terminamos el bucle
        else:
            break
            
    return matriz_actual