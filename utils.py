import math
import random
import itertools

"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 2   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Calculo de la Informacion de la probabilidad 'p' en base 'base' (2 por defecto)
def calculoInformacion(p, base = 2):
    if p <= 0:
        return 0
    return math.log(1/p, base)


# Calculo de la Entropia de una fuente de informacion nula
def calculoEntropia(probabilidades, base = 2):
    informacion = [calculoInformacion(p, base) for p in probabilidades]
    return sum(a * b for a, b in zip(probabilidades, informacion))


# Generar el alfabeto de una cadena
def genAlfabeto(cadena):
    alfabeto = []
    for simbolo in cadena:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)

    return alfabeto


# Generar las probabilidades de un alfabeto de una cadena
def genProbabilidadesAlf(cadena):
    alfabeto = genAlfabeto(cadena)
    probabilidades = []
    cant_simboloacteres = len(cadena)
    for simbolo in alfabeto:
        probabilidades.append(cadena.count(simbolo) / cant_simboloacteres)

    return probabilidades


# Generar mensaje de la fuente de memoria nula
def genMensaje(alfabeto, probabilidades, longitud_msj = 20):
    # crear distribución acumulada
    prob_acum = []
    total = 0
    for p in probabilidades:
        total += p
        prob_acum.append(total)

    msj = []
    for _ in range(longitud_msj):
        r = random.random()  # número aleatorio entre 0 y 1
        for simbolo, limite in zip(alfabeto, prob_acum):
            if r < limite:
                msj.append(simbolo)
                break

    return "".join(msj)


# Calculo de la Entropia en fuente binaria (W)
def calculoEntropiaBin(probW, base = 2):
    probabilidades = [probW, 1 - probW]
    return calculoEntropia(probabilidades, base)


# Generar alfabeto de extension de orden N
def genAlfabetoOrdN(alfabeto, N):
    if N == 1:
        return alfabeto
    else:
        alf_menor = genAlfabetoOrdN(alfabeto, N - 1)
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


# itertools: Generar alfabeto y probabilidades de orden N
def itertools_GenListasOrdN(alfabeto, probabilidades, N):
    # Generar alfabeto extendido
    alf_extension = ["".join(tupla) for tupla in itertools.product(alfabeto, repeat = N)]
    
    # Generar probabilidades extendidas
    prob_extension = []
    for tupla in itertools.product(range(len(alfabeto)), repeat = N):
        p = 1
        for i in tupla:
            p *= probabilidades[i]
        prob_extension.append(p)

    return alf_extension, prob_extension


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


# Generar matriz de ocurrencias
def genMatrizOcurrencias(cadena):
    alfabeto = genAlfabeto(cadena)
    N = len(alfabeto)
    matriz_ocurrencias = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(cadena) - 1):
        origen = alfabeto.index(cadena[i])
        destino = alfabeto.index(cadena[i + 1])
        matriz_ocurrencias[destino][origen] += 1

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


# Generar mensaje de la fuente Markov
def genMensajeMarkov(alfabeto, matriz, longitud_msj = 20, estado_inicial = None):
    N = len(alfabeto)

    # Si no se pasa estado inicial, arrancamos al azar
    if estado_inicial is None:
        estado_actual = random.randrange(N)
    else:
        estado_actual = alfabeto.index(estado_inicial)

    msj = [alfabeto[estado_actual]]

    for _ in range(longitud_msj - 1):
        # Probabilidades de transición desde este estado (columna)
        probs = [matriz[i][estado_actual] for i in range(N)]

        # Elegir siguiente estado según probs
        siguiente_estado = random.choices(range(N), weights = probs, k = 1)[0]

        msj.append(alfabeto[siguiente_estado])
        estado_actual = siguiente_estado

    return "".join(msj)


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


