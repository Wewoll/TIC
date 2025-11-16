import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils
import math

# Verifica si dos columnas de una matriz de canal son proporcionales en cualquiera de los dos sentidos  
def verificarColumnasProporcionales(matriz, c1, c2):
    return (proporcionalEnUnSentido(matriz, c1, c2) or proporcionalEnUnSentido(matriz, c2, c1))

# Verifica si dos columnas de una matriz de canal son proporcionales (condición de reducción suficiente)
def proporcionalEnUnSentido(matriz, a, b, tol = 1e-9):
    constante = None

    for fila in range(len(matriz)):
        x = matriz[fila][a]
        y = matriz[fila][b]

        es_x_cero = math.isclose(x, 0.0, abs_tol=tol)
        es_y_cero = math.isclose(y, 0.0, abs_tol=tol)

        # 0 = C * 0 → válido
        if es_x_cero and es_y_cero:
            continue

        # Si y = 0 pero x ≠ 0 → no se puede cumplir x = C·y
        if es_y_cero and not es_x_cero:
            return False

        # Calcular ratio
        ratio = x / y

        if constante is None:
            constante = ratio
        elif not math.isclose(ratio, constante, abs_tol=tol):
            return False

    return True


# Genera la matriz de transformación ("canal determinante") para combinar las dos columnas
def genMatrizReduccion(matriz_canal, idx_col1, idx_col2):
    # 1. Obtenemos las dimensiones originales (de la matriz P(B|A))
    num_columnas_original = len(matriz_canal[0]) # ej: 4
    num_columnas_nueva = num_columnas_original - 1  # ej: 3
    
    # 2. Creamos la matriz de transformación vacía P(C|B)
    #    Tendrá N_original filas x N_nueva columnas (ej: 4x3)
    matriz_transform = [[0.0] * num_columnas_nueva for _ in range(num_columnas_original)]
    
    # 3. Determinamos qué columna se "fusiona" y cuál se "elimina"
    #    La nueva columna fusionada tomará el índice más bajo.
    idx_col_fusionada = min(idx_col1, idx_col2)
    idx_col_eliminada = max(idx_col1, idx_col2)
    
    # 4. Llenamos la matriz de transformación
    puntero_col_nueva = 0
    
    # 'i' itera sobre las filas de la matriz de transformación
    # (que son las columnas de la matriz original)
    for i in range(num_columnas_original):
        if i == idx_col_eliminada:
            # --- Caso Especial: La columna que "desaparece" ---
            # Le asignamos un 1.0 en la columna "fusionada"
            matriz_transform[i][idx_col_fusionada] = 1.0
            
        else:
            # --- Caso Normal: Todas las demás columnas ---
            # Le asignamos un 1.0 en la siguiente columna nueva disponible
            matriz_transform[i][puntero_col_nueva] = 1.0
            # Avanzamos el puntero para la próxima columna normal
            puntero_col_nueva += 1
            
    return matriz_transform