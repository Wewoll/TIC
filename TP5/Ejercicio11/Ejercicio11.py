import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

# Calcula la lista de entropías a posteriori H(A|Bj)
# (Calcula la entropía de cada columna de la matriz P(A|B))
def calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A):
    matriz_posteriori = TP5_Funciones.calcularMatrizPosteriori(probs_priori_A, matriz_canal_B_dado_A)
        
    num_A = len(matriz_posteriori)
    num_B = len(matriz_posteriori[0])  
    lista_entropias_posteriori = []
    
    for j in range(num_B):
        columna_j = [matriz_posteriori[i][j] for i in range(num_A)]
        entropia_col = utils.calculoEntropia(columna_j)
        lista_entropias_posteriori.append(entropia_col)
        
    return lista_entropias_posteriori