import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

matriz_canal_A = [
    [0.4, 0.6, 0, 0],
    [0, 0, 0.5, 0.5],
    [0, 0, 0.7, 0.3]
]
probs_A = utils.genProbabilidadesEquiprobables(len(matriz_canal_A))

matriz_canal_B = [
    [0.2, 0.3, 0.5],
    [0, 0, 1],
    [0, 0, 1]
]
probs_B = utils.genProbabilidadesEquiprobables(len(matriz_canal_B))

matriz_canal_C = [
    [0.4, 0, 0.2, 0.4],
    [0.4, 0.3, 0.2, 0.1],
    [0, 0.3, 0, 0.7]
]
probs_C = utils.genProbabilidadesEquiprobables(len(matriz_canal_C))

matriz_canal_D = [
    [0, 0.5, 0, 0.5],
    [0.8, 0, 0.2, 0],
    [0, 0.5, 0, 0.5],
    [0.8, 0, 0.2, 0]
]
probs_D = utils.genProbabilidadesEquiprobables(len(matriz_canal_D))

probs_lista = [probs_A, probs_B, probs_C, probs_D]
matrices_lista = [matriz_canal_A, matriz_canal_B, matriz_canal_C, matriz_canal_D]
decimales=1

for i, (probs_priori, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):
    print(f"\n--- ANALIZANDO CANAL {i} ---")

    # Guardamos la matriz actual para irla reduciendo
    matriz_actual = matriz_canal
    paso_reduccion = 0

    # (b) Calcular la información mutua en cada paso
    print(f"\nMatriz Original (Paso {paso_reduccion}):")
    utils.imprimirMatriz(matriz_actual, decimales)
    
    informacion_mutua = utils.calcularInformacionMutua(probs_priori, matriz_actual)
    print(f"Información Mutua (Paso {paso_reduccion}): {informacion_mutua:.2f} bits")

    # (a) Efectuar todas las reducciones suficientes posibles
    while True:
        num_cols_actual = len(matriz_actual[0])
        par_encontrado = None

        # 1. Buscar un par de columnas reducibles
        for j in range(num_cols_actual):
            for k in range(j + 1, num_cols_actual):
                # Usamos la función del Ej 6a
                if TP6_Funciones.verificarColumnasProporcionales(matriz_actual, j, k):
                    par_encontrado = (j, k)
                    break
            if par_encontrado:
                break
        
        # 2. Si encontramos un par, reducimos la matriz
        if par_encontrado:
            paso_reduccion += 1
            j, k = par_encontrado
            print(f"\n[+] Reducción Suficiente (Paso {paso_reduccion}): Combinando columnas ({j}, {k})")

            # (Ej 6b) Generar la matriz de transformación P(C|B)
            matriz_transform = TP6_Funciones.generarMatrizReduccion(matriz_actual, j, k)
            
            # (Ej 4) Multiplicar para obtener el canal reducido P(C|A)
            matriz_reducida = TP6_Funciones.calcularMatrizCompuesta(matriz_actual, matriz_transform)
            
            # (b) Calcular la información mutua del nuevo canal
            informacion_mutua = utils.calcularInformacionMutua(probs_priori, matriz_reducida)
            
            print(f"Matriz Reducida (Paso {paso_reduccion}):")
            utils.imprimirMatriz(matriz_reducida, decimales)
            print(f"Información Mutua (Paso {paso_reduccion}): {informacion_mutua:.2f} bits")

            # Actualizamos la matriz para la siguiente iteración del 'while'
            matriz_actual = matriz_reducida
        
        # 3. Si no encontramos más pares, terminamos
        else:
            print("\n[!] No hay más reducciones suficientes posibles.")
            break

    # (c) Verificar si se obtiene un canal reducido determinante
    # (Usamos la función del Ej 2b)
    es_determinante = TP6_Funciones.esCanalDeterminante(matriz_actual)
    print(f"\n(c) ¿El canal reducido final es determinante? {es_determinante}")