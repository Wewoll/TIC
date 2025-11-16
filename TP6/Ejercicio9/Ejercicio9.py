import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils
import math

# Verifica si un canal es "Uniforme"
# Todas las filas son una permutación de la primera fila
def esCanalUniforme(matriz_canal):    
    # Usamos sorted() para tener una "huella" canónica de la fila
    # sorted([0.3, 0.5, 0.2]) -> [0.2, 0.3, 0.5]
    huella_fila_1 = sorted(matriz_canal[0])
    
    for fila in matriz_canal[1:]:
        # Si la "huella" de esta fila no coincide con la primera...
        if sorted(fila) != huella_fila_1:
            return False
            
    return True


# Calcula la capacidad  de un canal si es de un tipo especial (Determinante, Sin Ruido o Uniforme)
def calcularCapacidadEspecial(matriz_canal):
    num_entradas = len(matriz_canal)
    num_salidas = len(matriz_canal[0])
    
    # (i) Caso Canal Determinante
    if TP6_Funciones.esCanalDeterminante(matriz_canal):
        # C = log2(Nro de Salidas)
        return math.log2(num_salidas)

    # (ii) Caso Canal Sin Ruido
    if TP6_Funciones.esCanalSinRuido(matriz_canal):
        # C = log2(Nro de Entradas)
        return math.log2(num_entradas)
        
    # (iii) Caso Canal Uniforme
    if esCanalUniforme(matriz_canal):
        # C = log2(Nro Salidas) - H(fila)
        # H(fila) es la entropía de cualquier fila (usamos la primera)
        entropia_fila = utils.calculoEntropia(matriz_canal[0])
        return math.log2(num_salidas) - entropia_fila

    # Si no es ninguno de los casos especiales:
    # La capacidad debe calcularse por métodos numéricos (Ej. 10)
    return None