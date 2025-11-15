import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils
import math

# Genera la matriz que representa al canal de las cadenas recibidas
def genMatrizCanal(secuencia_entrada, secuencia_salida):
    alfabeto_A = utils.genAlfabeto(secuencia_entrada)
    alfabeto_B = utils.genAlfabeto(secuencia_salida)
    
    conteo_A = {simbolo: 0 for simbolo in alfabeto_A}
    conteo_pares = {sim_A: {sim_B: 0 for sim_B in alfabeto_B} for sim_A in alfabeto_A}
        
    for i in range(len(secuencia_entrada)):
        sim_A = secuencia_entrada[i]
        sim_B = secuencia_salida[i]
        
        conteo_pares[sim_A][sim_B] += 1
        conteo_A[sim_A] += 1
        
    matriz_canal = []
    for sim_A in alfabeto_A:
        fila = []
        denominador = conteo_A[sim_A]
        
        for sim_B in alfabeto_B:
            if denominador == 0:
                fila.append(0.0)
            else:
                numerador = conteo_pares[sim_A][sim_B]
                prob = numerador / denominador
                fila.append(prob)
                
        matriz_canal.append(fila)
        
    return matriz_canal


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


# Calcula la lista de entropías a posteriori H(A|Bj)
# (Calcula la entropía de cada columna de la matriz P(A|B))
def calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A):
    matriz_posteriori = calcularMatrizPosteriori(probs_priori_A, matriz_canal_B_dado_A)
        
    num_A = len(matriz_posteriori)
    num_B = len(matriz_posteriori[0])  
    lista_entropias_posteriori = []
    
    for j in range(num_B):
        columna_j = [matriz_posteriori[i][j] for i in range(num_A)]
        entropia_col = utils.calculoEntropia(columna_j)
        lista_entropias_posteriori.append(entropia_col)
        
    return lista_entropias_posteriori


# Calcula la Equivocación o Ruido H(A|B)
def calcularEquivocacion(probs_priori_A, matriz_canal_B_dado_A):
    entropias_posteriori = calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A)
    probs_salida_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
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
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    lista_probs_simultaneas = []
    for fila in matriz_simultanea:
        lista_probs_simultaneas.extend(fila)

    return utils.calculoEntropia(lista_probs_simultaneas)


# Calcula la Información Mutua I(A, B) por su fórmula de definición
def calcularInformacionMutua(probs_priori_A, matriz_canal_B_dado_A):
    probs_A = probs_priori_A
    probs_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
    matriz_A_B = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)
        
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