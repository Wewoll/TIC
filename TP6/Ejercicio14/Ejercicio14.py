import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

# Calcula la probabilidad de error (P_E)
def calcularProbabilidadError(probs_priori, matriz_canal):
    num_entradas = len(matriz_canal)    # Filas
    num_salidas = len(matriz_canal[0]) # Columnas

    # 1. Encontrar la "Regla de Decisión" (índices de los máximos de P(B|A))
    indices_maximos_regla = [-1] * num_salidas
    
    for j in range(num_salidas): # Para cada columna
        max_val = -1.0
        indice_max = -1
        for i in range(num_entradas): # Buscar el máximo en la fila i
            if matriz_canal[i][j] > max_val:
                max_val = matriz_canal[i][j]
                indice_max = i
        indices_maximos_regla[j] = indice_max

    # 2. Calcular P_E sumando las probabilidades P(A,B) de los "errores"
    probabilidad_error_total = 0.0
    
    for j in range(num_salidas): # Para cada columna (salida)
        for i in range(num_entradas): # Para cada fila (entrada)
            
            # Si la entrada 'i' NO es la que la regla eligió para esta salida 'j'...
            if i != indices_maximos_regla[j]:
                # ...entonces es un error. Sumamos su probabilidad simultánea.
                # P(A,B) = P(A) * P(B|A)
                prob_simultanea_error = probs_priori[i] * matriz_canal[i][j]
                probabilidad_error_total += prob_simultanea_error

    return probabilidad_error_total


# Estas es la otra funcion "logicamente correcta" o algo asi
# Calcula la probabilidad de error (P_E) utilizando la regla de decisión de maxima posibilidad
def calcularProbabilidadError_Gemini(probs_priori_A, matriz_canal_B_dado_A):    
    # 1. Calcular la matriz de eventos simultáneos P(A, B)
    matriz_simultanea = utils.calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    num_A = len(matriz_simultanea)    # Nro de filas (entradas)
    num_B = len(matriz_simultanea[0]) # Nro de columnas (salidas)
    
    prob_acierto_total = 0.0
    
    # 2. Iterar por cada COLUMNA (cada salida B_j)
    for j in range(num_B):
        
        # 3. Encontrar la probabilidad máxima en esa columna
        #    (Esta es la probabilidad de "adivinar correctamente" para esa salida)
        max_prob_columna = 0.0
        for i in range(num_A):
            if matriz_simultanea[i][j] > max_prob_columna:
                max_prob_columna = matriz_simultanea[i][j]
                
        # 4. Sumar la probabilidad de este acierto al total
        prob_acierto_total += max_prob_columna
        
    # 5. La probabilidad de error es 1 - (la probabilidad total de acertar)
    prob_error = 1.0 - prob_acierto_total
    
    return prob_error