import math
import random

# Calculo de la Informacion de la probabilidad 'p' en base 'base' (2 por defecto)
def calculoInformacion(p, base = 2):
    if p <= 0:
        return 0
    return math.log(1/p, base)

# Calculo de la Entropia de una fuente de informacion nula
def calculoEntropia(probabilidades, base = 2):
    informacion = [calculoInformacion(p, base) for p in probabilidades]
    return sum(a * b for a, b in zip(probabilidades, informacion))

# Calculo de la Entropia de una fuente de Markov
def calculoEntropiaMarkov(matriz, base = 2):
    entropiaMarkov = 0
    vector_estacionario = genVectorEstacionario(matriz)
    N = len(matriz)

    for j in range(N):
        # Tomo la columna j (todas las probabilidades de ir a otro estado desde j)
        prob_columna = [matriz[i][j] for i in range(N)]

        # Entropía condicional desde el estado j
        H_cond = calculoEntropia(prob_columna, base)

        # Pondero por la probabilidad de estar en el estado j
        entropiaMarkov += vector_estacionario[j] * H_cond

    return entropiaMarkov

# Generar el alfabeto de una cadena
def genAlfabeto(cadena):
    alfabeto = []
    for simbolo in cadena:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    alfabeto.sort()
    return alfabeto

# Generar las probabilidades de un alfabeto de una cadena
def genProbabilidadesAlf(cadena):
    alfabeto = genAlfabeto(cadena)
    probabilidades = []
    cant_simboloacteres = len(cadena)
    for simbolo in alfabeto:
        probabilidades.append(cadena.count(simbolo) / cant_simboloacteres)

    return probabilidades

# Generar alfabeto de extension de orden N
def genAlfabetoOrnN(alfabeto, N):
    if N == 1:
        return alfabeto
    else:
        alf_menor = genAlfabetoOrnN(alfabeto, N - 1)
        alf_extension = []
        for prefijo in alf_menor:
            for simbolo in alfabeto:
                alf_extension.append(prefijo + simbolo)

    return alf_extension

# Generar probabilidades del alfabeto de extencion de orden N
def genProbabilidadesAlfOrdN(probabilidades, N):
    if N == 1:
        return probabilidades
    else:
        prob_menor = genProbabilidadesAlfOrdN(probabilidades, N - 1)
        prob_extension = []
        for prob_parcial in prob_menor:
            for p in probabilidades:
                prob_extension.append(prob_parcial * p)

    return prob_extension

# Generar vector estacionario
def genVectorEstacionario(matriz, tolerancia = 0.01, iteraciones = 500):
    N = len(matriz)
    dif_max = 1
    vector_estacionario = [1/N for _ in range(N)]  # Inicializar vector estacionario equiprobable

    # Ciclo para generar un vector estacionario
    while (0 < iteraciones and dif_max > tolerancia):
        iteraciones -= 1
        vector_est_ant = vector_estacionario.copy()
        vector_estacionario = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                vector_estacionario[i] += matriz[i][j] * vector_est_ant[j]
            
        dif_max = maxDifVec(vector_est_ant, vector_estacionario)

    return vector_estacionario

# Busca la maxima diferencia entre dos valores paralelos
def maxDifVec(vector_ant, vector_nuevo):
    dif_max = 0
    for i in range(len(vector_ant)):
        dif = abs(vector_ant[i] - vector_nuevo[i])
        if dif > dif_max:
            dif_max = dif
    return dif_max

# Generar matriz de ocurrencias
def genMatrizOcurrencias(cadena):
    alfabeto = genAlfabeto(cadena)
    N = len(alfabeto)
    matriz_ocurrencias = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(cadena) - 1):
        origen = alfabeto.index(cadena[i])
        destino = alfabeto.index(cadena[i + 1])
        matriz_ocurrencias[origen][destino] += 1

    return matriz_ocurrencias

# Generar matriz de probabilidades (de transicion, normalizando la de ocurrencias)
def genMatrizProbabilidades(matriz_ocurrencias):
    N = len(matriz_ocurrencias)
    matriz_prob = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):  # columna
        col_sum = sum(matriz_ocurrencias[i][j] for i in range(N))
        if col_sum > 0:
            for i in range(N):  # fila
                matriz_prob[i][j] = matriz_ocurrencias[i][j] / col_sum

    return matriz_prob

# Generar matriz de transicion
def genMatrizTransicion(cadena):
    matriz = genMatrizOcurrencias(cadena)
    matriz = genMatrizProbabilidades(matriz)
    return matriz

# Analizar si una fuente de memoria es nula o no nula
def esFuenteSinMemoria(matriz, tolerancia):
    """
    Devuelve True si la fuente representada por la matriz de transición
    puede considerarse sin memoria, es decir, si las filas son casi iguales
    dentro de la tolerancia dada.
    """
    
    N = len(matriz)
    dif_max = 0
    
    for i in range(N):
        dif_fila = max(matriz[i]) - min(matriz[i])
        
        if dif_fila > dif_max:
            dif_max = dif_fila

    return dif_max < tolerancia



cadena_1 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"
cadena_2 = "]]]([[]))([(])]([]([([([)([([([[([))][([([[([)([(]"
cadenas = [cadena_1, cadena_2]
i = 1

for cadena in cadenas:
    print(f"\nPregunta {i}")
    i += 1

    # a)
    alfabeto = genAlfabeto(cadena)
    probabilidades = genProbabilidadesAlf(cadena)
    print(f"Alfabeto: {alfabeto}")
    print(f"Probabilidades: {probabilidades}")

    # b)
    matriz = genMatrizTransicion(cadena)
    print("Matriz: ")
    for k in range(len(matriz)):
        print(matriz[k])

    # c)
    res = esFuenteSinMemoria(matriz, 0.001)
    print(f"Es fuente sin memoria: {res}")

    # d)
    if res:
        entropia = calculoEntropia(probabilidades)
    else:
        entropia = calculoEntropiaMarkov(matriz)
    print(f"Entropia: {entropia}")
    
    if res:
        # e)
        alfabeto_orden2 = genAlfabetoOrnN(alfabeto, 2)
        probabilidades_orden2 = genProbabilidadesAlfOrdN(probabilidades, 2)
        entropia_orden2 = calculoEntropia(probabilidades_orden2)
        print(f"Alfabeto Orden 2: {alfabeto_orden2}")
        print(f"Probabilidades Orden 2: {probabilidades_orden2}")
        k = alfabeto_orden2.index("*+")
        print(f"P(\"*+\") = {probabilidades_orden2[k]}")
        k = alfabeto_orden2.index("-/")
        print(f"P(\"-/\") = {probabilidades_orden2[k]}")
        print(f"Entropia Orden 2: {entropia_orden2}")
    else:
        vector_estacionario = genVectorEstacionario(matriz)
        print(f"Vector Estacionario: {vector_estacionario}")
