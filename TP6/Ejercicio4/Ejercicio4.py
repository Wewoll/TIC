import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

# Calcula la matriz del canal compuesto P(C|A)
# P(C|A) = P(B|A) * P(C|B)
def calcularMatrizCompuesta(matriz_P_B_dado_A, matriz_P_C_dado_B):
    # --- Dimensiones ---
    # Matriz A->B tiene A_filas x B_cols
    A_filas = len(matriz_P_B_dado_A)
    B_cols_A = len(matriz_P_B_dado_A[0])
    
    # Matriz B->C tiene B_filas x C_cols
    B_filas_B = len(matriz_P_C_dado_B)
    C_cols = len(matriz_P_C_dado_B[0])
        
    # --- Inicializar Matriz Resultante ---
    # Tendrá A_filas x C_cols
    matriz_compuesta_P_C_dado_A = [[0.0] * C_cols for _ in range(A_filas)]
    
    # --- Multiplicación de Matrices ---
    # i = filas de la nueva matriz (A_filas)
    for i in range(A_filas):
        # j = columnas de la nueva matriz (C_cols)
        for j in range(C_cols):
            
            suma_caminos = 0.0
            # k = estados intermedios (B_cols_A o B_filas_B)
            for k in range(B_cols_A):
                # P(Bk|Ai) * P(Cj|Bk)
                suma_caminos += matriz_P_B_dado_A[i][k] * matriz_P_C_dado_B[k][j]
                
            matriz_compuesta_P_C_dado_A[i][j] = suma_caminos
            
    return matriz_compuesta_P_C_dado_A