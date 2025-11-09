import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# Calcula distancia de Hamming, errores detectables y errores corregibles
def analizarCodigoHamming(codigos):    
    n = len(codigos)
    min_distancia = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum(1 for c1, c2 in zip(codigos[i], codigos[j]) if c1 != c2)
            
            if dist < min_distancia:
                min_distancia = dist
                
    errores_detectables = min_distancia - 1
    errores_corregibles = (min_distancia - 1) // 2
    
    return min_distancia, errores_detectables, errores_corregibles