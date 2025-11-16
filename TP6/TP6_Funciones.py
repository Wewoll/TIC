import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils
import math

# Verifica si un canal es "Sin Ruido"
def esCanalSinRuido(matriz_canal):
    num_filas = len(matriz_canal)
    num_columnas = len(matriz_canal[0])
    
    for j in range(num_columnas):
        conteo_no_cero = 0
        for i in range(num_filas):
            if matriz_canal[i][j] > 0:
                conteo_no_cero += 1
                
        if conteo_no_cero != 1:
            return False
            
    return True


# Verifica si un canal es "Determinante"
def esCanalDeterminante(matriz_canal):
    for fila in matriz_canal:
        conteo_no_cero = 0
        for prob in fila:
            if prob > 0:
                conteo_no_cero += 1

        if conteo_no_cero != 1:
            return False
            
    return True


# Calcula la matriz del canal compuesto P(C|A)
# P(C|A) = P(B|A) * P(C|B)
def calcularMatrizCompuesta(matriz_P_B_dado_A, matriz_P_C_dado_B):
    A_filas = len(matriz_P_B_dado_A)
    B_cols_A = len(matriz_P_B_dado_A[0])
    C_cols = len(matriz_P_C_dado_B[0])
    matriz_compuesta_P_C_dado_A = [[0.0] * C_cols for _ in range(A_filas)]
    
    for i in range(A_filas):
        for j in range(C_cols):
            suma_caminos = 0.0
            for k in range(B_cols_A):
                suma_caminos += matriz_P_B_dado_A[i][k] * matriz_P_C_dado_B[k][j]  
            matriz_compuesta_P_C_dado_A[i][j] = suma_caminos
            
    return matriz_compuesta_P_C_dado_A


# Verifica si dos columnas de una matriz de canal son proporcionales en cualquiera de los dos sentidos  
def verificarColumnasProporcionales(matriz, c1, c2):
    return (proporcionalEnUnSentido(matriz, c1, c2) or proporcionalEnUnSentido(matriz, c2, c1))

# Funcion de verdad que es llamada por la de arriba
def proporcionalEnUnSentido(matriz, a, b, tol = 1e-9):
    constante = None

    for fila in range(len(matriz)):
        x = matriz[fila][a]
        y = matriz[fila][b]

        es_x_cero = math.isclose(x, 0.0, abs_tol=tol)
        es_y_cero = math.isclose(y, 0.0, abs_tol=tol)

        if es_x_cero and es_y_cero:
            continue

        if es_y_cero and not es_x_cero:
            return False

        ratio = x / y

        if constante is None:
            constante = ratio
        elif not math.isclose(ratio, constante, abs_tol=tol):
            return False

    return True


# Genera la matriz de transformación ("canal determinante") para combinar las dos columnas
def genMatrizReduccion(matriz_canal, idx_col1, idx_col2):
    num_columnas_original = len(matriz_canal[0])
    num_columnas_nueva = num_columnas_original - 1
    matriz_transform = [[0.0] * num_columnas_nueva for _ in range(num_columnas_original)]
    
    idx_col_fusionada = min(idx_col1, idx_col2)
    idx_col_eliminada = max(idx_col1, idx_col2)
    puntero_col_nueva = 0
    
    for i in range(num_columnas_original):
        if i == idx_col_eliminada:
            matriz_transform[i][idx_col_fusionada] = 1.0
        else:
            matriz_transform[i][puntero_col_nueva] = 1.0
            puntero_col_nueva += 1
            
    return matriz_transform

# Toma una matriz de canal y aplica todas las reducciones suficientes
def realizarReduccionMaxima(matriz_canal):
    matriz_actual = [fila[:] for fila in matriz_canal]
    
    while True:
        num_cols_actual = len(matriz_actual[0])
        
        if num_cols_actual == 1:
            break
            
        par_encontrado = None

        for j in range(num_cols_actual):
            for k in range(j + 1, num_cols_actual):
                if verificarColumnasProporcionales(matriz_actual, j, k):
                    par_encontrado = (j, k)
                    break
            if par_encontrado:
                break
        
        if par_encontrado:
            j, k = par_encontrado
            matriz_transform = genMatrizReduccion(matriz_actual, j, k)
            matriz_reducida = calcularMatrizCompuesta(matriz_actual, matriz_transform)
            matriz_actual = matriz_reducida
        else:
            break
            
    return matriz_actual


# Verifica si un canal es "Uniforme"
# Todas las filas son una permutación de la primera fila
def esCanalUniforme(matriz_canal):    
    huella_fila_1 = sorted(matriz_canal[0])
    
    for fila in matriz_canal[1:]:
        if sorted(fila) != huella_fila_1:
            return False
            
    return True


# Calcula la capacidad  de un canal si es de un tipo especial (Determinante, Sin Ruido o Uniforme)
def calcularCapacidadEspecial(matriz_canal):
    num_entradas = len(matriz_canal)
    num_salidas = len(matriz_canal[0])
    
    if esCanalDeterminante(matriz_canal):
        # C = log2(Nro de Salidas)
        return math.log2(num_salidas)

    if esCanalSinRuido(matriz_canal):
        # C = log2(Nro de Entradas)
        return math.log2(num_entradas)
        
    if esCanalUniforme(matriz_canal):
        # C = log2(Nro Salidas) - H(fila)
        # H(fila) es la entropía de cualquier fila (usamos la primera)
        entropia_fila = utils.calculoEntropia(matriz_canal[0])
        return math.log2(num_salidas) - entropia_fila

    # Si no es ninguno de los casos especiales:
    # La capacidad debe calcularse por métodos numéricos
    return None


# Estima la capacidad de un canal binario
def estimarCapacidadCanalBinario(matriz_canal, paso = 0.0001):
    capacidad_estimada = -1.0
    probabilidad_optima = 0.0
    
    num_pasos = int(1.0 / paso)
    for i in range(num_pasos + 1):
        p = i * paso
        probs_a_priori = [p, 1 - p]
        info_mutua_actual = utils.calcularInformacionMutua(probs_a_priori, matriz_canal)
        
        if info_mutua_actual > capacidad_estimada:
            capacidad_estimada = info_mutua_actual
            probabilidad_optima = p
            
    return capacidad_estimada, probabilidad_optima


# Calcula la probabilidad de error (P_E)
def calcularProbabilidadError(probs_priori, matriz_canal):
    num_entradas = len(matriz_canal)
    num_salidas = len(matriz_canal[0])

    indices_maximos_regla = [-1] * num_salidas
    
    for j in range(num_salidas):
        max_val = -1.0
        indice_max = -1
        for i in range(num_entradas):
            if matriz_canal[i][j] > max_val:
                max_val = matriz_canal[i][j]
                indice_max = i
        indices_maximos_regla[j] = indice_max

    prob_error = 0.0
    
    for j in range(num_salidas):
        for i in range(num_entradas):
            if i != indices_maximos_regla[j]:
                prob_simultanea_error = probs_priori[i] * matriz_canal[i][j]
                prob_error += prob_simultanea_error

    return prob_error