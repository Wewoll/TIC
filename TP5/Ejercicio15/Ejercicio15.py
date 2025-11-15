import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils
import math

# Calcula la Equivocación o Ruido H(A|B)
def calcularEquivocacion(probs_priori_A, matriz_canal_B_dado_A):
    entropias_posteriori = TP5_Funciones.calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A)
    probs_salida_B = TP5_Funciones.calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
    equivocacion = sum(p_b * h_post for p_b, h_post in zip(probs_salida_B, entropias_posteriori))
        
    return equivocacion

# Calcula la Pérdida H(B|A)
def calcularPerdida(probs_priori_A, matriz_canal_B_dado_A):
    num_A = len(probs_priori_A)
    perdida = 0.0
    
    for i in range(num_A):
        entropia_fila = utils.calculoEntropia(matriz_canal_B_dado_A[i])
        perdida += probs_priori_A[i] * entropia_fila
        
    return perdida

# Calcula la Entropía Afín o Conjunta H(A, B).
def calcularEntropiaAfin(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = TP5_Funciones.calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    lista_probs_simultaneas = []
    for fila in matriz_simultanea:
        lista_probs_simultaneas.extend(fila)

    return utils.calculoEntropia(lista_probs_simultaneas)

# Calcula la Información Mutua I(A, B) por su fórmula de definición
def calcularInformacionMutua(probs_priori_A, matriz_canal_B_dado_A):
    probs_A = probs_priori_A
    probs_B = TP5_Funciones.calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
    matriz_A_B = TP5_Funciones.calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)
        
    num_A = len(matriz_A_B)
    num_B = len(matriz_A_B[0]) 
    info_mutua = 0.0
    
    for i in range(num_A):
        for j in range(num_B):
            p_a = probs_A[i]
            p_b = probs_B[j]
            p_ab = matriz_A_B[i][j]
            
            if p_ab > 0:
                termino = p_ab * math.log2(p_ab / (p_a * p_b))
                info_mutua += termino
                
    return info_mutua