# Analizar si la matriz es ergodica o no
def esFuenteErgodica(matriz, tol = 1e-6):
    """
    Determina si una fuente de Markov es ergódica.
    La matriz debe tener columnas que sumen 1.
    
    Retorna True si es ergódica, False en caso contrario.
    """
    N = len(matriz)
    
    # Generar matriz de conectividad: 1 si hay transición posible, 0 si no
    alcanzable = [[1 if matriz[i][j] > tol else 0 for j in range(N)] for i in range(N)]
    
    # Propagamos conexiones hasta N-1 pasos
    for _ in range(N - 1):
        nueva_conectividad = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # j es alcanzable desde i si existe k tal que i->k y k->j
                for k in range(N):
                    if alcanzable[i][k] and alcanzable[k][j]:
                        nueva_conectividad[i][j] = 1
                        break  # suficiente con un camino
        alcanzable = nueva_conectividad
    
    # Si hay algún par de estados que no se alcanza, no es ergódica
    for i in range(N):
        for j in range(N):
            if alcanzable[i][j] == 0:
                return False
    return True


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 3   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Verifica si una lista de codigos es 'No Singular'
def esNoSingular(codigos):
    return len(codigos) == len(set(codigos))


# Verifica si una lista de codigos es 'No Singular', mediante un for
def esNoSingularFor(codigos):
    n = len(codigos)
    for i in range(n):
        for j in range(i+1, n):
            if codigos[i] == codigos[j]:
                return False  # encontró dos iguales → no es no singular
    return True  # todas distintas


# Verifica si una lista de codigos es 'Instantaneo'
def esInstantaneo(codigos):
    n = len(codigos)
    for i in range(n):
        for j in range(n):
            if i != j:
                if codigos[j].startswith(codigos[i]):
                    return False  # cod[i] es prefijo de cod[j]
    return True


# Verifica si una lista de codigos es 'Univoco'
def esUnivoco(codigos):
    i = -1
    C = set(codigos)
    S1 = set(codigos)
    set_vistos = []
    set_vistos.append(S1)

    # Iterar para construir S2, S3, ...
    while True:
        s_sig = set()
        i += 1

        for x in S1:
            for y in set_vistos[i]:
                if x != y:
                    # Si x es prefijo de y, agregar sufijo de y
                    if y.startswith(x):
                        s_sig.add(y[len(x):])

                    # Si y es prefijo de x, agregar sufijo de x
                    if x.startswith(y):
                        s_sig.add(x[len(y):])

        # Condición 1: ¿algún elemento de Si está en C?
        if any(pal in C for pal in s_sig):
            return False  # no es unívoco

        # Condición 2: ¿ya vimos este conjunto antes?
        if s_sig in set_vistos:
            return True  # es unívoco
        
        set_vistos.append(s_sig)


# Devolver que tipo de codigo
def tipoCodigo(codigos):
    if esNoSingular(codigos):
        if esInstantaneo(codigos):
            return "Instantáneo"
        else:
            if esUnivoco(codigos):
                return "Unívoco"
            else:        
                return "No singular"
    else:
        return "Bloque"


# Generar alfabeto de los codigos
def genAlfabetoCodigos(codigos):
    cadena = ""

    for cod in codigos:
        for caracter in cod:
            if caracter not in cadena:
                cadena += caracter

    return cadena


# Generar longitudes de los codigos
def genLongitudesCodigos(codigos):
    return [len(palabra) for palabra in codigos]


# Calculo de la sumatoria de la inecuacion de Kraft
def calculoInecuacionKraft(codigos):
    r = len(genAlfabetoCodigos(codigos))
    longitudes = genLongitudesCodigos(codigos)
    return sum(r ** (-l) for l in longitudes)


# Calculo de la Informacion de la probabilidad 'p' en base 'r'
def calculoInformacionR(p, r):
    if p <= 0:
        return 0
    return math.log(1/p, r)


# Calculo de la entropia en base 'r'
def calculoEntropiaCP(codigos, probabilidades):
    r = len(genAlfabetoCodigos(codigos))
    informacion = [calculoInformacionR(p, r) for p in probabilidades]
    return sum(a * b for a, b in zip(probabilidades, informacion))


