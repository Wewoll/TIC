import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

# Calcula la lista de probabilidades de los símbolos de salida P(B)
# P(B) = Suma sobre A de P(A, B)
def calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    num_A = len(matriz_simultanea)
    num_B = len(matriz_simultanea[0])
    probs_salida_B = [0.0] * num_B
    
    for j in range(num_B):
        for i in range(num_A):
            probs_salida_B[j] += matriz_simultanea[i][j]
        
    return probs_salida_B

# Calcula la matriz de probabilidades a posteriori P(A|B)
# P(A|B) = P(A, B) / P(B)
def calcularMatrizPosteriori(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)
    probs_salida_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)

    num_A = len(matriz_simultanea)
    num_B = len(matriz_simultanea[0])
    matriz_posteriori = [[0.0] * num_B for _ in range(num_A)]
    
    for i in range(num_A):
        for j in range(num_B):
            if probs_salida_B[j] == 0:
                matriz_posteriori[i][j] = 0.0
            else:
                matriz_posteriori[i][j] = matriz_simultanea[i][j] / probs_salida_B[j]
    
    return matriz_posteriori

# Calcula la matriz de probabilidades de eventos simultáneos P(A, B)
# P(A, B) = P(B|A) * P(A)
def calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A):
    num_A = len(probs_priori_A)
    num_B = len(matriz_canal_B_dado_A[0])
    matriz_simultanea = [[0.0] * num_B for _ in range(num_A)]
    
    for i in range(num_A):
        for j in range(num_B):
            matriz_simultanea[i][j] = matriz_canal_B_dado_A[i][j] * probs_priori_A[i]
            
    return matriz_simultanea