import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

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
        
    matriz_prob = []
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
                
        matriz_prob.append(fila)
        
    return matriz_prob