# Calculo de la longitud media
def calculoLongitudMedia(codigos, probabilidades):
    longitudes = genLongitudesCodigos(codigos)
    return sum(a * b for a, b in zip(probabilidades, longitudes))


# Calculo de la longitud ideal
def calculoLongitudIdeal(probabilidades, r):
    return [math.ceil(calculoInformacionR(p, r)) for p in probabilidades]


# Verificar si es codigo compacto
def esCodigoCompacto(codigos, probabilidades):
    if not (esNoSingular(codigos) and esInstantaneo(codigos)):
        return False
    
    r = len(genAlfabetoCodigos(codigos))
    longitudes = genLongitudesCodigos(codigos)
    long_ideales = calculoLongitudIdeal(probabilidades, r)

    for li, l in zip(long_ideales, longitudes):
        if l > li:
            return False
            
    return True


# Generar mensaje de la fuente de memoria
def genMensajeCP(codigos, probabilidades, N):
    msj = [random.choices(codigos, weights=probabilidades)[0] for _ in range(N)]
    return ''.join(msj)


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 4   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Verifica si se cumple el Primer Teorema de Shannon (pasar codigos extendidos)
def cumpleShannon(probabilidades, codigos, N = 1):
    prob_ext = genProbabilidadesAlfOrdN(probabilidades, N)
    long_media = calculoLongitudMedia(codigos, prob_ext)
    entropia = calculoEntropiaCP(codigos, probabilidades)

    long_media_norm = long_media / N
    lim_inf = entropia
    lim_sup = entropia + (1 / N)

    return  lim_inf <= long_media_norm < lim_sup


# Algoritmo de Huffman (iterativo)
def algoritmoHuffman(probabilidades):
    items = [[prob, [idx]] for idx, prob in enumerate(probabilidades)]
    codigos = [''] * len(probabilidades)

    while len(items) > 1:
        items.sort(key=lambda x: x[0])
        prob_baja, simbolos_bajos = items.pop(0)
        prob_alta, simbolos_altos = items.pop(0)

        for idx in simbolos_bajos:
            codigos[idx] = '0' + codigos[idx]

        for idx in simbolos_altos:
            codigos[idx] = '1' + codigos[idx]

        nuevo_item = [prob_baja + prob_alta, simbolos_bajos + simbolos_altos]
        items.append(nuevo_item)

    return codigos


# Algoritmo de Shannon-Fano, inicializacion
def algoritmoShannonFano(probabilidades):
    items = [[prob, idx] for idx, prob in enumerate(probabilidades)]
    items.sort(key=lambda x: x[0], reverse = True)
    codigos = [''] * len(probabilidades)
    recursividadShannonFano(items, codigos)
    return codigos

# Algoritmo de Shannon-Fano, parte recursiva
def recursividadShannonFano(items, codigos, prefijo = ''):
    N = len(items)
    if N == 1:
        codigos[items[0][1]] = prefijo
    else:   
        suma_total = sum(nodo[0] for nodo in items)
        suma_mitad = suma_total / 2

        suma_parcial = 0
        punto_corte = 0
        min_diferencia = float('inf')

        for i in range(len(items) - 1):
            suma_parcial += items[i][0]
            diferencia = abs(suma_parcial - suma_mitad)
            if diferencia < min_diferencia:
                min_diferencia = diferencia
                punto_corte = i + 1

        grupo_superior = items[:punto_corte]
        grupo_inferior = items[punto_corte:]
        
        recursividadShannonFano(grupo_superior, codigos, prefijo + '1')
        recursividadShannonFano(grupo_inferior, codigos, prefijo + '0')


# Calculo del Rendimiento (η) y la Redundancia (1 - η)
def calculoRendimientoYRedundancia(codigos, probabilidades):
    entropia = calculoEntropiaCP(codigos, probabilidades)
    long_media = calculoLongitudMedia(codigos, probabilidades)

    rendimiento = entropia / long_media
    redundancia = 1 - rendimiento

    return rendimiento, redundancia